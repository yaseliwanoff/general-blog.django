from django.shortcuts import render
from users.models import User


def index(request):
    context = {
        'title': 'blog',
        'users': User.objects.all(),
    }
    return render(request, 'myblog/home.html', context)


def posts(request):
    context = {
        'title': 'SLVNV - All posts',
    }
    return render(request, 'myblog/posts.html', context)
