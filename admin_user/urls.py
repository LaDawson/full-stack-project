from django.urls import path
from . import views


urlpatterns = [
    path('', views.admin_page, name='admin_page'),
    path('consultation_history_admin/<consultation_number>',
         views.consultation_history_admin, name='consultation_history_admin')
]
