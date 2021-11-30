from django.contrib import admin

from .models import Comment, Favorite

# Register your models here.

admin.site.register(Favorite)
admin.site.register(Comment)
