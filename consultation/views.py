from django.shortcuts import render, redirect, reverse
from .forms import ConsultationForm
from django.conf import settings
import stripe

def consultation(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    stripe_total = (30 * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    consultation_form = ConsultationForm()
    template = 'consultation/consultation.html'
    context = {
        'consultation_form': consultation_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
