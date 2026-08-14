from django.urls import path
from . import views

urlpatterns = [
    path('register_cine_board/', views.RegisterCineBoardView.as_view()),
    path('login_cine_board/', views.AuthLoginCineBoardView.as_view()),
    path('logout_cine_board/', views.AuthLogoutCineBoardView.as_view()),
    path('profile_cine_board/', views.ProfileCineBoardView.as_view()),

    path('cine_board_list/', views.ReadCineBoardView.as_view()),
    path('cine_board_detail/<int:id>/', views.DetailCineBoardView.as_view()),
    path('create_cine_board/', views.CreateCineBoardView.as_view()),
    path('update_cine_board/<int:id>/', views.UpdateCineBoardView.as_view()),
    path('delete_cine_board/<int:id>/', views.DeleteCineBoardView.as_view()),


    path('add_comment/<int:id>/', views.AddCommentView.as_view()),
    path('reserve_vip/<int:id>/', views.ReserveVIPView.as_view()),
]