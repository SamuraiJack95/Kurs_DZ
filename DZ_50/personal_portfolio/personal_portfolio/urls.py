"""
URL configuration for personal_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from skills import views

# app_name = 'work'

urlpatterns = [
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('blog/', include('blog.urls')),
    path('works/', views.video_get, name='videoget'),
    path('<int:work_id>/', views.detail, name='detail'),
    path('create/', views.createskills, name='createskills'),
    path('skills/<int:skills_pk>', views.viewskills, name='viewtodo'),
    path('skills/<int:skills_pk>/delete', views.deleteskills, name='deleteskills'),

]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)