from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserCreateView.as_view(), name='signup'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('all_users', views.UserListView.as_view(), name='all_users'),
]