from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('consultation_history/<consultation_number>', views.consultation_history, name='consultation_history'),

]
