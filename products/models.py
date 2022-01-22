from django.db import models
import random
from django.contrib.auth.models import User

def randomGen(min, max):
        # return a 6 digit random number
        return int(random.uniform(min,max))
    
class Product(models.Model):
    name = models.CharField(max_length=120,help_text='Name of the Product')
    description = models.TextField(help_text='A Brief Description of the Product  ',blank=True)
    image = models.ImageField(default= 'default.jpg',upload_to='Profile_pics/products',blank=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    user = models.ForeignKey(to=User, related_name='products',on_delete=models.CASCADE)
    customer = models.ForeignKey(to=User, related_name='customer', null=True, blank=True,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)
    oder_id  = models.IntegerField(default=randomGen(100000, 999999))
    
    
    def __str__(self):
        return self.name