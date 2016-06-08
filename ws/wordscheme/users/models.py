from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
    username    = models.CharField(max_length=32, unique=True)
    password    = models.CharField(max_length=64)
    reg_date    = models.DateTimeField('Registration Date')
    email       = models.EmailField(unique=True)

    def __str__(self):
        return self.username
