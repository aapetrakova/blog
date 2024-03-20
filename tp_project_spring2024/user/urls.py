from django.urls import path
from .views import RegisterView, LoginView, logoutUser
from django.contrib.auth.views import LogoutView
from blog.views import MainPageView
from tp_project_spring2024 import settings

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', MainPageView.as_view(), name='main_page'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logoutUser, name="logout"),
]