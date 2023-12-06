from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *
from tinymce.models import HTMLField
import datetime


class UserRegisterForm(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={
		"class":"input",
		"type":"text",
		"placeholder":"Enter your username"
	}) ,label="UserName")

	email = forms.EmailField(widget=forms.TextInput(attrs={
		"class":"input",
		"type":"text",
		"placeholder":"Enter your email"
	}), label="Email")

	password1 = forms.CharField(widget=forms.TextInput(attrs={
		"class":"input",
		"type":"password",
		"placeholder":"Enter your password"
	}), label="Password")

	password2 = forms.CharField(widget=forms.TextInput(attrs={
		"class":"input",
		"type":"password",
		"placeholder":"Retype your password"
	}), label="Password")

	
	first_name = forms.CharField(widget=forms.TextInput(attrs={
		"class":"input",
		"type":"text",
		"placeholder":"Enter First Name"
	}
	), label="FirstName")

	last_name = forms.CharField(widget=forms.TextInput(attrs={
		"class":"input",
		"type":"text",
		"placeholder":"Enter Last Name"
	}
	), label="LastName")

	class Meta:
		model = User
		fields = ['username', 'email','password1','password2', 'first_name', 'last_name']

class DairyForm(forms.ModelForm):
	
	class Meta:
		model = Dairy
		fields = ['title','date','content']


class ProjectForm(forms.ModelForm):
	class Meta:
		model = Projects
		fields = ['title','project_desc','project_links','project_date']
		
class BlogForm(forms.ModelForm):
	class Meta:
		model = Blogs
		fields = ['title','blog_desc','blog_date']


class NoteForm(forms.ModelForm):
	class Meta:
		model = Notes
		fields = ['title','note_desc','note_date']

class ProgImages(forms.ModelForm):
	class Meta:
		model = Project_Images
		fields = "__all__"    

class BlogImages(forms.ModelForm):
	class Meta:
		model = Blog_Images
		fields = "__all__"

class DairyImages(forms.ModelForm):
	class Meta:
		model = Dairy_Images
		fields = "__all__" 

class NoteImages(forms.ModelForm):
	class Meta:
		model = Note_Images
		fields = "__all__" 		

class Profileform(forms.ModelForm):

	gitlink = forms.URLField(widget=forms.TextInput(attrs={
		"class":"input",
		"type":"text",
		"placeholder":"Enter your GITHUB LINK"
	}) ,label="GIT Link")

	linkedin = forms.URLField(widget=forms.TextInput(attrs={
		"class":"input",
		"type":"text",
		"placeholder":"Enter your Linkedin LINK"
	}) ,label="Linkedin")

	website = forms.URLField(widget=forms.TextInput(attrs={
		"class":"input",
		"type":"text",
		"value":"12",
		"placeholder":"Enter your website LINK"
	}) ,label="Website")
	
	class Meta:
		model = ProfileModel
		fields = ['user','role','gitlink','linkedin','website','location']

class ProfileModel(forms.ModelForm):
	class Meta:
		model = ProfileModel
		fields = "__all__"
		
