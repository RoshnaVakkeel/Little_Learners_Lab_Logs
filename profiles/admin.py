# Register Profile with the backend admin site
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
