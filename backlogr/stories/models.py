"""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from backlogs.models import Backlog
from epics.model import Epic
# Create your models here.
class Story(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    short_id = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    project = models.ForeignKey(Backlog)
    epic = models.ForeignKey(Epic, blank=True, null=True)
    description = models.CharField(forms.CharField(widget=forms.Textarea, default=""))
    story points = models.IntegerField(null=True, blank=True)
    business_value = models.IntegerField(null=True, blank=True)

    created_on = models.DateTimeField(auto_add_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u"Story"
        verbose_name_plural = u"Stories"

    def __str__(self):
        return self.id + "-" #+ self.name

    def save(self, *args, **kwargs):
        super(Story, self).save(*args, **kwargs)
"""
