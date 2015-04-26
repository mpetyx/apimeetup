__author__ = 'mpetyx'

from django.db import models

class Task(models.Model):
    title = models.TextField()