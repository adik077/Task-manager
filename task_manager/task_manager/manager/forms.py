from django import forms
from .models import Task
from bootstrap_datepicker_plus import DateTimePickerInput

class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(label='',widget=DateTimePickerInput(attrs={'class': 'form-control','placeholder':'Deadline'}))
    body = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control','rows':3 ,'placeholder':'Task description...'}))
    class Meta:
        model = Task
        fields = ['deadline', 'body']
        order = ['deadline']




