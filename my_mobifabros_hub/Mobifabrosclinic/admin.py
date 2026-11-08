from django.contrib import admin
from .models import Appointment, ContactMessage

# Register your models here.
admin.site.register(Appointment)
admin.site.register(ContactMessage)
