from django.db import models


class User(models.Model):
	user = models.TextField(default=None)
	def __str__(self):
		return self.user

	class Meta:
		verbose_name = 'Visitor'
		verbose_name_plural = 'Visitors'	