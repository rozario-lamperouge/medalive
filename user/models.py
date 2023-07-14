# admin_signup/models.py

from django.db import models

class Admin(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.username
