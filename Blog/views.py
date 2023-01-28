from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
   return render(request, "Blog/index.html")
def posts(request):
    return render(request, "Blog/all-posts.html")