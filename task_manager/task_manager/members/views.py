from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import CreateUserForm, UpdateUserForm
from django.contrib.auth import views as auth_views


class Register(CreateView):
    form_class = CreateUserForm
    template_name = 'registration/register.html'
    def get_success_url(self):
        return reverse_lazy('login')

class UpdateUserInfo(UpdateView):
    template_name = 'registration/update_profile.html'
    form_class = UpdateUserForm
    def get_success_url(self):
        return reverse_lazy('list_tasks')

    def get_object(self):
        return self.request.user

class ChangePassword(auth_views.PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('change_password_done')

def change_password_done(request):
    return render(request,'registration/change_password_done.html',{})
