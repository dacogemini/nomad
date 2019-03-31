from django.shortcuts import render


def index(request):
    return render(request, 'packages/packages.html')


def package(request):
    return render(request, 'packages/search.html')


def search(request):
    return render(request, 'packages/package.html')
