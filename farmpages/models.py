from django.db import models
# Create your models here.
class VendorForm(models.Model):
	username=models.CharField(max_length=50,blank=False,null=True)
	email=models.EmailField(blank=False,null=True, unique=True)
	phone=models.CharField(max_length=10,blank=False,null=True)
	password1=models.CharField(max_length=32, blank=False,null=True)
	password2=models.CharField(max_length=32, blank=False,null=True)
	city=models.CharField(max_length=32,blank=False,null=True)
	pincode=models.CharField(max_length=6,blank=False,null=True)
	state=models.CharField(max_length=32,blank=False,null=True)
	country=models.CharField(max_length=32,blank=False,null=True)

class visitform(models.Model):
	name=models.CharField(max_length=50,blank=False,null=True)
	purpose=models.CharField(max_length=20,blank=False,null=True)
	phone=models.CharField(max_length=10,blank=False,null=True)
	time=models.CharField(max_length=44,blank=False,null=True)
	date=models.CharField(max_length=44,blank=False,null=True)
	insti=models.CharField(max_length=44,blank=False,null=True)
	num=models.CharField(max_length=44,blank=False,null=True)