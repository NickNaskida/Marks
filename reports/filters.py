import django_filters
from django_filters import DateFilter
from django.forms import DateInput
from django.conf import settings

from enter.models import enter_marks
from directory_page.models import Person_subjects

Choices1 = (
	('10', '10'), ('9', '9'),
	('8', '8'), ('7', '7'),
	('6', '6'), ('5', '5'),
	('4', '4'), ('3', '3'),
	('2', '2'), ('1', '1'),
	)


class enter_marks_filter(django_filters.FilterSet):
	mark1_f = django_filters.ChoiceFilter(field_name='mark', choices=Choices1, empty_label='All', label='')
	enter_date_f = DateFilter(field_name='enter_date', widget=DateInput(attrs={'placeholder': 'mm/dd/yyyy'}), label='')
	
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('request', None)
		super(enter_marks_filter, self).__init__(*args, **kwargs)
		self.filters['subject'].extra.update({'empty_label': 'All Subjects'})
		self.filters['subject'].label=''
		self.filters['subject'].queryset = Person_subjects.objects.filter(user=self.user)
		
	class Meta:
		model = enter_marks
		fields = ['subject']