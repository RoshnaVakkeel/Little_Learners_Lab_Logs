from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView
from .models import Post
from .forms import PostForm, CommentForm, UploadFileForm, EditForm


class PostList(generic.ListView):
    ''' Class to show list of posts'''
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


class AllPosts(generic.ListView):
    """
    to get all the lab log posts, and display 12 posts per page
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('created_on')  # noqa: E501
    template_name = 'lab_logs.html'
    paginate_by = 12


class PostDetail(View):
    ''' Class to show selected post in detail view '''
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
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            }
        )

    def post(self, request, slug, *args, **kwargs):
        if request.user.is_authenticated:
            queryset = Post.objects.filter(status=1)
            post = get_object_or_404(queryset, slug=slug)
            comments = post.user_comments.order_by('-created_on')
            liked = False
            if post.likes.filter(id=self.request.user.id).exists():
                liked = True

            comment_form = CommentForm(data=request.POST)

            if comment_form.is_valid():
                comment_form.instance.name = request.user.username
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
                messages.success(request, 'Thank you for your comment!')
            else:
                comment_form = CommentForm()

            # User HttpResponseRedirect here instead of render to ensure comment
            # is not re-submitted on page re-load
            return HttpResponseRedirect(reverse('log-details', args=[slug]))


class SharedPostsByUsers(LoginRequiredMixin, generic.ListView):
    """
    display all the posts (12 posts per page) added by currently
    logged in user
    """
    model = Post
    author = Post.author
    login_url = 'account_login'
    template_name = 'my_page.html'
    paginate_by = 12

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(author=self.request.user, status=1).order_by('-created_on')  # noqa: E501


@login_required()
def CreatePost(request):
    """ Add a post to the lab log post """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            form.save()
            messages.success(request, 'The post is being reviewed')
            return redirect(reverse('lab-logs'))
        else:
            messages.error(request, 'Failed to Create a post. \
                           Please ensure the form is valid.')
    else:
        form = PostForm()

    template = 'add_logs.html',
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def EditPost(request, slug):
    """ Edit a post to the lab log post """
    post = get_object_or_404(Post, slug=slug)
    if request.user.id == post.author.id:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.slug = slugify(post.title)
                post.status = 1
                form.save()
                messages.success(request, 'Update successful!')
                return redirect(reverse('my-page'))
            else:
                messages.error(request, 'Failed to update post. \
                    Please ensure the form is valid.')
        else:
            form = PostForm(instance=post)
    else:
        messages.error(request, 'Sorry. \
                    You are not authorised to perform that operaiton.')

    template = 'edit_logs.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


class DeletePost(generic.DeleteView):
    ''' Class to allow posts to be deleted '''
    model = Post
    template_name = 'delete_logs.html'
    success_url =  '/'
    success_message = "Post was deleted successfully"
    '''
    Display delete message once a post is deleted
    on the homepage blog post list. Solution implemented using
    Stack Overflow answer and amended to work with my project
    '''
    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeletePost, self).delete(request, *args, **kwargs)


class PostLike(View):
    """ To like a lab log post """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('log-details', args=[slug]))


def PostSearch(request):
    q = request.GET['q']

    if 'q' in request.GET:
        results = Post.objects.filter(Q(title__icontains=q)).filter(status=1)

    return render(request, 'search.html', {
        'q': q,
        'results': results
    })
