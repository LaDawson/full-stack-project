from django.shortcuts import render, redirect, reverse
from .forms import ConsultationForm


def consultation(request):
    consultation_form = ConsultationForm()
    template = 'consultation/consultation.html'
    context = {
        'consultation_form': consultation_form,
    }

    return render(request, template, context)
