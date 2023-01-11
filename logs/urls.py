from . import views
from django.urls import path
from .views import CreatePost, PostDetail, AllPosts, EditPost, PostLike


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('lab_logs/', AllPosts.as_view(), name='lab-logs'),
    path('log_details/<slug:slug>', PostDetail.as_view(), name='log-details'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post-like'),
    path('add_logs/', views.CreatePost, name='add-logs'),
    path('edit/<slug:slug>/', views.EditPost, name='edit-logs'),
]
