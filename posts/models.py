import random
from django.contrib.auth.models import User
from django.db import models
from profile.helpers import create_profile_with_random_nick
from profile.models import Profile, NICKNAME_CHOICES


class Post(models.Model):
    posted_by = models.ForeignKey(User, models.CASCADE, null=False)
    content = models.TextField(null=False)
    timestamp = models.DateTimeField(auto_now=True, null=False)

    def get_nickname(self):
        try:
            profile = Profile.objects.get(user=self.posted_by)
        except Profile.DoesNotExist:
            profile = create_profile_with_random_nick(self.posted_by)
        return f'Anonymous {profile.nickname}'

    def __str__(self):
        return f'Post #{self.id} by {self.posted_by.username}'


class Comment(models.Model):
    posted_by = models.ForeignKey(User, models.CASCADE, null=False)
    post = models.ForeignKey(Post, models.CASCADE, null=False)
    timestamp = models.DateTimeField(auto_now=True, null=False)
    content = models.TextField()

    def get_nickname(self):
        try:
            profile = Profile.objects.get(user=self.posted_by)
        except Profile.DoesNotExist:
            profile = Profile(user=self.posted_by, nickname='something')
        return f'Anonymous {profile.nickname}'

    def __str__(self):
        return f'{self.posted_by.username}\'s comment on Post #{self.post.id}'
