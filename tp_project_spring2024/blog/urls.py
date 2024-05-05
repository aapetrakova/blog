from django.urls import path
from .views import (
    MainPageView,
    PostDetailView,
    TagView,
    SearchResultsView,
    ProfileDetailView,
    ProfileUpdateView,
    PostCreateView
)

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('blog/<str:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('tag/<slug>/', TagView.as_view(), name="tag"),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('edit_profile/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('user_profile/<slug>/', ProfileDetailView.as_view(), name='profile_detail'),
]