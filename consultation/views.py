from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ConsultationForm
from django.conf import settings
from django.contrib import messages
from .models import Consultation
import stripe


def consultation(request):
    print("consultation")
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        print("POST request")
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'email2': request.POST['email2'],
            'phone_number': request.POST['phone_number'],
            'consultation_idea': request.POST['consultation_idea'],
            'consultation_number': Consultation.consultation_number,
            'date': Consultation.date
        }
        order_form = ConsultationForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            return redirect(reverse('consultation_success', args=[order.consultation_number]))
        else:
            messages.error(request, 'There was an error with your form.')
    else:
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


def consultation_success(request, consultation_number):
    order = get_object_or_404(Consultation,
                              consultation_number=consultation_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {consultation_number}.')
    template = 'consultation/consultation_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
