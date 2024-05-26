from django.shortcuts import redirect, render
from .models import mainform
from django.core.paginator import Paginator
from .form import RegistryForm, ProjectForm
from django.urls import reverse

# Create your views here.

def forms_all(request):
    forms_all = mainform.objects.all()
    paginator = Paginator(forms_all, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context ={'allfrm':page_obj} # Template Name #forms_all
    return render(request,'form_all.html',context)


def form_detail(request, id):
    form_detail = mainform.objects.get(id=id)
    if request.method=='POST':
        form = RegistryForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.project_name = form_detail
            myform.save()
    else:
        form = RegistryForm()    
    context = {'frm':form_detail,'form_rgst':form}
    return render(request,'form_detail.html',context)

def add_project(request):
    if request.method=='POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('frmu:allfrm'))
    else:
        form = ProjectForm()
    return render(request,'add_project.html',{'form_r':form})
    

