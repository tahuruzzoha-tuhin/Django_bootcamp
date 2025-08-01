from django.urls import path
from polls.views import *

urlpatterns = [
    path('', index, name='index'),
    path('questions/', question_list, name='question_list'),
    path('questions/create/', question_create, name='question_create'),
    path('questions/update/<int:pk>/', question_update, name='question_update'), 
    path('questions/delete/<int:pk>/', question_delete, name='question_delete'),
    
    path('choices/', choice_list, name='choice_list' ),
    path('choices/create/', choice_create, name='choice_create'),
    path('choices/update/<int:pk>/', choice_update, name='choice_update'), 
    path('choices/delete/<int:pk>/', choice_delete, name='choice_delete'),
]