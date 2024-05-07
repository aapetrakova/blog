"""
File with urls for connecting and displaying the main page of the blog and pages of individual posts.
"""

from django.urls import path
from blog.views import MainPageView, PostDetailView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('blog/<slug>/', PostDetailView.as_view(), name='post_detail'),
]