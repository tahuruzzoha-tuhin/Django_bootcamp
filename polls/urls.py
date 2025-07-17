from django.urls import path
from polls.views import index, question_list, question_create, question_update, question_delete

urlpatterns = [
    path('', index, name='index'),
    path('questions/', question_list, name='question_list'),
    path('questions/create/', question_create, name='question_create'),
    path('questions/update/<int:pk>/', question_update, name='question_update'), 
    path('questions/delete/<int:pk>/', question_delete, name='question_delete'),
]