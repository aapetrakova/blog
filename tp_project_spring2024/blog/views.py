from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator

from user.models import UserPost

from message.models import Comment
from message.forms import CommentForm
from django.http import HttpResponseRedirect

from taggit.models import Tag

from django.db.models import Q


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        posts = UserPost.objects.all()
        paginator = Paginator(posts, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'blog/main_page.html', context={
            'page_obj': page_obj,
        })


class PostDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(UserPost, url=slug)
        common_tags = UserPost.tag.most_common()
        last_posts = UserPost.objects.all().order_by('-id')[:5]
        comment_form = CommentForm()
        return render(request, 'blog/post_details.html', context={
            'post': post,
            'common_tags': common_tags,
            'last_posts': last_posts,
            'comment_form': comment_form
        })

    def post(self, request, slug, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['text']
            username = self.request.user
            post = get_object_or_404(UserPost, url=slug)
            comment = Comment.objects.create(post=post, username=username, text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, 'blog/post_details.html', context={
            'comment_form': comment_form
        })



class TagView(View):
    def get(self, request, slug, *args, **kwargs):
        tag = get_object_or_404(Tag, slug=slug)
        posts = UserPost.objects.filter(tag=tag)
        common_tags = UserPost.tag.most_common()
        return render(request, 'blog/tag.html', context={
            'title': f'#ТЕГ {tag}',
            'posts': posts,
            'common_tags': common_tags
        })


class SearchResultsView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        results = ""
        if query:
            results = UserPost.objects.filter(
                Q(h1__icontains=query) | Q(content__icontains=query)
            )
        paginator = Paginator(results, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'blog/search.html', context={
            'title': 'Поиск',
            'results': page_obj,
            'count': paginator.count
        })