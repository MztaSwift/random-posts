from django.urls import path
from .views import fetch_post, success

urlpatterns = [
    path('', fetch_post, name='fetch_post'),
    path('success/', success, name='success'),
]
