from django.shortcuts import render, redirect, reverse
from .forms import ConsultationForm


def consultation(request):
    consultation_form = ConsultationForm()
    template = 'consultation/consultation.html'
    context = {
        'consultation_form': consultation_form,
        'stripe_public_key': 'pk_test_51H474BHlEZ49am9XV6IE4jYsZpG7Bv7sXUIixaBlIbELEU5dmcWXbONZbKM35fl2ARA6XwBNJPH2LJWvwfRyQa9F00pNOHCLQl',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
