from django.contrib import admin
from .models import *

@admin.register(enter_marks)
class enter_marksAdmin(admin.ModelAdmin):
	list_display = ('user', 'subject', 'mark', 'enter_date',)
	list_filter = ('user', 'subject', 'mark', 'enter_date')
	ordering = ('-enter_date',)
	search_fields = ('user__username', 'subject__subject__subject', 'mark', 'enter_date')

