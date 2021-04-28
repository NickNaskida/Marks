from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

class Subjects(models.Model):
	subject = models.CharField(max_length=100)
	
	def __str__(self):
		return self.subject
	
	class Meta:
		verbose_name = 'Subject'
		verbose_name_plural = 'Subjects'

class Person_subjects(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	subject = models.ForeignKey(Subjects, on_delete=models.PROTECT, null=True)

	class Meta:
		verbose_name = "Person's subject"
		verbose_name_plural = "Person's subjects"

	def __str__(self):
          return '{}'.format(self.subject)	


