from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,VendorForm,visitform
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import random
# Create your views here.
def register(request):
	form=CreateUserForm()
	if request.method=="POST":
		form=CreateUserForm(request.POST)
		if form.is_valid():
			form.save()

			user=form.cleaned_data.get('username')
			messages.success(request,'Account created Successfully! Welcome '+user)
			return redirect('login_view')
	context= {'form':form}
	return render(request,'signup.html',context)
# def success(request): 
#     return HttpResponse('successfully created!') 
def login_view(request):
	if request.method=="POST":
		username=request.POST.get('username')
		password=request.POST.get('password')
		od=request.POST.get('check')
		user=authenticate(request,username=username,password=password)
		if user is not None:
			if od=='0':
				return redirect('dashboard')
			if od=='1':
				return redirect('home')
		else:
			messages.info(request,'Username/Password Incorrect!!')

	context= {}
	return render(request,'login.html',context)

def home(request):
	context={}
	return render(request,'index.html',context)
def dashboard(request):
	context={}
	return render(request,'dashboard1.html',context)	
# def login(request):
# 	context={}
# 	return render(request,'login.html',context)
# def signup(request):
# 	context={}
# 	return render(request,'signup.html',context)
def vendorlog(request):
	form=VendorForm()
	if request.method=="POST":
		form=VendorForm(request.POST)

		if form.is_valid():
			form.save()
			user=form.cleaned_data.get('username')
			messages.success(request,'Account created Successfully! Welcome '+user)
			return redirect('login_view')
	context= {'form':form}
	return render(request,'vendorreg.html',context)

def visitpass(request):
	form=visitform()
	if request.method=="POST":
		form=visitform(request.POST)
		if form.is_valid():
			form.save()
			user=form.cleaned_data.get('name')
			phone=form.cleaned_data.get('phone')
			purpose=form.cleaned_data.get('purpose')
			date=form.cleaned_data.get('date')
			time=form.cleaned_data.get('time')
			inti=form.cleaned_data.get('insti')
			a="FRMG2020"+str(random.randint(5343,4354354))+"OKA"
			print(a)
			context={'a':a,'user':user,'phone':phone,'purpose':purpose,'date':date,'time':time,'inti':inti}
			return render(request,'recipt.html',context)	
	context= {'form':form}
	return render(request,'dashboard1.html',context)
