from django import forms
from .models import mainform, get_opportunnity


class RegistryForm(forms.ModelForm):
    class Meta:
        model = get_opportunnity
        fields = ['name','email','website','passport_pic','notes']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = mainform
        fields = '__all__'
        exclude = ('owner','slug',)