from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	#path('enter', views.enter, name='enter'),
	#path('reports', views.reports, name='reports'),
	#path('directory', views.directory, name='directory'),
]