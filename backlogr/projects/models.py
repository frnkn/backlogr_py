from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User)
    name = models.CharField(max_length=250)
    description = models.CharField(forms.CharField(widget=forms.Textarea, default=""))
    created_on = models.DateTimeField(auto_add_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u"Project"
        verbose_name_plural = u"Projects"

    def __str__(self):
        return self.id + "-" + self.name

    def save(self, *args, **kwargs):
        super(Project, self).save(*args, **kwargs)
