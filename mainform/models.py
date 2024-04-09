from django.db import models

# Create your models here.
area = (
    ('Indutry','Indutry'),
    ('Agriculture','Agriculture'),
    ('Tourism','Tourism'),
)
class mainform(models.Model): # Table
    project_name = models.CharField(max_length=130) # Column
    area = models.CharField(max_length=25,choices=area)
    regist_date = models.DateField(auto_now=False)
    person = models.CharField(max_length=88)
    possition = models.CharField(max_length=50)
    nation = models.CharField(max_length=30)
    passport = models.CharField(max_length=25)
    phone1 = models.CharField(max_length=16)
    phone2 = models.CharField(max_length=16)
    email = models.EmailField(max_length=25)

    def __str__(self):
        return self.project_name
