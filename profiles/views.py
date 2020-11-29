from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from consultation.models import Consultation
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):

    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
    consultations = profile.consultation.all().order_by('-date')

    if request.method == 'POST':

        form = UserProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated')

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'consultations': consultations,
    }

    return render(request, template, context)


@login_required
def consultation_history(request, consultation_number):

    consultation = get_object_or_404(Consultation,
                                     consultation_number=consultation_number)

    messages.info(request, (
        f'This is a past confirmation for order {consultation_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'consultation/consultation_success.html'
    context = {
        'consultation': consultation,
        'from_profile': True,
    }

    return render(request, template, context)
