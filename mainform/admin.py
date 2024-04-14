from django.contrib import admin

# Register your models here.

from .models import mainform, type_activity, get_opportunnity

admin.site.register(mainform)
#admin.site.register(Activity_ty)
admin.site.register(type_activity)
admin.site.register(get_opportunnity)
