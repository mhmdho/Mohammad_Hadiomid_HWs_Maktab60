from django.contrib import admin

from person.models import Student, Teacher

# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)