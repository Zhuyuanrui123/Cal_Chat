from django.urls import include, path
from posts.views import *

urlpatterns = [
    path('', HomepagePostsView.as_view(), name='home_posts'),
    path('posts/new/', NewPostView.as_view(), name='new_post'),
    path('posts/<int:id>/', PostView.as_view(), name='view_post'),
]
