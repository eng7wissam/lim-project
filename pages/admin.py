from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.login)

class BannerAdmin(admin.ModelAdmin):
    list_display=('alt_text', 'image_tag')

admin.site.register(models.Banners,BannerAdmin) #

class ServiceAdmin(admin.ModelAdmin):
    list_display=('title', 'image_tag')

admin.site.register(models.Service,ServiceAdmin) #


class GalleryAdmin(admin.ModelAdmin):
    list_display=['title', 'image_tag']    

admin.site.register(models.gallery,GalleryAdmin) #

class GalleryImageAdmin(admin.ModelAdmin):
    list_display=('alt_text', 'image_tag')

admin.site.register(models.GalleryImage,GalleryImageAdmin) #
