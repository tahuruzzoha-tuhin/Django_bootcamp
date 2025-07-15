from django.contrib import admin

from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', "created_to")
    search_fields = ('question_text',)  
    list_filter = ('pub_date',)

    
admin.site.register(Question, QuestionAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes', 'created_at')
    search_fields = ('choice_text',)
    list_filter = ('created_at',)

admin.site.register(Choice, ChoiceAdmin)