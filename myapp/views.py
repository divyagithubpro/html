from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request,"about.html")


def blog(request):
    return render(request,"blog.html")


def Class(request):
    return render(request,"class.html")


def index(request):
    return render(request,"index.html")

def hello(request):
    return render(request,"hello.html")