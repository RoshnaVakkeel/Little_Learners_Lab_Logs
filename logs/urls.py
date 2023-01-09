from . import views
from django.urls import path
from .views import CreatePost, PostDetail, AllPosts


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('lab_logs/', AllPosts.as_view(), name='lab-logs'),
    path('log_details/<slug:slug>', PostDetail.as_view(), name='log-details'),
    path('add_logs/', CreatePost.as_view(), name='add-logs'),
]
