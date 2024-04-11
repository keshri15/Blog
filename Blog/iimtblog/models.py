from django.db import models
# from django.utils.timezone import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class ContactTb(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        
        return f"{self.name} - {self.email}"
    
    
   
class Popular_Blog(models.Model):
    
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    content=RichTextField()
    post_date=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='image',default="")


class Regular_Blog(models.Model):
    
    title = models.CharField(max_length=122)
    author = models.CharField(max_length=50)
    content = RichTextField()
    post_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='image',default="")    