
from django.shortcuts import render
from django.views import generic

from .models import Highlight


class PostDetail(generic.DetailView):
    model = Highlight
    template_name = '_sidebar.html'

# class HighlightDetail(generic.HighlightView):
#     model = Highlight
#     template_name = '_sidebar.html'
