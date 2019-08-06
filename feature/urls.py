from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='features'),
    path('<int:feature_id>', views.package, name='features'),
    path('search', views.search, name='search'),
]
