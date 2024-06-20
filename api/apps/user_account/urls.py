from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_register, name='user-register'),
    path('login/', views.user_login, name='user-login'),
    path('list/', views.user_list, name='user-list'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),
    path('users/delete-all/', views.delete_all_users, name='delete-all-users'),
]
