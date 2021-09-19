from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    username = forms.TextInput()
    email = forms.CharField(required=True, widget=forms.EmailInput)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UpdateUserForm(UserChangeForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username','email','password']
