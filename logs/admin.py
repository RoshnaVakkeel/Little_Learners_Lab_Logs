from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    # Admin page functionality for posts
    list_display = ('title', 'slug', 'status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('items_required', 'steps_to_perform')
    list_filter = ('created_on', 'status')
    search_fields = ['title', 'items_required', ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Comments display on admin site
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
