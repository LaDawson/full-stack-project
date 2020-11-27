from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from consultation.models import Consultation


@login_required
def admin_page(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))

    consultation = Consultation.objects.all()
    consultations = consultation.order_by('-date')

    template = 'admin_pages/admin_home.html'
    context = {
        'consultations': consultations,
    }

    return render(request, template, context)


@login_required
def consultation_history_admin(request, consultation_number):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))

    consultation = get_object_or_404(Consultation,
                                     consultation_number=consultation_number)

    messages.info(request, (
        f'This is a past confirmation for order {consultation_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'admin_pages/admin_consultation.html'
    context = {
        'consultation': consultation,
    }

    return render(request, template, context)
