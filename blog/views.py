from django.views import generic
from .models import Post

###########################################################################
# The built-in ListViews, a subclass of generic class-based-views renders
# a list with the objects of the specified model we just need to mention
# the template, similarly DetailView provides a detailed view for a given
# object of the model at the provided template. #
###########################################################################

# BLOG


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

# BLOG DETAIL


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
