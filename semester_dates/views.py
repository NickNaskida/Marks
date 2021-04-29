from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import add_dates
from .models import dates


@login_required
def semester_dates(request):
	userDates = dates.objects.get(user=request.user.id)
	DisplayDates = dates.objects.filter(user=request.user.id)
	
	if request.method == 'POST':
		form = add_dates(request.POST, instance=userDates)

		data = request.POST
		data._mutable = True
		data['user'] = request.user.id
		data._mutable = False

		if form.is_valid():
			form.save()
			return redirect('directory_page') 
	else:
		form = add_dates(instance=userDates)
		
	data = {
		'form': form,
		'dates': DisplayDates
	}
	return render(request, 'semester_dates/dates.html', data)



