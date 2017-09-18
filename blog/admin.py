from django.contrib import admin

# Register your models here.
# https://tutorial.djangogirls.org/en/django_admin/
from .models import Post
admin.site.register(Post)