from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(required=True) #subject
	email = forms.EmailField(required=True) #from email
	message = forms.CharField(widget=forms.Textarea) #message

