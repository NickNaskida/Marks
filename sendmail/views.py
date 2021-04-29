from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages

@login_required
def sendmail(request):
	if request.method == 'POST':   
	    form = ContactForm(request.POST)
	    if form.is_valid():
	        name = form.cleaned_data['name']
	        email = form.cleaned_data['email']
	        message = form.cleaned_data['message'] + "|| Senders email: " + f'{email}'

	        try:
	        	send_mail(
	            	name, #subject
					message, #message
					email, #from email
					['sitemail.geo@gmail.com'], #to email
					)
	        except BadHeaderError:
	        	return httpResponse('Invalid header found')
	        messages.success(request, f'Thanks {name}! We received your email and will respond shortly...')	
	        return redirect('home')	
	else:
		form = ContactForm()    	
	return render(request, 'sendmail/mail.html', {'form': form}) 
 
    	   	

