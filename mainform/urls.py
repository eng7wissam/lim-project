from django.urls import path, include
from . import views

app_name='mainform'

urlpatterns = [
    path('', views.forms_all, name='allfrm'),
    path('add', views.add_project, name='add_project'),
    path('<int:id>', views.form_detail, name='frm_detail'),
]
