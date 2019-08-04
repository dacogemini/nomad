from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Feature


def index(request):
    features = Feature.objects.all()
    # features = Feature.objects.order_by('list_date').filter(is_published=True)

    paginator = Paginator(features, 6)
    page = request.GET.get('page')
    paged_features = paginator.get_page(page)

    context = {
        'features': paged_features
    }
    return render(request, 'features/index.html', context)


def feature(request):
    return render(request, 'features/search.html')


def search(request, feature_id):
    return render(request, 'features/feature.html')
