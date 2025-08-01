from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from polls.models import Question, Choice
from polls.forms import QuestionForm, ChoiceForm


# Class-based view example
# from django.views import View   
# class PollsView(View):
#     def get(self, request):
#         return HttpResponse("Hello, world. You're at the polls class-based view.")
    
#     def post(self, request):
#         return HttpResponse("This is a POST request to the polls class-based view.")


# Functional view example
def index(request):
    return render(request, 'polls/base.html')


def question_list(request):
    questions_items = Question.objects.all()
    return render(request, 'polls/question_list.html', {'questions': questions_items})


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question_list')
    else:
        form = QuestionForm()
    return render(request, 'polls/question_form.html', {'form': form})

def question_update(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('question_list')
    else:
        form = QuestionForm(instance=question)
    return render(request, 'polls/question_form.html', {'form': form})

def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        question.delete()
        return redirect('question_list')
    # return HttpResponse("Deleted")
    return render(request, 'polls/question_confirm_delete.html', {'question': question})



# Choices

def choice_list(request):
    choices = Choice.objects.all()
    return render(request, "polls/choice_list.html", {"choices": choices})

def choice_create(request):
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("choice_list")
    else:
        form = ChoiceForm()
    return render(request, "polls/choice_form.html", {'form':form})




def choice_update(request, pk):
    choices = get_object_or_404(Choice, pk=pk)
    if request.method == 'POST':
        form = ChoiceForm(request.POST, instance=choices)
        if form.is_valid():
            form.save()
            return redirect('choice_list')
    else:
        form = ChoiceForm(instance=choices)
    return render(request, 'polls/choice_form.html', {'form': form})



def choice_delete(request, pk):
    choice = get_object_or_404(Choice, pk=pk)
    if request.method == 'POST':
        choice.delete()
        return redirect('choice_list')
    # return HttpResponse("Deleted")
    return render(request, 'polls/choice_confirm_delete.html', {'choice': choice})