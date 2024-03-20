from django.urls import path
from .views import MainPageView, PostDetailView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('blog/<slug>/', PostDetailView.as_view(), name='post_detail'),
]