from django.urls import path
from .views import MainPageView, PostDetailView, TagView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('blog/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('tag/<slug>/', TagView.as_view(), name="tag"),
]