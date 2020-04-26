from django.db import models
from django.contrib.auth.models import User
from datetime import date, time, datetime, timedelta


class TaskUser(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    comment = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class ArchivedTodo(models.Model):
    TASK_STATUS = [
        ('OP', 'Open'),
        ('IP', 'In progress'),
        ('DN', 'Done'),
    ]
    task = models.CharField(max_length=200, null=False, blank=False)
    status = models.CharField(max_length=2, choices=TASK_STATUS, default='OP', null=False, blank=False)
    task_owner = models.ForeignKey(TaskUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    date_closed = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.task

    @property
    def diff_date(self):
        d = self.date_closed
        now = self.date_created
        d1 = date(now.year, now.month, now.day)
        d2 = date(d.year, d.month, d.day)
        t = abs(d2 - d1).days
        return t

    @property
    def diff_time(self):
        d = self.date_closed
        now = self.date_created
        d1 = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        d2 = str(d.hour) + ":" + str(d.minute) + ":" + str(d.second)
        FMT = '%H:%M:%S'
        tdelta = datetime.strptime(d1, FMT) - datetime.strptime(d2, FMT)
        return tdelta


class Todo(models.Model):
    TASK_STATUS = [
        ('OP', 'Open'),
        ('IP', 'In progress'),
        ('DN', 'Done'),
    ]
    task = models.CharField(max_length=200, null=False, blank=False)
    status = models.CharField(max_length=2, choices=TASK_STATUS, default='OP', null=False, blank=False)
    task_owner = models.ForeignKey(TaskUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)
    date_closed = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.task

    @property
    def is_from_today(self):
        # ---- Check if todo was entered today
        return date.today() == self.date_created.date()

    @property
    def diff_date(self):
        """
        "  Purpose    : Calculate duration in days
        "  Parameters : 
        "  returns    : Day delta
        """
        d = self.date_closed
        now = self.date_created
        d1 = date(now.year, now.month, now.day)
        d2 = date(d.year, d.month, d.day)
        t = abs(d2 - d1).days
        return t

    @property
    def diff_time(self):
        """
        "  Purpose    : Returns the elapsed time between creation and completion
        "  Parameters :  
        "  returns    : Time delta
        """
        d = self.date_closed
        now = self.date_created
        d1 = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        d2 = str(d.hour) + ":" + str(d.minute) + ":" + str(d.second)
        FMT = '%H:%M:%S'
        tdelta = datetime.strptime(d1, FMT) - datetime.strptime(d2, FMT)
        return tdelta

    @property
    def is_afew_momentsago(self):
        # ---- Selfmade function to check if a new record
        # ---- was recently added (within 3 minutes)
        d1 = self.date_created + timedelta(minutes=3)
        # Need to convert the date formats to ISO format!
        d1 = d1.isoformat()
        d2 = datetime.now().isoformat()
        if d2 > d1:
            return False
        else:
            return True
