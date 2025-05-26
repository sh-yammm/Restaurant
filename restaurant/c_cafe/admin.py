from django.contrib import admin

# Register your models here.

from .models import Category, MenuItem, Reservation, Review

admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(Reservation)
admin.site.register(Review)
