from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('allposts', views.posts, name="posts"),
   path('allposts/<str:slug>/', views.post_detail, name="post-detail")

]
