from django.shortcuts import render

# Create your views here.

# https://tutorial.djangogirls.org/en/django_views/
def post_list(request):
    return render(request, 'blog/post_list.html', {})