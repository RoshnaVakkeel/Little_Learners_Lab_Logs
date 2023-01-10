from . import views
from django.urls import path
from .views import CreatePost, PostDetail, AllPosts, EditPost


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('lab_logs/', AllPosts.as_view(), name='lab-logs'),
    path('log_details/<slug:slug>', PostDetail.as_view(), name='log-details'),
    path('add_logs/', CreatePost.as_view(), name='add-logs'),
    path('edit/<slug:slug>/', EditPost.as_view(), name='edit-logs'),
]
