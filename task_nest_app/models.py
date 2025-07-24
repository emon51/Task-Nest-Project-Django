from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Todo_model(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 