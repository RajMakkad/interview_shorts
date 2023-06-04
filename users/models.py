from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='defaul.jpeg', upload_to='profile_pictures')
    branch = models.CharField(max_length=100, default='Branch')

    def __str__(self):
        return f'{self.user.username} Profile.'
