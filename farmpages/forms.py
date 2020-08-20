from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import VendorForm,visitform
class CreateUserForm(UserCreationForm):
	# pic=forms.ImageField()
	class Meta:
		model	= User
		fields	= ['username','email','first_name','last_name','password1','password2']
class VendorForm(ModelForm):
	class Meta:
		model	= VendorForm
		fields='__all__'
		widgets = {
            'password1': forms.PasswordInput(),'password2': forms.PasswordInput(),
        }
class visitform(ModelForm):
	class Meta:
		model	= visitform
		fields='__all__'
	# def clean_pass(self):
	# 	password1=self.cleaned_data.get("password1")
	# 	password2=self.cleaned_data.get("password2")
	# 	if password1!=password2:
	# 		raise forms.ValidationError("Password fields don't match")
	# 	return password1,password2