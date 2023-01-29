from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Author,Tag
# Create your views here.


def index(request):
   return render(request, "Blog/index.html")
def posts(request):
   latest_posts =  Post.objects.all().order_by("-date")[:3]

   return render(request, "Blog/all-posts.html", {
      "posts" : latest_posts
    })