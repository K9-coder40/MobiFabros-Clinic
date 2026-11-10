from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment, ContactMessage

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
    if request.method == 'POST':
        # Extract data from the HTML form 'name' attributes
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        department = request.POST.get('department')
        doctor = request.POST.get('doctor')
        message_text = request.POST.get('message')
        messages.success(request, 'Your appointment request has been successfully submitted!')
        # Save to database
        Appointment.objects.create(
            name=name,
            email=email,
            phone=phone,
            date=date,
            department=department,
            doctor=doctor,
            message=message_text
        )

        return redirect('index')
    return render(request, 'appointment.html')

def contact(request):
    if request.method == 'POST':
        # Extract data from the contact form
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')
        messages.success(request, 'Your message has been sent successfully. We will get back to you soon!')

        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message_text
        )
       
        return redirect('index')  # Matches your url name
    return render(request, 'contact.html')
