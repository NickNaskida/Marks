from django.shortcuts import render
from django.db.models import Q
from .models import User
from django.contrib.auth.models import User as registered_users
from enter.models import enter_marks
from django.db.models import Count

def get_ip(request):
	adress = request.META.get('HTTP_X_FORWARDED_FOR')
	if adress:
		ip = adress.split(',')[-1].strip()
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip

def home(request):
		
	ip = get_ip(request)
	u = User(user=ip)
	result = User.objects.filter(Q(user__icontains=ip))
	if len(result) == 1:
		pass
	elif len(result) > 1:
		pass
	else:
		u.save()

	count = User.objects.count()

	users_count = registered_users.objects.count()

	mark1 = len(enter_marks.objects.all())

	total = mark1 

	data = {
	'count': count, 
	'users_count': users_count,
	'total': total
	}

	return render(request, 'main/home.html', data)

	



