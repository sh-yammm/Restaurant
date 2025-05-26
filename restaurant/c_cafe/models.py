from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True) 


    def __str__(self):
        return self.name

class Reservation(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField('+91',max_length=10)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"

class Review(models.Model):

    customer_name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Event(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title or f"Image {self.id}"

class Chef(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, help_text="e.g., Head Chef, Pastry Chef")
    bio = models.TextField()
    photo = models.ImageField(upload_to='chefs/', blank=True, null=True)

    def __str__(self):
        return self.name
