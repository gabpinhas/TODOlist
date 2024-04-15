from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    task_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=150, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
