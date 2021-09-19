from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    body = models.TextField(max_length=300)

    def get_absolute_url(self):
        return reverse('list_tasks')

    def __str__(self):
        if len(self.body)>30:
            body_desc=self.body[0:30]
        else:
            body_desc=self.body
        return str(self.author)+" | "+body_desc+"..."

