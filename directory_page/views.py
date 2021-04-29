from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import subject_add
from .models import *
from enter.models import enter_marks
from semester_dates.models import dates

@login_required
def directory_page(request):
	if len(dates.objects.filter(user=request.user.id)) == 0:
		dates.objects.create(
			user=request.user,
			first_semester_start='2020-09-15',
			first_semester_end='2020-12-31',
			second_semester_start='2021-01-15',
			second_semester_end='2021-07-01'
			)

	if request.method == 'POST': 
		form = subject_add(request.POST)

		data = request.POST
		data._mutable = True
		data['user'] = request.user.id
		data._mutable = False
		
		if form.is_valid():
			form.save()		
			return redirect('directory_page')			
	else:	
		form = subject_add()

	subjects = Person_subjects.objects.select_related().filter(user= request.user.id)

	data = {
		'form': form,
		'subjects': subjects		
	}	

	return render(request, 'directory_page/directory.html', data)

def deleteSubject(request, pk):
	item = Person_subjects.objects.filter(user= request.user.id).get(id=pk)
	has_mark = len(enter_marks.objects.filter(user=request.user.id, subject=item))
	
	if request.method == 'POST':
		item.delete()
		return redirect('directory_page')

	data = {
	'item': item,
	'has_mark': has_mark
	}
	return render(request, 'directory_page/directory_delete.html', data)

