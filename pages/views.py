from django.shortcuts import render
import folium.map
from . import  models
from .forms import LoginForm
from django.urls import reverse
import folium
#from django.http import HttpResponse

# Create your views here.

def index(request):
    #m = folium.map()
    #m = m._repr_html_()
    context = {
        'name':'Indx : Wessam M Alhadi Ramadan','age':65}
    return render(request, 'index.html',context)
   # return HttpResponse('Hello Brother')

def about(request):    
    dataform = LoginForm(request.POST)
    if dataform.is_valid():
        dataform.save()
        #context = {'name':'About :Ali Omar Abd Alsalam','age':44}
    return render(request, 'about.html',{'lg_frm':LoginForm})


def gallery_imgs(request):     
    all_gallerys =models.gallery.objects.all().order_by('id')  
    context ={'glry':all_gallerys}
    return render(request, 'gallery.html', context)

def gallery_details(request, id):     
    gallery =models.gallery.objects.get(id=id)
    gallery_imgs_details=models.GalleryImage.objects.filter(gallery=gallery).order_by('-id')
    context ={'gallery_imgs_details':gallery_imgs_details, 'gallery':gallery}
    return render(request, 'gallery_img.html', context)



'''
        dataform = LoginForm(request.POST)
    dataform.save()

    user_name = request.POST.get('username')
    pass_word = request.POST.get('password')
    data = login(username=user_name, password=pass_word)
    data.save()


context ={'allfrm':page_obj} # Template Name #forms_all
return render(request,'form_all.html',context)
'''