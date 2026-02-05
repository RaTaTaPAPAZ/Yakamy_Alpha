from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', views.dashboard, name='dashboard'),

    path('notes/create/', views.create_note, name='create_note'),

    path('notes/<int:note_id>/edit/', views.edit_note, name='edit_note'),

    path('notes/<int:note_id>/delete/', views.delete_note, name='delete_note'),

    path('tasks/create/', views.create_task, name='create_task'),

    path('tasks/<int:task_id>/edit/', views.edit_task, name='edit_task'),

    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),

    path('reminders/create/', views.create_reminder, name='create_reminder'),

    path('reminders/<int:reminder_id>/edit/', views.edit_reminder, name='edit_reminder'),

    path('reminders/<int:reminder_id>/delete/', views.delete_reminder, name='delete_reminder'),

    path('mcp/', views.mcp_create, name='mcp_create'),

    path("mcp/clarify/", views.mcp_clarify, name="mcp_clarify"),

]
