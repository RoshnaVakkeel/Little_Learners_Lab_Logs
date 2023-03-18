from . import views
from django.urls import path

urlpatterns = [
    path('edit-profile/', views.ProfileAccount.as_view(), name='edit_profile'),
    path('user-delete/', views.UserDelete.as_view(), name='user_delete'),
    path('update-profile/', views.UpdateProfile.as_view(),
         name='update_profile'),
]
