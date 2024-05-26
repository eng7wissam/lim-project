from django.contrib import admin

# Register your models here.

from .models import mainform, type_activity, get_opportunnity

class mainformAdmin(admin.ModelAdmin):
    list_display = ['project_name','area','location','address','phone1','possition','image']
    list_display_links = ['location','address']
    list_editable = ['phone1','possition']
    search_fields = ['project_name']
    list_filter = ['type_activity', 'location']
    #fields = ['project_name','area','location'] # fields do you wont to display
    

admin.site.register(mainform, mainformAdmin)

#admin.site.register(Activity_ty)
admin.site.register(type_activity)
admin.site.register(get_opportunnity)
