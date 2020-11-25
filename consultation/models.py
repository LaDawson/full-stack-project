import uuid
from django.db import models
from profiles.models import Profile

class Consultation(models.Model):
    consultation_number = models.CharField(max_length=32, null=False, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="consultations")
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False, default="")
    phone_number = models.CharField(max_length=30, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    consultation_idea = models.TextField(max_length=3000, null=False, blank=False)
    consultation_cost = models.DecimalField(max_digits=5, decimal_places=2, null=False, default=30)

    def _generate_consultation_number(self):
        """ Creates a random number using UUID for the consultation """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """ Saves the uuid as the consultation number """
        if not self.consultation_number:
            self.consultation_number = self._generate_consultation_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.consultation_number
