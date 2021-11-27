from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Image, Category, Location

# Create your views here.

def home(request):
    images = Image.images()
    locations = Location.objects.all()
    return render(request, 'index.html', {'images':images,'locations':locations})

def gallery(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    location = Location.objects.all()
    return render(request, 'gallery.html', locals())

