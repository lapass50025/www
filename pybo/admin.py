from django.contrib import admin

from pybo import models

class QuestionAdmin(admin.ModelAdmin):
	search_fields = ['subject']

admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Answer)
