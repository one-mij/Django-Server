from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'newapp/home.html', context)

def blog(request):
    context = {}
    return render(request, 'newapp/blog.html', context)