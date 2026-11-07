from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def departments(request):
    return render(request, 'departments.html')

def services(request):
    return render(request, 'services.html')

def appointment(request):
    return render(request, 'appointment.html')

def contact(request):
    return render(request, 'contact.html')
