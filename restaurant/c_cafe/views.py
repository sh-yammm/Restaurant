from django.shortcuts import render,redirect

# Create your views here.

from django.views import View

class HomeView(View):
    
    def get(self, request,*args,**kwargs):

        data = {'page':'home-page'}

        return render(request, 'c_cafe/base.html', context=data)
    
class AboutView(View):
    
    def get(self, request,*args,**kwargs):

        data = {'page':'about-page'}

        return render(request, 'c_cafe/about.html', context=data)
    
class MenuView(View):
    
    def get(self, request,*args,**kwargs):

        data = {'page':'menu-page'}

        return render(request, 'c_cafe/menu.html', context=data)
    
class EvenView(View):
    
    def get(self, request,*args,**kwargs):

        data = {'page':'event-page'}

        return render(request, 'c_cafe/event.html', context=data)
    
class ChefView(View):
    
    def get(self, request,*args,**kwargs):

        data = {'page':'chef-page'}

        return render(request, 'c_cafe/chef.html', context=data)
    
