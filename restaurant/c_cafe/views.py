from django.shortcuts import render,redirect
from django.views import View
from .models import MenuItem,Review, Event, GalleryImage, Chef

# Create your views here.


class HomeView(View):
    
    def get(self, request,*args,**kwargs):

        items = MenuItem.objects.filter(is_available=True)

        events = Event.objects.all()

        gallery = GalleryImage.objects.all()

        chefs = Chef.objects.all()

        reviews = Review.objects.all()

        return render(request, 'c_cafe/home.html', 
                      {'items': items,
                       'events': events,
                       'gallery': gallery,
                       'chefs': chefs,
                       'reviews': reviews})

    