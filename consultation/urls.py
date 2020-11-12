from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.consultation, name='consultation'),
    path('consultation_success/<consultation_number>', views.consultation_success, name='consultation_success'),
]
