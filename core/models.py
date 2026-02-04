from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="%(class)s_items"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Note(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Task(BaseModel):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='todo'
    )
    priority = models.IntegerField(default=1)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class Reminder(BaseModel):
    text = models.CharField(max_length=255)
    remind_at = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.text
