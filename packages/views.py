from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Package


def index(request):
    packages = Package.objects.order_by('list_date').filter(is_published=True)

    paginator = Paginator(packages, 6)
    page = request.GET.get('page')
    paged_packages = paginator.get_page(page)

    context = {
        'packages': paged_packages
    }
    return render(request, 'packages/packages.html', context)


def package(request):
    return render(request, 'packages/search.html')


def search(request, package_id):
    return render(request, 'packages/package.html')
