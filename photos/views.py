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

def search_category(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'category.html', {"message": message})

def about_me(request):
    return render(request, 'about.html')

def getLocations(request,location):
    locations = Image.filterimageByLocation(location)
    return render(request,'locations.html',{'images':locations})