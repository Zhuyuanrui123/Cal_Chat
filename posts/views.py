from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from profile.models import Profile
from posts.forms import *
from posts.models import *


@method_decorator(login_required, name='dispatch')
class HomepagePostsView(TemplateView):
    template_name = 'home_posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_posts'] = Post.objects.all().order_by('-timestamp')
        context['all_comments'] = Comment.objects.all().order_by('post')
        return context


@method_decorator(login_required, name='dispatch')
class PostView(FormView):
    template_name = 'view_post.html'
    form_class = NewCommentForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        self.success_url = self.request.get_full_path
        context = super().get_context_data(**kwargs)
        try:
            context['post'] = Post.objects.get(id=self.kwargs['id'])
            context['comments'] = Comment.objects.filter(post=self.kwargs['id']).order_by('-timestamp')
        except Post.DoesNotExist:
            raise Http404
        try:
            profile = Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            profile = create_profile_with_random_nick(self.request.user)
        context['nickname'] = profile.nickname
        return context

    def form_valid(self, form):
        self.success_url = self.request.get_full_path()
        post_obj = Post.objects.get(id=self.kwargs['id'])
        form.add_comment(self.request.user, post_obj)
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class NewPostView(FormView):
    template_name = 'new_post.html'
    form_class = NewPostForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            profile = Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            profile = create_profile_with_random_nick(self.request.user)
        context['nickname'] = profile.nickname
        return context

    def form_valid(self, form):
        form.create_post(self.request.user)
        return super().form_valid(form)
