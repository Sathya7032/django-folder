
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
 
urlpatterns = [

    path('', views.index, name ='index'),
    path('base/',views.base,name='base'),
    path('homepage/', views.homepage, name ='homepage'),
    path('tutorials/', views.tutorials, name ='tutorials'),
    path('profile/', views.profile, name="profile"),
    path('addDiary/', views.addDiary,name="addDiary"),
    path('addNote/', views.addNote,name="addNote"),
    path('addBlog/', views.addBlog,name="addBlog"),
    path('addProject/', views.addProject,name="addProject"),
    path('projects/', views.projects,name="projects"),
    path('note/', views.note,name="note"),
    path('blogs/', views.blogs,name="blogs"),
    path('dairy/', views.dairy,name="dairy"),
    path('dairy/<slug:dairy_id>', views.dairyView),
    path('blog/<slug:blog_id>', views.blogView),
    path('note/<slug:note_id>', views.noteView),
    path('project/<slug:project_id>', views.projectView),
    path('profileForm/',views.profileForm,name="profileForm"),
    path('blog_feed/',views.blog_feed,name="blog_feed"),
    path('tutorials/html1/',views.index1,name="index1"),
    path('contact/',views.contactHandler,name="contact"),
]
