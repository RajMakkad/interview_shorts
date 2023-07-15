from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# imported User from auth model for author field.
class Short(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    experience = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    difficulty = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    ctc = models.TextField(default='50k')
    offer = models.CharField(max_length=100, default='Accepted')
    
    # This function is used to specify how the table rows are gonna look from the outside.
    def __str__(self):
        return self.title