from django.shortcuts import render
from .models import Post

# Create your views here.

#CRUD - create retrive update delete

#List all the posts

def post_list_view(request):
    post_objects = Post.opjects.all()
    context = {
        'post_objects': post_objects

    }
    return render(request, "posts/index.html", context)