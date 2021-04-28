from django import forms
from django.forms import DateInput, Select, HiddenInput
from .models import enter_marks
from django.core.exceptions import ValidationError
from datetime import datetime

Choices1 = (
	('10', '10'), ('9', '9'),
	('8', '8'), ('7', '7'),
	('6', '6'), ('5', '5'),
	('4', '4'), ('3', '3'),
	('2', '2'), ('1', '1'),
	)

class enter_mark(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['subject'].empty_label = 'Select Subject'

	class Meta:
		model = enter_marks
		fields = [
		'user',
		'subject',
		'mark',
		'enter_date'
		] 	
		widgets = {
			'user': forms.HiddenInput(),
			'subject': forms.Select(),
			'mark': forms.Select(choices=Choices1),
			'enter_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'value': datetime.now().strftime("%Y-%m-%d")})
		}

	def clean(self):	
		form_data = self.cleaned_data
		subject = form_data['subject']
		user = form_data['user']
		enter_date = form_data['enter_date']

		if len(enter_marks.objects.filter(subject=subject, user=user, enter_date=enter_date)) > 1:
			self._errors["subject"] = ["You can't have more marks in {} today".format(subject)]
		return form_data
