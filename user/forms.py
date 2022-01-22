from django import forms
from PIL import Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import  Profile

 ################################## Trying With Signals !##############################################
class CreateUserFormSignal(UserCreationForm):
    #do the email thing here
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mugshot','description','phone_number','address',]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name',]

