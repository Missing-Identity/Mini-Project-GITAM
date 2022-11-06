from django.urls import path, include
from django.contrib import admin

from health_app import views

urlpatterns = [
    path('', views.post_list_view, name='post_list'),
    path('new/', views.CreatePostView.as_view(), name='post_form'),
]