from django.contrib import admin
from .models import Note, Task, Reminder

admin.site.register(Note)
admin.site.register(Task)
admin.site.register(Reminder)
