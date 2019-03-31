from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='packages'),
    path('<int:package_id>', views.package, name='package'),
    path('search', views.search, name='search'),
] 