from home.models import Contact, Comment, Blog, Profile
from django.contrib import admin

# Register your models here.

admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Profile)