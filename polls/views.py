from django.shortcuts import render
from django.http import HttpResponse

from polls.models import Question


# Class-based view example
# from django.views import View   
# class PollsView(View):
#     def get(self, request):
#         return HttpResponse("Hello, world. You're at the polls class-based view.")
    
#     def post(self, request):
#         return HttpResponse("This is a POST request to the polls class-based view.")


# Functional view example
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'polls/index.html', context=context)

