from django import forms
from .models import MaintenanceTicket

class TicketForm(forms.ModelForm):
    class Meta:
        model = MaintenanceTicket
        fields = ['title', 'description', 'status']
        