from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator

from user.models import UserPost

from message.models import Comment
from message.forms import CommentForm
from django.http import HttpResponseRedirect


class MainPageView(View):
    """A class for visualizing the main page of a blog"""

    def get(self, request, *args, **kwargs):
        """"GET request for the main page of a blog

        :param request: GET request
        :param args:
        :param kwargs:
        :return: the main page of the blog
        """

        posts = UserPost.objects.all()
        paginator = Paginator(posts, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'blog/main_page.html', context={
            'page_obj': page_obj,
        })


class PostDetailView(View):
    '''A class for visualizing the post detail page'''

    def get(self, request, slug, *args, **kwargs):
        """GET request for the post detail page of a blog

        :param request: GET request
        :param slug: url of the post
        :param args:
        :param kwargs:
        :return: the post detail page
        """

        post = get_object_or_404(UserPost, url=slug)
        last_posts = UserPost.objects.all().order_by('-id')[:5]
        comment_form = CommentForm()
        return render(request, 'blog/post_details.html', context={
            'post': post,
            'last_posts': last_posts,
            'comment_form': comment_form,
        })

    def post(self, request, slug, *args, **kwargs):
        """POST request for the comments on post detail page of a blog

        :param request: POST request
        :param slug: url of the post
        :param args:
        :param kwargs:
        :return: the comment on post detail page
        """

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['text']
            username = self.request.user
            post = get_object_or_404(UserPost, url=slug)
            comment = Comment.objects.create(post=post, username=username, text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, 'myblog/post_details.html', context={
            'comment_form': comment_form
        })