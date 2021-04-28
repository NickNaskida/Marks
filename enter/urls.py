from django.urls import path
from . import views

urlpatterns = [
	path('', views.enter, name='enter'),
	path('<str:pk>/delete', views.deleteMark, name='enter_delete'),
]