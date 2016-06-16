from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class Articles(models.Model):
    user_id         = models.ForeignKey(User, on_delete=models.CASCADE)
    date            = models.DateTimeField('Publication Date')
    article_text    = models.TextField()
    subject         = models.CharField(max_length=64)

    def __str__(self):
        return "%s %s..." % (self.user_id, self.article_text[:20])

    def preview(self):
        return "%s" % self.article_text[:200]

class Comments(models.Model):
    user_id         = models.ForeignKey(User, on_delete=models.CASCADE)
    art_id          = models.ForeignKey(Articles, on_delete=models.CASCADE)
    date            = models.DateTimeField('Comment Date')
    comment_text    = models.TextField()

class Ratings(models.Model):
    user_id         = models.ForeignKey(User, on_delete=models.CASCADE)
    art_id          = models.ForeignKey(Articles, on_delete=models.CASCADE)
    rating          = models.SmallIntegerField()
