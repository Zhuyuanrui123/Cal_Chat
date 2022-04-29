from django import template


def count_comments(comments, post):
    return comments.filter(post=post).count()


register = template.Library()
register.filter(count_comments)
