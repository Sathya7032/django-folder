from django.db import models
from django.contrib.auth.models import User
import datetime
from tinymce.models import HTMLField


class Dairy(models.Model):
    dairy_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    date = models.DateField(("Date"), default=datetime.date.today)
    content = HTMLField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    project_desc = HTMLField()
    project_links = models.TextField(max_length=100)
    project_date = models.DateField(("Date"), default=datetime.date.today)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title
    
class Blogs(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    blog_desc = HTMLField()
    blog_date = models.DateField(("Date"), default=datetime.date.today)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title
    
class Notes(models.Model):
    note_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    note_desc = HTMLField()
    note_date = models.DateTimeField(("Date"),default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title
    
class Project_Images(models.Model):
    image_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='Photos') 
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)


class Blog_Images(models.Model):
    image_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='Photos')
    blog_id = models.ForeignKey(Blogs,on_delete=models.CASCADE)   


class Dairy_Images(models.Model):
    image_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='Photos')
    dairy_id = models.ForeignKey(Dairy,on_delete=models.CASCADE)
    
class Note_Images(models.Model):
    image_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='Photos')
    note_id = models.ForeignKey(Notes,on_delete=models.CASCADE)

class ProfileModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    gitlink = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    website = models.URLField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.role

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=1000)
    post_date = models.DateField(("Date"), default=datetime.date.today)
    post_desc = HTMLField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title

class PostImagess(models.Model):
    images_id = models.AutoField(primary_key=True)
    post_images = models.FileField( upload_to='Posts')
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)   

    def __str__(self):
        return self.post_images 
       
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField(max_length=40)
    
    def __str__(self):
        return self.name
    
class Css(models.Model):
    css_id = models.AutoField(primary_key=True)
    css_title = models.CharField(max_length=1000)
    css_date = models.DateField(("Date"), default=datetime.date.today)
    css_desc = HTMLField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.css_title
    
class CssImagess(models.Model):
    images_id = models.AutoField(primary_key=True)
    css_images = models.FileField( upload_to='Posts')
    css_id = models.ForeignKey(Css, on_delete=models.CASCADE)   

    def __str__(self):
        return self.css_images     
    
class Java(models.Model):
    java_id = models.AutoField(primary_key=True)
    java_title = models.CharField(max_length=1000)
    java_date = models.DateField(("Date"), default=datetime.date.today)
    java_desc = HTMLField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.java_title

class JavaImagess(models.Model):
    images_id = models.AutoField(primary_key=True)
    java_images = models.FileField( upload_to='Posts')
    java_id = models.ForeignKey(Java, on_delete=models.CASCADE)   

    def __str__(self):
        return self.java_images 

class Python(models.Model):
    python_id = models.AutoField(primary_key=True)
    python_title = models.CharField(max_length=1000)
    python_date = models.DateField(("Date"), default=datetime.date.today)
    python_desc = HTMLField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.python_title 

class PythonImagess(models.Model):
    images_id = models.AutoField(primary_key=True)
    python_images = models.FileField( upload_to='Posts')
    python_id = models.ForeignKey(Post, on_delete=models.CASCADE)   

    def __str__(self):
        return self.python_images            