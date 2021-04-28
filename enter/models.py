from django.db import models
from django.contrib.auth.models import User
from directory_page.models import Person_subjects

class enter_marks(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	subject = models.ForeignKey(Person_subjects, on_delete=models.PROTECT, null=True)
	mark = models.IntegerField()
	enter_date = models.DateField()

	class Meta:
		verbose_name = "Users mark"
		verbose_name_plural = "Users marks"

	def __str__(self):
		return '{}, {}, {}'.format(self.subject, self.mark, self.enter_date)

