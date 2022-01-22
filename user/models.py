from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver 
from PIL import Image
import random
import datetime

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	mugshot = models.ImageField(default= 'default.jpg',upload_to='Profile_pics',blank=True)
	description = models.TextField(help_text='A Brief Description OF Yorself ',blank=True)
	#Product = models.ManyToManyField("Product", blank=True) --> tobe fully implimented
	verified = models.BooleanField(default=False, help_text='To Be Used Later For Account Verification ')
	phone_number = models.CharField(max_length=13, blank=True)#PhoneField() needs to be implimented  
	address = models.TextField(blank=True)
 
 

	def __str__(self):
		return str(self.user.username)




    
