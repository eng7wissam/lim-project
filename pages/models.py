from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=50)

class Banners(models.Model):
    img = models.ImageField(upload_to="banners/")
    alt_text = models.CharField(max_length=150)

    def __str__(self):
        return self.alt_text
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))


class Service(models.Model):
    title = models.CharField(max_length=150)
    details=models.TextField()
    img=models.ImageField(upload_to="services/", null=True)

    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))
    
class Enquiry(models.Model):
    full_name = models.CharField(max_length=150)
    email =models.CharField(max_length=150)
    detail =models.TextField()
    send_time=models.DateTimeField(auto_now_add=True)

    def __set__(self):
        return self.full_name

class gallery(models.Model):
    title = models.CharField(max_length=150)
    details=models.TextField()
    img= models.ImageField(upload_to="services/", null=True)

    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))

class GalleryImage(models.Model):
    gallery = models.ForeignKey(gallery, on_delete=models.CASCADE, null=True)
    alt_text = models.CharField(max_length=150)
    img= models.ImageField(upload_to="gallery_imgs/", null=True)

    def __str__(self):
        return self.alt_text
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))
    
             
    
    