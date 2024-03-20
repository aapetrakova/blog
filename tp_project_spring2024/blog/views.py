from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator

from .models import Post


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        paginator = Paginator(posts, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'blog/main_page.html', context={
            'page_obj': page_obj,
        })


class PostDetailView(View):

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, url=slug)
        last_posts = Post.objects.all().order_by('-id')[:5]
        return render(request, 'blog/post_details.html', context={
            'post': post,
            'last_posts': last_posts,
        })