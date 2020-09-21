import uuid
from django.db import models


class Consultation(models.Model):
    consultation_number = models.CharField(max_length=32, null=False, editable=False)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=30, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    consultation_idea = models.CharField(max_length=3000, null=False, blank=False)
    consultation_cost = models.DecimalField(max_digits=5, decimal_places=2, null=False, default=30)

    def _consultation_number(self):
        """ Creates a random number using UUID for the consultation """
        return uuid.uuid4().hex.upper()

    def save_consultation_number(self, *args, **kwargs):
        """ Saves the uuid as the consultation number """
        if not self.consultation_number:
            self.consultation_number = self._consultation_number()
        super().save(*args, **kwargs)
        print(self.consultation_number)

    def __str__(self):
        return self.consultation_number
