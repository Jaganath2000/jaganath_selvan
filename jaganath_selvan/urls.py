# jaganath_selvan/urls.py
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ContactMe.urls')),  # Include ContactMe app's URLs
]
