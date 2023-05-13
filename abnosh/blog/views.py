from django.shortcuts import render
from .models import Education , Person 


# Create your views here.

def home(request) : 
    person  = Person.objects.all()[0]
    context = {'person' : person }  
    return render(request , 'website/index.html' , context )
