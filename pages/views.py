from django.shortcuts import render
from django.http import HttpResponse

from packages.models import Package
from blog.models import Category, Post, Comment


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def blog(request):
    return render(request, 'pages/blog.html')
