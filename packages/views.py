from django.shortcuts import render

from .models import Package

def index(request):
    packages = Package.objects.all()

    context = {
        'packages': packages
    }
    return render(request, 'packages/packages.html', context)


def package(request):
    return render(request, 'packages/search.html')


def search(request):
    return render(request, 'packages/package.html')
