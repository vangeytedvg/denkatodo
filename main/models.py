from django.db import models
from django.contrib.auth.models import User


class TaskUser(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    comment = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


# Create your models here.
class Todo(models.Model):
    TASK_STATUS = [
        ('OP', 'Open'),
        ('IP', 'In progress'),
        ('DN', 'Done'),
    ]
    task = models.CharField(max_length=200, null=False, blank=False)
    status = models.CharField(max_length=2, choices=TASK_STATUS, default='OP', null=False, blank=False)
    task_owner = models.ForeignKey(TaskUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.task
