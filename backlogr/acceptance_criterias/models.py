from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from stories.models import Story
# Create your models here.
class AcceptanceCriteria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    short_id = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    story = models.ForeignKey(Story)
    description = models.CharField(forms.CharField(widget=forms.Textarea, default=""))


    created_on = models.DateTimeField(auto_add_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u"Acceptance Criteria"
        verbose_name_plural = u"Acceptance Criterias"

    def __str__(self):
        return self.id + "-" + self.description

    def save(self, *args, **kwargs):
        super(AcceptanceCriteria, self).save(*args, **kwargs)
