from django.urls import path
from . import views

urlpatterns = [
	path('', views.semester_dates, name='semester_dates'),
]