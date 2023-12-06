
from django.contrib import admin
from django.urls import path,include
from user import views as user_view
from django.contrib.auth import views as auth
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('login/', user_view.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='user/index.html'), name ='logout'),
    path('register/', user_view.register, name ='register'),
    path(r'^tinymce/', include('tinymce.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


