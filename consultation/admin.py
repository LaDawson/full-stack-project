from django.contrib import admin
from .models import Consultation


class ConsulationAdmin(admin.ModelAdmin):
    readonly_fields = ('consultation_number', 'date', 'consultation_cost'
                       )

    fields = ('consultation_number', 'user_profile', 'date',
              'email', 'first_name', 'last_name',
              'phone_number', 'consultation_idea',
              'consultation_cost'
              )

    list_display = ('consultation_number', 'date',
                    'first_name', 'email',)

    ordering = ('-date',)


admin.site.register(Consultation, ConsulationAdmin)
