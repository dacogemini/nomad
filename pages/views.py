from django.shortcuts import render
from django.http import HttpResponse

from packages.models import Package


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')
