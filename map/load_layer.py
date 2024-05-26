import os
from django.contrib.gis.utils import LayerMapping
from .models import Cities_Ly, projects, Regions, Municip

cities_mapping = {
    'region': 'region',
    'latitude': 'latitude',
    'longitude': 'longitude',
    'name_ar': 'name_ar',
    'name_en': 'name_en',
    'region_no': 'Region_No',
    'geom': 'MULTIPOLYGON25D',
}

projects_mapping = {
    'fid': 'fid',
    'project_id': 'Project_id',
    'project_no': 'project_No',
    'project_na': 'project_na',
    'region': 'region',
    'city': 'city',
    'excutive': 'excutive',
    'field': 'field',
    'activity': 'activity',
    'latitude': 'latitude',
    'longitude': 'longitude',
    'geom': 'MULTIPOINT',
}

regions_mapping = {
    'name': 'Name',
    'name_of': 'Name_of',
    'no_of': 'No_Of',
    'type': 'Type',
    'geom': 'MULTIPOLYGON',
}

municip_mapping = {
    'name': 'Name',
    'latitude': 'Latitude',
    'longitude': 'Longitude',
    'geom': 'MULTIPOINT25D',
}

cities_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/Libya_Cities_Polygon.shp'))

projects_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/Libya_Projects_Point.shp'))

region_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/Libya_Regions_Polygon.shp'))

municip_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/Libya_Municip_Polygon.shp'))




def run(verbose=True):
    lm = LayerMapping(Municip, municip_shp, municip_mapping, transform=False, encoding='utf-8') # utf-8 iso-8859-1
    lm.save(strict=True, verbose=verbose)

    #lm = LayerMapping(Regions, region_shp, regions_mapping, transform=False, encoding='utf-8') # utf-8 iso-8859-1
    #lm.save(strict=True, verbose=verbose)


    #lm = LayerMapping(Cities_Ly, cities_shp, cities_mapping, transform=False, encoding='utf-8') # utf-8 iso-8859-1
    #lm.save(strict=True, verbose=verbose)

    #lm = LayerMapping(projects, projects_shp, projects_mapping, transform=False, encoding='utf-8') # utf-8 iso-8859-1
    #lm.save(strict=True, verbose=verbose)


    #lmr = LayerMapping(Regions, regions_shp, regions_mapping, transform=False, encoding='utf-8') # utf-8 iso-8859-1
    #lmr.save(strict=True, verbose=verbose) # 