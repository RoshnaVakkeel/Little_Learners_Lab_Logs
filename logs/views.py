from django.shortcuts import render
from django.views import generic
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
