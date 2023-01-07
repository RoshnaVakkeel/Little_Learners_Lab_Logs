from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import PostForm


class CreatePost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_logs.html'


class PostList(generic.ListView):
    ''' Class to show list of posts'''
    model = Post
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    ''' Class to show single posts in a detail view '''
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.user_comments.order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "log_details.html",
            {
                "post": post,
                "comments" : comments,
                "liked" : liked,
            }
        )