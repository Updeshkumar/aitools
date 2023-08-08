from django.shortcuts import render
from django.http import HttpResponse
from .models import blog
from django.shortcuts import get_object_or_404, render
# Create your views here.

def index(request):
    context = blog.objects.all()
    return render(request, "index.html", {'context': context})

def product_detail(request, slug):
    context = get_object_or_404(blog, slug=slug)
    return render(request, 'blog/singlepage/single.html', {'context': context})