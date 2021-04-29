from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import enter_mark
from .models import enter_marks
from django.views.generic import DeleteView
from directory_page.models import Person_subjects

@login_required
def enter(request):
	if request.method == 'POST': 
		form = enter_mark(request.POST)

		data = request.POST
		data._mutable = True
		data['user'] = request.user.id
		data._mutable = False

		if form.is_valid():
			form.save()		
			return redirect('enter')
	else:
		form = enter_mark()

	form.fields['subject'].queryset = Person_subjects.objects.filter(user=request.user.id)
		
	table_data = enter_marks.objects.select_related()\
		.filter(user= request.user.id).order_by('-id')[:10]

	data = {
	'form': form,
	'table_data': table_data
	}
	return render(request, 'enter/enter.html', data)


def deleteMark(request, pk):
	item = enter_marks.objects.filter(user= request.user.id).get(id=pk)
	
	if request.method == 'POST':
		item.delete()
		return redirect('enter')

	data = {
	'item': item,
	}
	return render(request, 'enter/enter_delete.html', data)
