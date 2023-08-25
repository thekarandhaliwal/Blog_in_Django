from django.shortcuts import render
from django.http import HttpResponse
from blogApp.models import Post, Category

def home(request):
    posts = Post.objects.all()[:11]
    print(posts)

    category = Category.objects.all()
    data = {
        'post': posts,
        'cats': category
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    print(post)
    return render(request, 'posts.html', {'post': post})
