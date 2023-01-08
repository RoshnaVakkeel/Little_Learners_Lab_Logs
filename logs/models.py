from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Model for lab log posts
    """

    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="log_posts",
        blank=True,
        null=True
    )
    description = models.TextField()
    items_required = models.TextField()
    steps_to_perform = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(null=True, unique=True)
    likes = models.ManyToManyField(
        User,
        related_name='post_like',
        blank=True
        )

    class Meta:
        """
        To arrange the post on the created_on field in the decending order
        """
        ordering = ["-created_on"]

    def __str__(self):
        """
        To return a string representation of an object
        """
        return self.title

    def number_of_likes(self):
        """
        To return the total number of likes on a post
        """
        return self.likes.count()


class Comment(models.Model):
    """
    Model for Comment
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="user_comments",
        blank=True,
        null=True)
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        To order the comments on the created_on field in the ascending order
        """
        ordering = ['created_on']

    def __str__(self):
        """
        To return a string of the comment made by the user
        """
        return f"Comment {self.body} by {self.name}"
