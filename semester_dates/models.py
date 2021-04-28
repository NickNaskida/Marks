from django.db import models
from django.contrib.auth.models import User

class dates(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	first_semester_start = models.DateField('First semester start date')
	first_semester_end = models.DateField('First semester end date')
	second_semester_start = models.DateField('Second semester start date')
	second_semester_end =  models.DateField('Second semester end date')

	class Meta:
		verbose_name = "Person's date"
		verbose_name_plural = "Person's dates"
