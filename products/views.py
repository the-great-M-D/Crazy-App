from django.shortcuts import render, redirect
from .forms import ProductCreate

# Create your views here.

def addProduct(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form =  ProductCreate(request.POST)
            if form.is_valid():
                form.save()
            return redirect('home')
    else:
        form = ProductCreate()
        return render(request, 'products/index.html', {'form':form})
        
        

def updateProduct(request):
    pass