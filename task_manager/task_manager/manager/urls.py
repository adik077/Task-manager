from django.urls import path
from .views import CreateShowTasks, EditTask, remove_task, complete_task

urlpatterns = [
    path('',CreateShowTasks.as_view(), name='list_tasks'),
    path('remove_task/<int:pk>/', remove_task, name='remove_task'),
    path('complete_task/<int:pk>/', complete_task, name='complete_task'),
    path('edit_task/<int:pk>/', EditTask.as_view(), name='edit_task'),
]
