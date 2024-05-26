from django.conf.urls import include
from django.urls import path
#from geojson import GeoJSONLayerView
from .views import HomePageView, city_dataset, project_dataset, forms_all , viewmap, rgn_dataset, viewAllmap, registry_app, approve,home , mp_index, map_index, prj_index, project_view, project_search_view, projects, applicants, homepage, createInvestor, updateInvestor, deleteInvestor


urlpatterns = [
    path('', homepage, name='homepage'), #homepage/
    path('home', HomePageView, name='home'), #''
    path('rgstry/', registry_app, name='regist_form'),
    path('cities_data/', city_dataset, name='city'),  #cities_data/
    path('mapds/', rgn_dataset, name='regns'), #<int:id>
    path('approve/', approve, name='approve_form'),

    #path('', viewAllmap, name='viewall'), #''       
    path('maphome/', home, name='maphome'),
    #path('rgns_data/<int:id>', rgn_dataset, name='regns'), # rgns_data/

    path('projects_data/', project_dataset, name='projects_data'),
   #path('region_data/', HomePageView, name='region'),
    path('rgn/', forms_all, name='region'),
    path('mapd/<int:id>', viewmap, name='regions_details'), 

    path('allRegion', viewAllmap, name='allRegion'),
    path('viewMap/<int:id>', viewmap, name='viewMap'), #''
    path('map/', mp_index, name='map'),
    path('mapin/', map_index, name='mapin'),
    path('prjmap/', prj_index, name='prjmap'),
    path('prj/', project_search_view, name='prj'),
    path('prj/<int:id>/', project_view, name='prj'),
    path('prjall/', projects, name='prjall'),
    path('applicants/', applicants, name='applicants'),
    path('create_investor/', createInvestor, name='create_investor'),
    path('update_investor/<str:pk>/', updateInvestor, name='update_investor'),
    path('delete_investor/<str:pk>/', deleteInvestor, name='delete_investor'),

]
