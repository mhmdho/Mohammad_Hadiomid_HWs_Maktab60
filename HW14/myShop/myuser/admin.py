from django.contrib import admin

from .models import Comment, Customer, Favorite, Supplier

# Register your models here.

admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Favorite)
admin.site.register(Comment)
