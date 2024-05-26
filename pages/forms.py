from django import forms
from .models import login

# Create your models here.

class LoginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = '__all__' # ['user','password']

#     username = forms.CharField(max_length=40, label='User Login', initial='Enter User Name')
# max_length=40, disabled=False / help_text='Enter User Name'
# label='User Login', initial='Enter User Name'
'''
class LoginForm(forms.Form):
    username = forms.CharField(max_length=40, disabled=False, required=True)
    password = forms.CharField(max_length=50,widget=forms.PasswordInput)
'''
