from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
import pyttsx3
from .models import *
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
#################### index#######################################

engine = pyttsx3.init()

def index(request):
	return render(request, 'user/index.html', {'title':'index'})

########### register here #####################################
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			######################### mail system ####################################
			htmly = get_template('user/Email.html')
			d = { 'username': username }
			subject, from_email, to = 'welcome', 'your_email@gmail.com', email
			html_content = htmly.render(d)
			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			##################################################################
			messages.success(request, f'Your account has been created ! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
		messages.warning(request, f'something went wrong, please try again..')
	return render(request, 'user/register.html', {'form': form, 'title':'register here'})

################ login forms###################################################
def Login(request):
	if request.method == 'POST':
		# AuthenticationForm_can_also_be_used__
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' welcome {username} !!')
			return redirect('homepage')
		else:
			messages.info(request, f'username or password is incorrect')
	form = AuthenticationForm()
	return render(request, 'user/login.html', {'form':form, 'title':'log in'})

@login_required
def homepage(request):
	return render(request,"user/homepage.html",{'dairy':dairy})

@login_required
def tutorials(request):
	users = User.objects.all()
	return render(request,"tutorial/tutorialhome.html",{'users':users})

@login_required
def profile(request):
	if request.user.is_active:
		user = User.objects.get(username=request.user)
		last_login = user.last_login.strftime('%y-%m-%d %A %I:%M:%S %p')
		progs = Projects.objects.filter(project_user = request.user).count
		blogs = Blogs.objects.filter(blog_user=request.user).count()
		dairy = Dairy.objects.filter(user=request.user).count()
		note = Notes.objects.filter(note_user=request.user).count()
		note1 = Notes.objects.filter(note_user = request.user)
		blogs1 = Blogs.objects.filter(blog_user = request.user)
		dict={
			'progs':progs,
			'blogs':blogs,
			'dairy':dairy,
			'note':note,
			'note1':note1,
		       }				
		
	return render(request,"user/profile.html",{'dict':dict,'last_login':last_login,'blogs1':blogs1})

@login_required
def addDiary(request):
	if request.method=='POST':
		form = DairyForm(request.POST)
		if form.is_valid():
			new_dairy=form.save()
			new_dairy.user = request.user
			new_dairy.save()
			messages.success(request, f'Your dairy is added successfully !....')
			return redirect('homepage')
	else:
		form = DairyForm()	
	return render(request,"add/addDairy.html",{'form':form, 'title':'log in'})

@login_required
def projects(request):
	progs = Projects.objects.filter(user=request.user)
	return render(request,"landingpages/project.html",{'progs':progs})

@login_required
def blogs(request):
	blogs = Blogs.objects.filter(user=request.user)
	
	return render(request,"landingpages/blog.html",{'blogs':blogs})

@login_required
def dairy(request):
	dairy = Dairy.objects.filter(user= request.user)
	return render(request,"landingpages/dairy.html",{'dairy':dairy})

@login_required
def note(request):
	note = Notes.objects.filter(user=request.user)
	return render(request,"landingpages/note.html",{'note':note})

@login_required
def addNote(request):
	if request.method=='POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			new_note=form.save()
			new_note.user = request.user
			new_note.save()
			messages.success(request, f'Your notes is added successfully !....')
			return redirect('homepage')
	else:
		form = NoteForm()	
	return render(request,"add/addnote.html",{'form':form, 'title':'log in'})

@login_required
def addBlog(request):
	if request.method=='POST':
		form = BlogForm(request.POST)
		if form.is_valid():
			new_blog=form.save()
			new_blog.user = request.user
			new_blog.save()
			messages.success(request, f'Your blog is added successfully !....')
			return redirect('homepage')
	else:
		form = BlogForm()	
	return render(request,"add/addblog.html",{'form':form, 'title':'log in'})

@login_required
def addProject(request):
	if request.method=='POST':
		form = ProjectForm(request.POST)
		if form.is_valid():
			new_project=form.save()
			new_project.user = request.user
			new_project.save()
			messages.success(request, f'Your project is added successfully !....')
			return redirect('homepage')
	else:
		form = ProjectForm()	
	return render(request,"add/addproject.html",{'form':form, 'title':'log in'})

@login_required
def dairyView(request, dairy_id):
    dairy = Dairy.objects.get(dairy_id=dairy_id)
    dairy1 = Dairy_Images.objects.filter(dairy_id=dairy_id)
	
    return render(request,'single/1dairy.html',{'dairy':dairy, 'dairy1': dairy1})


@login_required
def blogView(request, blog_id):
	blog = Blogs.objects.get(blog_id=blog_id)
	blog1 = Blog_Images.objects.filter(blog_id=blog_id)
	return render(request,'single/1blog.html',{'blog':blog, 'blog1': blog1})



@login_required
def noteView(request, note_id):
    note = Notes.objects.get(note_id=note_id)
    note1 = Notes.objects.all()
    return render(request,'single/1note.html',{'note':note, 'note1': note1})

@login_required
def projectView(request, project_id):
    project = Projects.objects.get(project_id=project_id)
    project1 = Projects.objects.all()
    return render(request,'single/1project.html',{'project':project, 'project11': project1})

@login_required
def projImage(request):
	if request.method=='POST':
		form = ProgImages(request.POST)
		if form.is_valid():
			prog_img = form.save()
			prog_img.project_id=request.project_id
			prog_img.save()
	return render(request,'single/1project.html')

@login_required
def profileForm(request):
	if request.method=='POST':
		form = Profileform(request.POST)
		if form.is_valid():
			new_profile=form.save()
			new_profile.user = request.user
			new_profile.save()
			print("saved")
			messages.success(request, f'Your profile is added successfully !....')
			return redirect('profile')
	else:
		form = Profileform()	
		print("failled")
	return render(request,"user/profileUpload.html",{'form':form, 'title':'form'})

@login_required
def base(request):
	profile_user = ProfileModel.objects.get(user=request.user)
	return render(request,"user/base.html",{'profile_user':profile_user})

@login_required
def blog_feed(request):
	blogs = Blogs.objects.all()
	profile_user = ProfileModel.objects.all()
	return render(request,"common/blog_feed.html",{'blogs':blogs})


def index1(request):
    posts = Post.objects.all()  # fetching all post objects from database
    p = Paginator(posts, 1)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    # sending the page object to index.html
    return render(request, "common/html1.html",{'page_obj':page_obj})



def contactHandler(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject2 = request.POST.get('subject')
        message1 = request.POST.get('message')
        print(name)
        query = Contact(name=name,email=email,subject=subject2,message=message1)
        query.save()

        subject = 'THANK YOU FOR CONTACTING ME '
        message = f'Hi {name}, Thank you so much for reaching out to me. I will get back to you as soon as possible '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )

        
        subject1 = 'HELLOW SIR YOU GOT A NEW MAIL'
        message = f'Hi k satyanarayana chary,  Some one contacted you details are:- \n username - {name},\n  email - {email},\n subject - {subject2},\n message - {message1} \n'
        email_from = settings.EMAIL_HOST_USER
        recipient_list1 = ['charysatheesh4@gmail.com', ]
        send_mail( subject1, message, email_from, recipient_list1 )

        messages.success(request,"Thanks for contacting me ,I will look forward to utilize this oppertunity.....")
        return redirect('/contact/')
    
    return render(request, 'tutorial/contact.html')

