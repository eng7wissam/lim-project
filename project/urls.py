"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from app.views import indx
from map import views as map_view



urlpatterns = [
    path('', include('map.urls')), #map/
    path('pages/', include('pages.urls')), #,namespace='about'  pages/
    path('regist/', indx, name='regist'),
    #path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('mainform/', include('mainform.urls',namespace='frmu')),
    path('products/', include('products.urls')),

    #path('map/', map_view.mp_index, name='map'),

    #path('default/', include('app.urls')),
    
]
#www.mysite.com/'' will open main root
#www.mysite.com/pages will open pages

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

               