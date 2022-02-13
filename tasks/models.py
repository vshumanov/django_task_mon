from django.db import models


class Task(models.Model):
    name = models.TextField(max_length=255)
    is_done = models.BooleanField(default=False)
