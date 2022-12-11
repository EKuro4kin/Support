from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views
from .views import UserDetailView

urlpatterns = [
    path('create', views.UserCreateView.as_view(), name='create'),
    path('<int:pk>', UserDetailView.as_view(), name='detail'),
    path('all_users', views.UserListView.as_view(), name='all_users'),
    # path('profile', views.ProfileView.as_view(), name='profile'),

    # Урлы аутентификации
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]