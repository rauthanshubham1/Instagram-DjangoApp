from django.shortcuts import render

def posts(request):
    return render(request, "posts/posts.html")

def addpost(request):
    return render(request, "posts/addpost.html")