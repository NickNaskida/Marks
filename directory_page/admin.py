from django.contrib import admin
from .models import *

@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
	list_display = ('subject',)
	list_filter = ('subject',)
	ordering = ('subject',)

@admin.register(Person_subjects)
class Person_subjectsAdmin(admin.ModelAdmin):
	list_display = ('user', 'subject',)
	list_filter = ('user', 'subject',)
	ordering = ('user',)
	search_fields = ('user__username', 'subject__subject')