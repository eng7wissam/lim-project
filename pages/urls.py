from django.urls import path
from . import views

urlpatterns =[
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery_imgs, name='gallery'),
    path('gallerydetail/<int:id>', views.gallery_details, name='gallerydetail'), 
    
    #gallerydetail/
    
    
]
#www.mysite.com/pages/index