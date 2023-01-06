from . import views
from django.urls import path
from .views import CreatePost


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_logs/', CreatePost.as_view(), name='add-logs'),
]
