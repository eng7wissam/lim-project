from django.shortcuts import render, redirect
import folium.map
from .models import Search  ,Municip, Cities_Ly, Locations, Regions, Investors, Applicants, Projects
from .forms import SearchForm, RegionForm, Applicants, rgstForm, MunicipForm, InvestorForm
import folium, geocoder
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from folium.plugins import FastMarkerCluster
from django.db.models import Avg

# Create your views here.
#class HomePageView(TemplateView):
#    template_name = 'index.html'

def HomePageView(request):
    context = {}
     #   'name':'Indx : Wessam M Alhadi Ramadan','age':65}
    return render(request, 'index.html',context)

def city_dataset(request):
    cities  = serialize('geojson', Cities_Ly.objects.all())
    return HttpResponse(cities, content_type='json')

def project_dataset(request):
    project  = serialize('geojson', Locations.objects.all())
    return HttpResponse(project, content_type='json')

def home(request):
    context = {'project': list(Locations.objects.values('id','latitude','longitude'))}
    return render(request, 'home.html', context)

def cities_position(request):
    return JsonResponse({'cities_ly': list(Cities_Ly.objects.values('latitude','longitude'))}
    )

def map_index(request):
    #address = Municip.objects.all()
    location = geocoder.osm('paris')
    lat = location.lat
    lng = location.lng
    country = location.country
    m = folium.Map(location=[32.738194, 12.731634], zoom_start=6)
    folium.Marker([32.738194, 12.731634], tooltip='Click For More', popup='Zawia').add_to(m)

    #folium.Marker([lat, lng], tooltip='Click For More', popup=country).add_to(m)
    m = m._repr_html_()
    context ={'map': m,}
    return render(request, 'mp_index.html', context)


def mp2_index(request):
    if request.method == 'POST':
        form = MunicipForm(request.POST) # SearchForm
        if form.is_valid():
            form.save()
            return redirect('map')
    else:
        form = MunicipForm()
    address = Municip.objects.all()
    #address = request.POST.get('address')
    location = geocoder.osm(address) #'paris' 
    lat = location.Lat
    lng = location.Lng
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('You address input is invild')
    m = folium.Map(location=[32.738194, 12.731634], zoom_start=6)
    folium.Marker([lat, lng], tooltip='Click For More', popup=country).add_to(m)
    #folium.Marker([32.738194, 12.731634], tooltip='Click For More', popup='Alzawia').add_to(m)
    m = m._repr_html_()
    context = {
        'map':m,
        'form':form,
    }
    return render(request, 'mp_index.html', context)  #mp_index.html  map_view.html

def mp_index(request):
    #avg_lat = Municip.objects.aggregate(avg=Avg('latitude'))['avg']
    #stations = Municip.objects.filter(latitude__gt=avg_lat)

    #stations = Municip.objects.all()
    stations = Locations.objects.all()
    m = folium.Map(location=[26.133567, 17.549336], zoom_start=5) # 32.738194, 12.731634
    latitudes = [station.latitude for station in stations]
    longitudes =[station.longitude for station in stations]
    FastMarkerCluster(data=list(zip(latitudes, longitudes))).add_to(m)
    #folium.Marker(popup=station.)
    context = {'map': m._repr_html_()}
    return render(request, 'indexmap.html', context)

def prj_index(request):
    #avg_lat = Municip.objects.aggregate(avg=Avg('latitude'))['avg']
    #stations = Municip.objects.filter(latitude__gt=avg_lat)
    stations = Locations.objects.all()
    m = folium.Map(location=[32.738194, 12.731634], zoom_start=6)
    latitudes = [station.latitude for station in stations]
    longitudes =[station.longitude for station in stations]
    FastMarkerCluster(data=list(zip(latitudes, longitudes))).add_to(m)
    #folium.Marker(popup=station.)
    context = {'map': m._repr_html_()}
    return render(request, 'indexmap.html', context)

def homepage(request):
    applicant = Applicants.objects.all()
    project = Projects.objects.all()
    investor = Investors.objects.all()
    stations = Locations.objects.all()
    total_project = stations.count()
    total_applicant = applicant.count()
    total_investors = investor.count()


    region1 = stations.filter(region_id=1).count()
    region2 = stations.filter(region_id=2).count()
    region3 = stations.filter(region_id=3).count()
    region4 = stations.filter(region_id=4).count()

    area1 = stations.filter(area_id=8).count()
    area2 = stations.filter(area_id=9).count()
    area3 = stations.filter(area_id=10).count()
    area4 = stations.filter(area_id=11).count()
    area5 = stations.filter(area_id=12).count()
    area6 = stations.filter(area_id=13).count()
    area7 = stations.filter(area_id=14).count()
    area8 = stations.filter(area_id=15).count()
    area9 = stations.filter(area_id=16).count()

    area_list =['Industry','Tourism','Health','Education','Services','Real Estate','Transportation','Elictricity & Energy','Transformative']
    number_list = [area1,area2,area3,area4,area5,area6,area7,area8,area9]


    #stations = Municip.objects.all()
    
    m = folium.Map(location=[26.133567, 17.549336], zoom_start=4) # 32.738194, 12.731634
    latitudes = [station.latitude for station in stations]
    longitudes =[station.longitude for station in stations]
    FastMarkerCluster(data=list(zip(latitudes, longitudes))).add_to(m)
    #folium.Marker(popup=station.)

    regn_list = ['Eastern', 'Western', 'Central', 'Southern']
    regn_number = [region1,region2,region3,region4]


    context ={'map': m._repr_html_(), 'projects': project, 'investors':investor,'applicants':applicant,'total_proj':total_project, 'total_app':total_applicant, 'region1':region1, 'region2':region2, 'region3':region3, 'region4':region4,'area1':area1,'area1':area2,'area2':area2,'area3':area3,'area4':area4 ,'area5':area5, 'area6':area6,'area7':area7,'area8':area8,'area9':area9,'total_investors':total_investors,'area_list':area_list, 'number_list':number_list, 'regn_list':regn_list, 'regn_number':regn_number}
    return render(request, 'mainpage.html', context) # dashboard.html


def projects(request):
    project = Locations.objects.all()
    return render(request, 'projects_all.html', {'projects': project})

def applicants(request):
    labels =[]
    data = []
    applicant = Applicants.objects.all()
    #project = Locations.objects.all()
    project = Projects.objects.all()  #.order_by('id')
    project2 = Projects.objects.all().order_by('-id')[:10]
    investor = Investors.objects.all()
    total_project = project.count()
    total_applicant = applicant.count()
    total_investors = investor.count()


    region1 = project.filter(region=1).count()
    region2 = project.filter(region=2).count()
    region3 = project.filter(region=3).count()
    region4 = project.filter(region=4).count()

    proj = Investors.objects.order_by('-invest_cost')[:5]
    for rgn in proj:
        labels.append(rgn.name)
        data.append(rgn.invest_cost)


    context ={'projects': project2, 'investors':investor,'applicants':applicant,'total_proj':total_project, 'total_app':total_applicant, 'region1':region1, 'region2':region2, 'region3':region3, 'region4':region4, 'total_investors':total_investors, 'labels': labels, 'data': data}
    return render(request, 'applicants.html', context)

def investor(request):
    pass
    #project = Investors.objects.all()
    #return render(request, 'applicants.html', {'projects': project})


def project_search_view(request):
    #print(dir(request))
    print(request.GET)
    query_dict = request.GET # this is dictionary
    #query = query_dict.get("q") # <input type="text" name="q" />
    try:
        query = int(query_dict.get("q"))
    except:
        query = None
    project_obj = None
    if query is not None:
        project_obj = Projects.objects.get(id=query)
        #project  = serialize('geojson', projects.objects.get(id=query))

    context = {
        "object": project_obj,
       #"projects": project,
    }
    return render(request, 'search.html', context=context)

def project_view(request, id):
    project = Projects.objects.get(id=id)
    investor = project.investors.all()
    applicant = project.applicants.all()

    investor_count = investor.count()

    context= {'prjcts': project, 'applicants': applicant, 'investors':investor ,'total_investors': investor_count}
    return render(request, "project_detail.html", context)

def project_view2(request, id):
    project_obj = None
    if id is not None:
        project = Projects.objects.get(id=id)

        investor = project.investors.all()
        applicant = project.applicants.all()

        #projects_count = project.count()
    context= {'projects': project_obj, 'applicants': applicant, 'investors':investor }
    return render(request, "project_detail.html", context)


def forms_all(request):
    all_regions =Regions.objects.all().order_by('id')  
    #page_obj = request.GET.get('page')
    context ={'region':all_regions}
    return render(request, 'map_all.html', context)

def form_detail(request, id):
    regions =Regions.objects.get(id=id)
    regions_details=Regions.objects.filter(id=id).order_by('-id')
    context ={'regions_details':regions_details, 'regions':regions}
    return render(request, 'map_detail.html', context)

def map_details(request, id):
    regions =serialize('geojson', Regions.objects.get(id=id))
    regions_details=Regions.objects.filter(id=id)#.order_by('-id')
    context ={'regions_details':regions_details, 'regions':regions}
    return render(request, 'map_details.html', context)

def viewAllmap(request):
        forms_all = Regions.objects.all()
        if request.method =='POST':
           dataform = RegionForm(request.POST)
           if dataform.is_valid():
               dataform.save()
        else:
           dataform = RegionForm()
        context = {'allRegion': dataform}  # , 'form_rgst':dataform
        return render(request,'map_details.html', context)
       #rgn_loc = Regions.objects.values_list('geom', flat=True).get(pk=req[id])


def viewmap(request, id):
    #form_detail =serialize('geojson', Regions.objects.get(id=id))
    form_detail = Regions.objects.get(id=id)
    if request.method=='POST':
        form = RegionForm(request.POST) #, request.FILES
        if form.is_valid():
            myform = form.save(commit=False)
            myform.type = form_detail
            myform.save()
    else:
        form = RegionForm() 
    context = {'viewMap': form_detail,'form_rgst':form}
    return render(request,'map_details.html',context)

def rgn_dataset(request, pk):
    cities  = serialize('geojson', Regions.objects.all())
    #form = RegionForm(request.POST, request.FILES)
    #json_loc = form.geom #newJob.objects.filter(pk=req['search'])
    region =serialize('geojson', Regions.objects.get(id=pk))

    #region  = serialize('geojson', Regions.objects.all())
    #region  = serialize('geojson', Regions.objects.all())
    #return JsonResponse({'geojson': list(Regions.objects.values('id'))})

    return HttpResponse(region, content_type='json')

def viewjob(request):
        req = request.GET
        rgn_name = Regions.objects.values_list('name', flat=True).get(pk=req['search'])
        rgn_er = Regions.objects.values_list('type', flat=True).get(pk=req['search'])
        rgn_loc = Regions.objects.values_list('geom', flat=True).get(pk=req['search'])

        json_loc = Regions.objects.filter(pk=req['search'])
        json_loc = serialize('geojson', json_loc, geometry_field='geom')
        context = {
        'name': rgn_name,
        'type': rgn_er,
        'geom': rgn_loc,
        'json_loc': json_loc
        }

        print(context)

        return render(request,'map_details.html', context)

def registry_app(request):
    form = Applicants()
    #if request.is_ajax():
     #   term = request.GET.get('term')
      #  region = Regions.objects.all().filter(name_icontains=term)
       # respose_content = list(region.values())
        #return JsonResponse(respose_content, self=False)
    if request.method =='POST':
        form = Applicants(request.POST)
        if form.is_valid():
            #myform = form.save(commit=False)
           # myform.project_name = form_detail
            form.save()
            return redirect('regist_form')
    context ={'form': form} #, 'form_rgst':form
    return render(request,'registry.html',context)

def approve(request):
    context = {'form_approve': rgstForm()}
    return render(request, 'approve.html', context)

def createInvestor(request):
    form = InvestorForm()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = InvestorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request, 'investor_form.html', context)

def updateInvestor(request, pk):
    investor = Investors.objects.get(id=pk)
    form = InvestorForm(instance=investor)

    if request.method == 'POST':
        form = InvestorForm(request.POST, instance=investor)
        if form.is_valid():
            form.save()
            return redirect('/homepage/')

    context ={'form':form}
    return render(request, 'investor_form.html', context)

def deleteInvestor(request, pk):
    investor = Investors.objects.get(id=pk)
    if request.method == 'POST':
        investor.delete()
        return redirect('/homepage/')
    context ={'item': investor}
    return render(request, 'delete.html', context)



    #cities  = serialize('geojson', Cities_Ly.objects.all())
    #return HttpResponse(cities, content_type='json')

    #context = {'cities_ly': list(Regions.objects.values('id','latitude','longitude'))}
    #return render(request, 'map_details.html', context)


