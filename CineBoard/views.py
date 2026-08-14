from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from . import models, forms


class RegisterCineBoardView(generic.CreateView):
    form_class = forms.CustomRegisterForm
    template_name = 'register_cine_board.html'
    success_url = '/profile_cine_board/'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class AuthLoginCineBoardView(generic.FormView):
    form_class = AuthenticationForm
    template_name = 'login_cine_board.html'
    success_url = '/profile_cine_board/'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

class AuthLogoutCineBoardView(generic.View):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect('/login_cine_board/')

class ProfileCineBoardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'profile_cine_board.html'


class ReadCineBoardView(generic.ListView):
    model = models.CinemaModel
    template_name = 'read_cine_board.html'
    context_object_name = 'cine_board_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        genre_id = self.request.GET.get('genre')

        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        if genre_id:
            queryset = queryset.filter(genres__id=genre_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = models.Genre.objects.all()
        return context

class DetailCineBoardView(generic.DetailView):
    model = models.CinemaModel
    template_name = 'cine_board_detail.html'
    context_object_name = 'film'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = forms.CommentForm()
        context['vip_form'] = forms.VIPReservationForm()
        return context


class CreateCineBoardView(generic.CreateView):
    model = models.CinemaModel
    form_class = forms.CinemaForm
    template_name = 'create_cine_board.html'
    success_url = '/cine_board_list/'

class UpdateCineBoardView(generic.UpdateView):
    model = models.CinemaModel
    form_class = forms.CinemaForm
    template_name = 'update_cine_board.html'
    pk_url_kwarg = 'id'
    success_url = '/cine_board_list/'

class DeleteCineBoardView(generic.DeleteView):
    model = models.CinemaModel
    template_name = 'confirm_cine_delete.html'
    pk_url_kwarg = 'id'
    success_url = '/cine_board_list/'


class AddCommentView(LoginRequiredMixin, generic.View):
    def post(self, request, id):
        film = get_object_or_404(models.CinemaModel, id=id)
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.film = film
            comment.author = request.user
            comment.save()
        return redirect(f'/cine_board_detail/{film.id}/')

class ReserveVIPView(LoginRequiredMixin, generic.View):
    def post(self, request, id):
        film = get_object_or_404(models.CinemaModel, id=id)
        if models.VIPReservation.objects.filter(user=request.user).exists():
            return redirect(f'/cine_board_detail/{film.id}/')

        form = forms.VIPReservationForm(request.POST)
        if form.is_valid():
            vip = form.save(commit=False)
            vip.user = request.user
            vip.film = film
            vip.save()
        return redirect(f'/cine_board_detail/{film.id}/')