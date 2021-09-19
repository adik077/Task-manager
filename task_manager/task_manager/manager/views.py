from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from .models import Task
from .forms import TaskForm
from datetime import datetime,timezone
from django.http import HttpResponseRedirect


class CreateShowTasks(CreateView):
    form_class = TaskForm
    template_name = 'all_tasks.html'
    reverse_lazy('list_tasks')

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.all()

        ### Returning sorted by deadline tasks ###
        safe_tasks = []
        to_do_now_tasks=[]
        time_exceeded_tasks = []
        done_tasks = []
        for task in tasks:
            if self.request.user.id == task.author.id:
                if task.is_active:
                    if (task.deadline - datetime.now(timezone.utc)).total_seconds()>=86400:
                        safe_tasks.append(task)
                    elif 0<=(task.deadline - datetime.now(timezone.utc)).total_seconds()<86400:
                        to_do_now_tasks.append(task)
                    elif (task.deadline - datetime.now(timezone.utc)).total_seconds()<0:
                        time_exceeded_tasks.append(task)
                else:
                    done_tasks.append(task)

        #context["tasks"] = tasks
        context["safe_tasks"] = sorted(safe_tasks,key=lambda x: x.deadline)
        context["to_do_now_tasks"] = sorted(to_do_now_tasks,key=lambda x: x.deadline)
        context["time_exceeded_tasks"] = sorted(time_exceeded_tasks,key=lambda x: x.deadline)
        context["done_tasks"] = sorted(done_tasks, key=lambda x: x.deadline)
        return context

class EditTask(UpdateView):
    form_class = TaskForm
    model = Task
    template_name = 'edit_task.html'
    reverse_lazy('list_tasks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task,pk=self.kwargs["pk"])
        context["task_creator"] = task.author.id
        return context


def remove_task(request,pk):
    task = get_object_or_404(Task, pk=pk)
    if request.user.id == task.author.id:
        task.delete()
    return HttpResponseRedirect(reverse_lazy('list_tasks'))

def complete_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    if task.is_active == True:
        task.is_active = False
    else:
        task.is_active = True
    task.save()
    return HttpResponseRedirect(reverse_lazy('list_tasks'))
