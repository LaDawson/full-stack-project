from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'default_first_name': 'First Name',
            'default_last_name': 'Last Name',
            'default_email': 'Email Address',
            'default_phone_number': 'Phone Number',
        }
        self.fields['default_email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].label = False
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
