from django.db import models
import random
from django.contrib.auth.models import User

# Create your models here.
def randomGen(min, max):
        # return a 9 digit random number
        return int(random.uniform(min,max))
    
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0 )
    account_number = models.IntegerField(default=randomGen(1000000000, 9999999999))
    date_createted = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.account_number)