from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from products.models import Product

# Create your views here.
class HomePage(TemplateView):
    template_name = 'home/index.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(HomePage, self).get_context_data(*args, **kwargs)
        #context["services"] = Service.objects.all()     
        return context
    
@method_decorator(login_required,name='dispatch')   
class DashBoard(TemplateView):
    template_name = 'home/dash.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(DashBoard, self).get_context_data(*args, **kwargs)
        context["products"] = Product.objects.all()
        return context
    
@method_decorator(login_required,name='dispatch')
class CreateProduct(TemplateView):
    template_name = 'home/dash.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(CreateProduct, self).get_context_data(*args, **kwargs)
        context = []
        return 
    