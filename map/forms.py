from django import forms
from datetime import datetime

from django.urls import reverse_lazy
from .models import Search, Regions, Applicants, Municip, Locations, Projects, Investors
from django.contrib.gis.db import models as gis_models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# lable, initial, disable , help_text,
# widget=forms.PasswordInput, required

class SearchForm(forms.ModelForm):
    address = forms.CharField(label='')
    class Meta:
        model = Search
        fields = ['address', ]

class ApplicantForm(forms.ModelForm):
        class Meta:
            model = Applicants
            fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['region'].queryset = Regions.objects.all()

            if 'region' in self.data:
                             self.fields['region'].queryset = Regions.objects.all()


class rgstForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('approve_form')
        self.helper.form_method='GET'
        self.helper.add_input(Submit('submit', 'Submit'))

    Executive_type=(
        (1,'تحت التاسيس'),
        (2,'تحت التنفيذ'),
        (3,'دخلت التشغيل'),
    )
    name = forms.CharField(widget=forms.TextInput(attrs={
             'hx-get': reverse_lazy('approve_form'), 'hx-trigger': 'keyup'
        }))
    executive = forms.ChoiceField(
        choices=Executive_type, widget=forms.RadioSelect()
    )
    #regist_date = forms.DateField(widget=forms.DateInput(format = '%d-%m-%Y' ,attrs={'type':'date', 'max':datetime.today()}))

    date_of_birth = forms.DateField(localize=True,widget=forms.DateInput(format = '%Y-%mm-%dd',attrs={'type': 'date'}))
    
    #issue_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=settings.DATE_INPUT_FORMATS)


class RegionForm(forms.ModelForm):
        #name = forms.CharField(max_length=40)
        #name_of = forms.CharField(max_length=40)
        #no_of = forms.IntegerField()
        #type = forms.CharField(max_length=30, label='المنطقة') #, initial='Enter Name here'   widget=forms.Textarea(attrs={'style': "width:100%;"}), 
        #geom = gis_models.MultiPolygonField(srid=4326)
        class Meta:
            model = Regions
            fields = '__all__' #['name','type','no_of','geom']

class MunicipForm(forms.ModelForm):
      name =forms.CharField(label='')
      class Meta:
            model = Municip
            fields = ['name', ]

class LocationsForm(forms.ModelForm):
      class Meta:
            model= Locations
            fields = ['proj_name', ]

class ProjectsForm(forms.ModelForm):
      class Meta:
            model= Projects
            fields = ['proj_name', ]

class InvestorForm(forms.ModelForm):
      class Meta:
            model= Investors
            fields = '__all__' 

