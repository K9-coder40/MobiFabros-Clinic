from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('departments/', views.departments, name='departments'),
    path('services/', views.services, name='services'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
]