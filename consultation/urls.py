from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.consultation, name='consultation'),
    path('consultation_success/<consultation_number>', views.consultation_success, name='consultation_success'),
    path('cache_consultation_data/', views.cache_consultation_data, name='cache_consultation_data'),
    path('wh/', webhook, name='webhook'),
]
