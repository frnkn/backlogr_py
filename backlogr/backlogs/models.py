from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.
class Backlog(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    short_id = models.CharField(max_length=10)
     #forms.CharField(widget=forms.Textarea, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u"Backlog"
        verbose_name_plural = u"Backlogs"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Backlog, self).save(*args, **kwargs)
