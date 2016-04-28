
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from backlogs.models import Backlog
import uuid
# Create your models here.
class BacklogItem(models.Model):
    """
    A BacklogItem is either an epic, a user story or a non functional requirement.
    Every item has a integer id, a uuid for the visible part of the application and a short_id.
    The short_id is made out of the backlog name and the integer id, e.g. MYBACKLOG-12.

    Every Backlog Item refers to a user and a backog as foreign key.

    Every Backlog Item has the fields Who, What, Why to specify the user story.
    Every Backlog Item has the field accptance_criteria to specify those in markdown format
    Every item has a field to notes kept in markdown foemat

    Story Points and Business Value define the importance of an item.
    Based on these figures a rank is calculated.

    DateTimeFields track creation and update dates.

    Future Requirements: Items can be broken down in smaller items. and this history should be tracked.

    Todos:
    * Lets calculate the short id based on the short backlog name. Create the short backlog name identifier within the backlog
    """
    BACKLOG_ITEM_CHOICES = (
        ('user_story', 'user_story'),
        ('epic', 'epic'),
        ('non_functional_requirement', 'non_functional_requirement'),
    )
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, db_index=True)
    backlog = models.ForeignKey(Backlog, db_index=True)

    backlog_item_type = models.CharField(max_length=50, choices=BACKLOG_ITEM_CHOICES, default= BACKLOG_ITEM_CHOICES[0][0], db_index=True)

    who = models.CharField(max_length=255, blank=True)
    what = models.CharField(max_length=255, blank=True)
    why = models.CharField(max_length=255, blank=True)

    acceptance_criteria = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    story_points = models.IntegerField(null=True, blank=True)
    business_value = models.IntegerField(null=True, blank=True)

    #rank default should be the first
    """
    As a pm I want to rerank my cards in the backlog list view
    Every item should be added to the bottom of the list!

    On rearranging the ranks of all instances have to be updated and saved to the database -> DONE
    Within a backlog list the rank must be unique
    """
    list_ui_rank = models.PositiveIntegerField(default=0)

    """
    Used for breakdown of backlog items
    """
    parent_uuid = models.CharField(max_length=255, blank=True)
    is_archive = models.BooleanField(default=True)

    #prio

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u"Backlog Item"
        verbose_name_plural = u"Backlog Items"

    def __str__(self):
        return str(self.id) + "-" + self.backlog_item_type

    def get_user_story(self):
        return "As a " + self.who + " I'd like to " + self.what + ", so that " + self.why + "."

    def make_short_id(self):
        return self.backlog.name.upper() + "-" + str(self.id)

    def save(self, *args, **kwargs):
        if not self.pk:
            #Get the highest UI Rank and assign the new item to the board
            #If no objects exist assign 0
            bi = BacklogItem.objects.filter(backlog=self.backlog)
            print "CREATED"
            print len(bi)
            self.list_ui_rank = len(bi)
        self.short_id = self.make_short_id()
        super(BacklogItem, self).save(*args, **kwargs)
