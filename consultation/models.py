from django.db import models
import uuid
from django.conf import settings


class consultation(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=30, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    consultation_cost = settings.CONSULTATION_COST

    def _order_number(self):
        """ Creates a random order number using UUID for the consultation """
        return uuid.uuid4().hex

    def save_order_number(self, *args, **kwargs):
        """ Saves the uuid as the order number """
        if not self.order_number:
            self.order_number = self._order_number()
        super().save(*args, **kwargs)
        print(self.order_number)

    def __str__(self):
        return self.order.order_number
