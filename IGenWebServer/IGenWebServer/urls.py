"""IGenWebServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from core import views as core_views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', core_views.home, name = 'landing'),
	path('home/', core_views.home, name = 'home'),
	path('signup/', core_views.signup, name = 'signup'),
	path('login/', core_views.login, name = 'login'),
	path('logout/', core_views.logout, name = 'logout'),
	path('upload', core_views.upload_dna, name = 'upload'),
	path('dashboard', core_views.dashboard, name = 'dashboard'),
	path('status', core_views.check_status, name = 'status'),
	path('about', core_views.about, name = 'about'),
	path('resources', core_views.resources, name = 'resources'),
	path('results', core_views.show_results, name = 'results'),
	path('howitworks', core_views.howitworks, name = 'howitworks'),
]
