from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=100)
    caption = models.CharField(max_length=1000)

    def __str__(self):
        return self.username