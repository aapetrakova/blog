"""
File with urls for registration, login and logout of user
"""

from django.urls import path
from .views import RegisterView, LoginView, logoutUser
from blog.views import MainPageView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', MainPageView.as_view(), name='main_page'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logoutUser, name="logout"),
]