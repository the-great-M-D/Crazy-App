from django.shortcuts import *
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . forms import *
from django.contrib.auth.forms import UserCreationForm  
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout 
             
################################## Hacking it ##############################################
 
def register(request):
    if request.user.is_authenticated:
        # also do this for loginPage 
        return redirect('home')
    else: 
        form = CreateUserFormSignal()
        if request.method == 'POST':
            form = CreateUserFormSignal(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            messages.success(request, f'Account Created For {name}')
            return redirect('login')    
        context = {'form':form}
        return render(request, 'users/register.html', context)
    
def updateProfile(request):
    if request.method == 'POST':
        print(f'{request.user}')            
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        messages.success(request, f'Profile Updated You Are ready to login at least i hope so')
        return  redirect('home')
    p_form = ProfileUpdateForm()
    u_form = UserUpdateForm()
    context = {'u_form':u_form,
               'p_form':p_form}
    return render(request, 'users/updateProfile.html', context)      
                
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print(f'i wonder whats in here{user}')
            if user is not None:
                login(request, user)
                print('danko goin to profile page')
                return redirect('updateProfile')
        else:
            messages.info(request, "Username OR Password Incorect ")
        return render(request, 'users/login.html')    

def logoutUser(request):
    logout(request)
    return redirect('login')

    
