from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from consultation.models import Consultation


def admin_page(request):
    consultation = Consultation.objects.all()
    consultations = consultation.all().order_by('-date')

    template = 'admin_pages/admin_home.html'
    context = {
        'consultations': consultations,
    }

    return render(request, template, context)


def consultation_history(request, consultation_number):
    consultation = get_object_or_404(Consultation,
                                     consultation_number=consultation_number)

    messages.info(request, (
        f'This is a past confirmation for order {consultation_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'consultation/consultation_success.html'
    context = {
        'consultation': consultation,
        'from_profile': True,
    }

    return render(request, template, context)
