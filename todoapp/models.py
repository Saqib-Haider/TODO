from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    create_time = models.DateTimeField(default=timezone.now)
    complete_time = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title




