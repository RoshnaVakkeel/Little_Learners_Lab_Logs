from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import PostForm


class CreatePost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_logs.html'


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(generic.DetailView):
    ''' Class to show single posts in a detail view '''
    model = Post
    template_name = 'log_details.html'