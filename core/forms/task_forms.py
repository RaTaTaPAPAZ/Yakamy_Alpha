from django import forms
from core.models import Task


class TaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'due_date']
