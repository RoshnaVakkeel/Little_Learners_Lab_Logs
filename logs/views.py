from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import PostForm, CommentForm


class PostList(generic.ListView):
    ''' Class to show list of posts'''
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class AllPosts(generic.ListView):
    """
    to get all the lab log posts, and display 6 posts per page
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('created_on')  # noqa: E501
    template_name = 'lab_logs.html'
    paginate_by = 12


class PostDetail(View):
    ''' Class to show selcted post in detail view '''
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
                "comments": comments,
                "commented":False,
                "liked": liked,
                "comment_form":CommentForm(),
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.user_comments.order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment  = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "log_details.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form":CommentForm(),
            }
        )


class CreatePost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_logs.html'
