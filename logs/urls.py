from . import views
from django.urls import path
from .views import PostDetail, AllPosts, PostLike, SharedPostsByUsers, DeletePost  # noqa: E501


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('search/', views.PostSearch, name='search'),
    path('lab_logs/', AllPosts.as_view(), name='lab-logs'),
    path('my_page/', views.SharedPostsByUsers.as_view(), name='my-page'),
    path('log_details/<slug:slug>', PostDetail.as_view(), name='log-details'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post-like'),
    path('add_logs/', views.CreatePost, name='add-logs'),
    path('edit/<slug:slug>/', views.EditPost, name='edit-logs'),
    path('delete/<slug:slug>/', DeletePost.as_view(), name='delete-logs'),
]
