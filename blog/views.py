from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

# https://tutorial.djangogirls.org/en/django_views/
# https://tutorial.djangogirls.org/en/dynamic_data_in_templates/
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {})

