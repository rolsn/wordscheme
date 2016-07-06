from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class Articles(models.Model):
    user_id         = models.ForeignKey(User, on_delete=models.CASCADE)
    date            = models.DateTimeField('Publication Date')
    article_text    = models.TextField()
    subject         = models.CharField(max_length=64)
    urlname         = models.CharField(max_length=48)

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

class UserRelationships(models.Model):
    class Meta:
        unique_together = (('follower_id', 'following_id'),)

    follower_id     = models.ForeignKey(User, on_delete=models.CASCADE)
    following_id    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    date            = models.DateTimeField('Started following on')
    relation_type   = models.SmallIntegerField('Following or blocking')

