from django import forms
from .models import dates
from django.forms import DateInput

class add_dates(forms.ModelForm):
	class Meta:
		model = dates
		fields = [
		'user',
		'first_semester_start', 
		'first_semester_end',
		'second_semester_start',
		'second_semester_end'
		]

		widgets = {
			'user': forms.HiddenInput(),
			'first_semester_start': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
			'first_semester_end': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
			'second_semester_start': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
			'second_semester_end': DateInput(attrs={'class': 'form-control', 'type': 'date'})
		}
	
	def clean(self):
		form_data = self.cleaned_data
		first_start = form_data['first_semester_start']
		first_end = form_data['first_semester_end']
		second_start = form_data['second_semester_start']
		second_end = form_data['second_semester_end']

		if first_start > first_end:
			self._errors["first_semester_end"] = ["Start date can't be bigger than end date"]
		if second_start > second_end :
			self._errors["second_semester_end"] = ["Start date can't be bigger than end date"]	
		if first_start > second_start:
			self._errors["second_semester_start"] = ["First semester start date can't be bigger than second semester start date"]
		if first_end > second_end:
			self._errors["second_semester_end"] = ["First semester end date can't be bigger than second semester end date"]
		return form_data

