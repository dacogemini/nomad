from . import views
from django.urls import path

urlpatterns = [
    path('', views.HighlightDetail.as_view(), name='highlight_detail'),
]
