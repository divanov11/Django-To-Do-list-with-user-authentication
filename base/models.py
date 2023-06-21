from django.db import models
from django.contrib.auth.models import User



# model named "Task" that represents tasks that can be created and managed. The model has the following fields:

class Task(models.Model):
    user = models.ForeignKey(
    User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'
