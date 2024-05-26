from django.contrib import admin
from .models import House, Search, Incidences ,Cities_Ly ,Locations, Regions ,Municip, Applicants, type_activity, Area,Investors, Projects
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from django.db import models
from django.contrib.gis.db import models as gis_models
from mapwidgets.widgets import GooglePointFieldWidget


'''
admin.site.register(
    Incidences,                      #<-- this is a model
    LeafletGeoAdmin, 
    settings_overrides =  {
      #  'DEFAULT_CENTER': (59.334591, 18.063240),
       # 'DEFAULT_ZOOM': 10,
       # 'TILES': [('','//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png','')],
    }
)
'''
# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin): #admin.ModelAdmin
    #pass
    list_display =('name','location')
admin.site.register(Incidences, IncidencesAdmin)

class CitiesAdmin(LeafletGeoAdmin):
    list_display =('name_ar','region_no')

admin.site.register(Cities_Ly, CitiesAdmin)

class LocationsAdmin(LeafletGeoAdmin):
    list_display =('proj_name', 'city','field','area','geom')
    list_editable = ['area']
    search_fields = ['proj_name']
    list_filter = ['area', 'region']


admin.site.register(Locations, LocationsAdmin)

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        gis_models.PointField: {"widget":GooglePointFieldWidget}
    }
#admin.site.register(House, HouseAdmin)



class RegionsAdmin(LeafletGeoAdmin):
    list_display =('name','name_of')

admin.site.register(Regions, RegionsAdmin)

class MunicipAdmin(LeafletGeoAdmin):
    list_display =('name',)

admin.site.register(Municip, MunicipAdmin)

class appformAdmin(admin.ModelAdmin):
    pass
    list_display = ['proj_name','proj_no' ,'area','region','city' ,'location','regist_date','proj_id']
    list_display_links = ['proj_no']
    list_editable = ['region','area','location']
    search_fields = ['proj_name']
    list_filter = ['area', 'region']
    exclude = ['proj_id']
    #fields = ['project_name','area','location'] # fields do you wont to display
    

admin.site.register(Projects, appformAdmin)

admin.site.register(Area)
admin.site.register(type_activity)
admin.site.register(Search)

class ApplicantsformAdmin(admin.ModelAdmin):
    pass
    list_display = ['person','possition','nation','email','address','phone1']
    list_display_links = ['email','address']
    list_editable = ['phone1','possition']
    search_fields = ['person']
    list_filter = ['phone1', 'address']

admin.site.register(Applicants , ApplicantsformAdmin)

admin.site.register(Investors)




#class RegionsAdmin(LeafletGeoAdmin):
 #   list_display=('name','name_of')


#admin.site.register(Regions, RegionsAdmin)


