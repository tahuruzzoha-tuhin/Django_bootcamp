from django import forms
from polls.models import Question, Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'description', 'pub_date']  
        widgets = {
            'pub_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'question_text': forms.TextInput(attrs={'placeholder': 'Enter question text'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter question description'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "form-control",
                # "placeholder": f"Enter {field.label}"
            })

        

        
class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['question', 'choice_text', 'votes']
        widgets = {
            'question': forms.Select(),
            'choice_text': forms.TextInput(attrs={'placeholder': 'Enter choice text'}),
            'votes': forms.NumberInput(attrs={'min': 0}),
        }   
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "form-control",
                # "placeholder": f"Enter {field.label}"
            })