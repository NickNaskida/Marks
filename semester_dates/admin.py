from django.contrib import admin
from .models import *

@admin.register(dates)
class enter_marksAdmin(admin.ModelAdmin):
	list_display = (
		'user',
		'first_semester_start',
		'first_semester_end',
		'second_semester_start',
		'second_semester_end',
		)
