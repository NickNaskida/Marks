from django import forms
from .models import Subjects, Person_subjects


class subject_add(forms.ModelForm): 
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['subject'].empty_label = 'Select Subject'
		self.fields['subject'].label = ''

	class Meta:
		model = Person_subjects
		fields = ['user', 'subject']
		widgets = {
			'user': forms.HiddenInput(),
			'subject': forms.Select()
		}

	def clean(self):
		form_data = self.cleaned_data
		subject = form_data['subject']
		user = form_data['user']

		if len(Person_subjects.objects.filter(subject=subject, user=user)) >= 1:
			self._errors["subject"] = ["You already have this subject"] 
		return form_data

	

#subject = forms.ModelChoiceField(queryset=Subjects.objects.all()
#, label='', empty_label='Select Subject')
