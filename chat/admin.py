from django.contrib import admin
from .models import AuthenticationMethod, Poll, Choice, ImageReview
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(AuthenticationMethod)
admin.site.register(ImageReview)
