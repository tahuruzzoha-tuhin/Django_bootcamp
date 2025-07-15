
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
    
]


# python manage.py runserver
# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser