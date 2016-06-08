from __future__ import unicode_literals

from django.db import models

from users.models import Users

class Articles(models.Model):
    user_id         = models.ForeignKey(Users, on_delete=models.CASCADE)
    date            = models.DateTimeField('Publication Date')
    article_text    = models.TextField()
    subject         = models.CharField(max_length=64)
