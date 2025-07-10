from django.contrib import admin

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    search_fields = ('question_text',)  
    
admin.site.register(Question, QuestionAdmin)
