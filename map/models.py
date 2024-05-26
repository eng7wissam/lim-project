from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

#from django.contrib.gis import gdal
#from django.db.models import Manager as GeoManager
#from django.db.models.manager import Manager
#from django.contrib.gis.gdal.libgdal import lgdal
# Create your models here.

class House(models.Model):
    name = models.CharField(max_length=44)
    location = gis_models.PointField(srid=4326)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='Houses'

def image_upload(instance, filename):
    imagename , extension = filename.split(".")
    return "imgs/%s.%s"%(instance.id,extension)

class Area(models.Model):
    area = models.CharField(max_length=25)

    def __str__(self):
        return self.area


class type_activity(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    
class Regions(models.Model):
    name = models.CharField(max_length=40)
    name_of = models.CharField(max_length=40)
    no_of = models.IntegerField()
    type = models.CharField(max_length=30)
    geom = gis_models.MultiPolygonField(srid=4326)
    
    def __str__(self):
        return self.name

class Cities_Ly(models.Model):
    name_ar = models.CharField(max_length=85)
    name_en = models.CharField(max_length=47)
    region_name = models.CharField(max_length=43)
    latitude = models.FloatField()
    longitude = models.FloatField()
    region_no = models.IntegerField()
    region = models.ForeignKey(Regions,on_delete=models.CASCADE, null=True)
    geom = gis_models.MultiPolygonField(srid=4326)
    def __unicode__(self):
        return self.geom

    
class Municip(models.Model):
    name = models.CharField(max_length=254)
    region = models.ForeignKey(Regions,on_delete=models.CASCADE, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField() 
    geom = gis_models.MultiPointField(srid=4326)
    objects =gis_models.Manager()
    def __str__(self):
        #return (self.latitude, self.longitude)
       return self.name


class Projects(models.Model):
    proj_name = models.CharField(max_length=254)
    proj_no = models.PositiveIntegerField()
    region = models.ForeignKey(Regions,on_delete=models.CASCADE, verbose_name='ادخل المنطقة')
    city = models.CharField(max_length=254)
    location = models.ForeignKey(Municip,on_delete=models.CASCADE) 
    area = models.ForeignKey(Area,on_delete=models.CASCADE, verbose_name='ادخل المجال')
    type_activity = models.ForeignKey(type_activity,on_delete=models.CASCADE, null=True)
    regist_date = models.DateField(auto_now=False, null=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    proj_id = models.CharField(max_length=25, default=0)


    def save(self, *args , **kwargs):        
         #+ str(self.regist_date.year)
        self.proj_id= str(self.region.id) + str(self.area.id) + str(self.proj_no) #+ str(self.ID) 
        super().save(*args , **kwargs)

    def __str__(self):
        return self.proj_name

class Applicants(models.Model): # Table
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='applicants')
    owner = models.ForeignKey(User, related_name='app_owner', on_delete=models.CASCADE)
    person = models.CharField(max_length=88)
    possition = models.CharField(max_length=50)
    nation = models.CharField(max_length=30)
    passport = models.CharField(max_length=25)
    phone1 = models.CharField(max_length=16)
    phone2 = models.CharField(max_length=16)
    address = models.CharField(max_length=26)
    email = models.EmailField(max_length=25)
    regist_date = models.DateField(auto_now=False)


    def __str__(self):
        return self.person
    
class Investors(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='investors')
    name = models.CharField(max_length=30)
    nation = models.CharField(max_length=30)
    type_currency = models.CharField(max_length=25)
    phone = models.CharField(max_length=16)
    email = models.EmailField(max_length=25)
    percent =models.DecimalField(max_digits=5, decimal_places=2)
    invest_cost =models.FloatField() 
    #proj_id = models.ForeignKey(Projects.proj_id, on_delete=models.CASCADE)


    def __str__(self):
        return self.name    


class Locations(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True,related_name='locations')
    proj_no = models.FloatField()
    proj_name = models.CharField(max_length=254)
    region = models.ForeignKey(Regions,on_delete=models.CASCADE, null=True, verbose_name='ادخل المنطقة')
    #location = models.ForeignKey(Municip,on_delete=models.CASCADE, null=True) 
    city = models.CharField(max_length=75, null=True)
    area = models.ForeignKey(Area,on_delete=models.CASCADE, null=True)
    field = models.CharField(max_length=36, null=True)
    regist_date = models.DateField(auto_now=True, null=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=True, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True) 
    geom = gis_models.MultiPointField(srid=4326, null=True)
    objects =gis_models.Manager()

    def __unicode__(self):
        return self.proj_name
    

class Incidences(models.Model):
    name = models.CharField(max_length=30)
    #location = models.CharField(max_length=30)
    location = gis_models.PointField(srid=4326) # stid=2453 null=True
    objects =gis_models.Manager()
    #objects = GeoManager()
    def __unicode__(self):
        return self.name    
    class Meta:
        verbose_name_plural = 'Incidences'

class Search(models.Model):
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address
