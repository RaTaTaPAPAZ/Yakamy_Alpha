from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Note, Task, Reminder
from django.shortcuts import redirect
from .forms.note_forms import NoteForm
from django.shortcuts import get_object_or_404
from .forms.task_forms import TaskForm
from .forms.reminder_form import ReminderForm


@login_required
def dashboard(request):
    notes = Note.objects.filter(user=request.user)
    tasks = Task.objects.filter(user=request.user)
    reminders = Reminder.objects.filter(user=request.user)

    context = {
        'notes': notes,
        'tasks': tasks,
        'reminders': reminders,
    }
    return render(request, 'dashboard.html', context)
@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('dashboard')
    else:
        form = NoteForm()

    return render(request, 'note_form.html', {'form': form})
@login_required
def edit_note(request, note_id):
    # 1. Получаем заметку или 404
    note = get_object_or_404(Note, id=note_id, user=request.user)

    # 2. Если отправили форму — сохраняем
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    # 3. Если просто открыли страницу — показываем форму
    else:
        form = NoteForm(instance=note)

    return render(request, 'note_form.html', {'form': form})
@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)

    if request.method == 'POST':
        note.delete()
        return redirect('dashboard')

    return render(request, 'note_confirm_delete.html', {'note': note})
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('dashboard')
    else:
        form = TaskForm()

    return render(request, 'task_form.html', {'form': form})
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)

    return render(request, 'task_form.html', {'form': form})
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('dashboard')

    return render(request, 'task_confirm_delete.html', {'task': task})


@login_required
def create_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()
            return redirect('dashboard')
    else:
        form = ReminderForm()

    return render(request, 'reminder_form.html', {'form': form})
@login_required
def edit_reminder(request, reminder_id):
    reminder = get_object_or_404(Reminder, id=reminder_id, user=request.user)

    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ReminderForm(instance=reminder)

    return render(request, 'reminder_form.html', {'form': form})
@login_required
def delete_reminder(request, reminder_id):
    reminder = get_object_or_404(Reminder, id=reminder_id, user=request.user)

    if request.method == 'POST':
        reminder.delete()
        return redirect('dashboard')

    return render(request, 'reminder_confirm_delete.html', {'task': reminder})