from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Consultation
import time


class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, consultation):

        customer_email = consultation.email
        subject = render_to_string(
            'confirmation_emails/confirmation_email_subject.txt',
            {'consultation': consultation})
        body = render_to_string(
            'confirmation_emails/confirmation_email_body.txt',
            {'consultation': consultation,
             'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    def _send_consultation_email(self, consultation):

        contact_email = settings.DEFAULT_FROM_EMAIL
        subject = render_to_string(
            'confirmation_emails/confirmation_email_subject_admin.txt',
            {'consultation': consultation})
        body = render_to_string(
            'confirmation_emails/confirmation_email_body_admin.txt',
            {'consultation': consultation})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [contact_email]
        )

    def handle_event(self, event):

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):

        intent = event.data.object
        pid = intent.id
        billing_details = intent.charges.data[0].billing_details

        consultation = Consultation.objects.get(
            first_name__iexact=billing_details.name,
            email__iexact=billing_details.email,
            phone_number__iexact=billing_details.phone,
            stripe_pid=pid,
        )

        self._send_confirmation_email(consultation)
        self._send_consultation_email(consultation)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} \
                Consultation received, confirmation email sent',
            status=200)

    def handle_payment_intent_payment_failed(self, event):

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
