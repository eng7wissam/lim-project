from django.db import models

class Product(models.Model):
    prod_list = [
        ('Phone','Phone'),
        ('Computer','Computer'),
    ]
    name = models.CharField(max_length=60, verbose_name='الاسم:')
    details = models.TextField(null=True, blank=True) #(null=True, blank=True)
    price =models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to=('photo/%y/%m/%d'))#'photo/%y/%m/%d', default='photo/20/10/11'
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50, null=True, blank=True,choices=prod_list)
    def __str__(self) -> str:
        return self.name # self.price
    
    class Meta:
        verbose_name = 'MyProduct'
        ordering = ['-name']