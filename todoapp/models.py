from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    STATUS = [
        ("PENDING", "Pending"),
        ("COMPLETE", "Complete"),
        ("EXPIRED", "Expired"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todo_user")
    tasks = models.CharField(max_length=100)
    status = models.CharField(max_length=10,choices=STATUS,default="PENDING")
    deadline = models.DateField(blank=True, null=True, default=None)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.tasks

