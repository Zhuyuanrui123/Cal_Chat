from django import forms
from posts.models import Post, Comment


class NewPostForm(forms.Form):
    content = forms.CharField(required=True)

    def create_post(self, user):
        post_obj = Post(posted_by=user, content=self.cleaned_data['content'])
        post_obj.save()


class NewCommentForm(forms.Form):
    content = forms.CharField(required=True)

    def add_comment(self, user, post):
        comment_obj = Comment(posted_by=user, post=post, content=self.cleaned_data['content'])
        comment_obj.save()
