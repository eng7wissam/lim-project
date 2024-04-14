from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
area = (
    ('Indutry','Indutry'),
    ('Agriculture','Agriculture'),
    ('Tourism','Tourism'),
)

class type_activity(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

def image_upload(instance, filename):
    imagename , extension = filename.split(".")
    return "imgs/%s.%s"%(instance.id,extension)

class mainform(models.Model): # Table
    owner = models.ForeignKey(User, related_name='projcet_owner', on_delete=models.CASCADE)
    project_name = models.CharField(max_length=130) # Column
    area = models.CharField(max_length=25,choices=area)
    location = models.CharField(max_length=26)
    regist_date = models.DateField(auto_now=False)
    description = models.TextField(max_length=200)
    person = models.CharField(max_length=88)
    possition = models.CharField(max_length=50)
    nation = models.CharField(max_length=30)
    passport = models.CharField(max_length=25)
    phone1 = models.CharField(max_length=16)
    phone2 = models.CharField(max_length=16)
    address = models.CharField(max_length=26)
    email = models.EmailField(max_length=25)
    type_activity = models.ForeignKey('type_activity',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True, null=True)

    def save(self,*args, **kwargs):
        self.slug =slugify(self.project_name)# slugify cut spase and putt -
        super(mainform,self).save(*args,**kwargs)


    def __str__(self):
        return self.project_name
    
class get_opportunnity(models.Model):
    project_name = models.ForeignKey(mainform, related_name='get_oppor', on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    email = models.EmailField(max_length=50)
    website = models.URLField()
    passport_pic = models.FileField(upload_to='registred/')
    notes = models.TextField(max_length=200)
    created_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
