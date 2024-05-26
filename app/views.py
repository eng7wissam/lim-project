from django.shortcuts import render
from .models import application

# Create your views here.
def indx(request):
    obj = application.objects.all()
    context={
        'obj':obj,
    }
    return render(request, 'regist.html',context)
