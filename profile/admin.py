from django.contrib import admin
from django.contrib.auth.decorators import login_required
from allauth.account.admin import EmailAddress
from allauth.socialaccount.admin import SocialAccount, SocialApp, SocialToken
from profile.models import *

# set admin site title
admin.site.site_header = 'Cal Chat'
admin.site.site_title = 'Cal Chat'

# disable django-allauth stuff
admin.site.unregister(EmailAddress)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialToken)

# register my stuff
admin.site.register(Profile)
