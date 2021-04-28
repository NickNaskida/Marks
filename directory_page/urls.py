from django.urls import path
from . import views

urlpatterns = [
	path('', views.directory_page, name='directory_page'),
	path('<str:pk>/delete', views.deleteSubject, name='directory_delete'),
]