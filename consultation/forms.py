from django import forms
from .models import Consultation


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ('first_name', 'last_name', 'email',
                  'phone_number', 'consultation_idea',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Surname',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'consultation_idea': 'Project Idea/Description'
        }
        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].label = False
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]