from . import views
from django.urls import path
from .views import CreatePost, PostDetail


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_logs/', CreatePost.as_view(), name='add-logs'),
    path('log_details/<slug:slug>', PostDetail.as_view(), name='log-details'),
]
