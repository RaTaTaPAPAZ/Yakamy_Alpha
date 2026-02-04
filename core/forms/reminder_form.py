from django import forms
from core.models import Reminder


class ReminderForm(forms.ModelForm):
    remind_at = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = Reminder
        fields = ['text', 'remind_at','is_active']
