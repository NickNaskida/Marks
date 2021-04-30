from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from enter.models import enter_marks
from semester_dates.models import dates
from .filters import enter_marks_filter
from django.db.models import Avg
from django.db.models import Q
from directory_page.models import Person_subjects

@login_required
def reports(request):
	table_data = enter_marks.objects.select_related().filter(user = request.user.id).order_by('-enter_date')

	tableFilter = enter_marks_filter(request.GET, request=request.user.id, queryset= table_data) #
	table_data = tableFilter.qs

	model_data = dates.objects.get(user = request.user.id)

	f_start = model_data.first_semester_start
	f_end = model_data.first_semester_end
	s_start = model_data.second_semester_start
	s_end = model_data.second_semester_end


	f_1 = enter_marks.objects.filter(Q(enter_date__range=(f_start, f_end)), user=request.user.id)\
		.aggregate(Avg('mark'))
	
	s_1 = enter_marks.objects.filter(Q(enter_date__range=(s_start, s_end)), user=request.user.id)\
		.aggregate(Avg('mark'))
	

	if f_1['mark__avg'] == None:
		f_avg = 0
	else:
		f_avg = f_1['mark__avg']
	

	if s_1['mark__avg'] == None:
		s_avg = 0	
	else:
		s_avg = s_1['mark__avg']

	if f_avg and s_avg > 0:
		b_avg = round((f_avg + s_avg) / 2, 1)
	else:
		b_avg = '-'

	f_avg = round(f_avg, 1)	
	s_avg = round(s_avg, 1)	

	data = {
	'table_data': table_data,
	'filter': tableFilter,
	'f_avg': f_avg,
	's_avg': s_avg,
	'b_avg': b_avg
	}
	return render(request, 'reports/reports.html', data)