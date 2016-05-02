from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, Http404
from backlogs.models import Backlog
from models import BacklogItem
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from backlog_items.models import BacklogItem
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from uuid import UUID
import logging
from django.contrib.messages.views import SuccessMessageMixin

logger = logging.getLogger('backlogr')

# Create your views here.
"""
## Backlog Item Requirements

* As a pm I'd like to create a backog item via a form on a single page. -->DONE

* As a pm I'd like to create a backlog item via a form in a modal.

* As a pm I'd like to breakdown a backlog item into smaller backlog items and keeping its parent relation

* As a pm I'd like to update a backlog item via a form on a single page. --> DONE

* As a pm I'd like to update an item via a form in a modal.

## Non functional requirements
* User sees all form fields except User and backlog field -> DONE
* For the single create view the user gets redirected to the referring backlog -> DONE
* For the modal view from the backlog view, the whole creation story should work via ajax.
** The user creates the item, the model closes, the backlog list gets updated.
** In an advanced step anagular or similar should do the job

* Certain events have to be logged such as exceptions as they could be security relevant. -> DONE
"""
class BacklogItemUpdateAjaxView(LoginRequiredMixin, UpdateView):
    pass


class BacklogItemBreakDownView(LoginRequiredMixin, CreateView):
    """
    As a pm I'd like to breakdown a backlog item into smaller backlog items and keeping its parent relation
    """
    model = BacklogItem
    template_name = 'backlog_items/backlog_item_breakdown_view.html'
    fields = ['backlog_item_type', 'who', 'what', 'why', 'acceptance_criteria', 'notes', 'story_points', 'business_value']
    success_message = "Your backlog item was broken down successfully"

    def dispatch(self, *args, **kwargs):
        try:
            val = UUID(kwargs['backlog_uuid'], version=4)
        except ValueError:
            # If it's a value error, then the string
            # is not a valid hex code for a UUID.
            logger.error("An error occurred while breaking down backlog item: %s" % e)
            raise Http404

        self.backlog = get_object_or_404(Backlog, uuid=kwargs['backlog_uuid'])
        logger.debug("BRoke DOwn")
        self.parent_uuid = kwargs['parent_uuid']
        return super(BacklogItemBreakDownView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('backlog_detail_view', kwargs={'uuid': self.backlog.uuid})

    def form_valid(self, form):

        #user = self.request.user
        backlog_item = form.save(commit=False)
        backlog_item.backlog = self.backlog
        backlog_item.user = self.request.user
        backlog_item.parent_uuid = self.parent_uuid

        return super(BacklogItemBreakDownView, self).form_valid(form)


class BacklogItemUpdateView(LoginRequiredMixin, UpdateView):
    """
    As a pm I'd like to update a backlog item via a form on a single page
    """
    model = BacklogItem
    template_name = 'backlog_items/backlog_item_update_view.html'
    fields = ['backlog_item_type', 'who', 'what', 'why', 'acceptance_criteria', 'notes', 'story_points', 'business_value', 'is_archive']

    def get_object(self, queryset=None):
        try:
            val = UUID(self.kwargs['backlog_item_uuid'], version=4)
        except ValueError as e:
            # If it's a value error, then the string
            # is not a valid hex code for a UUID.
            logger.error("An error occurred while updating a backlog item: %s" % e)
            raise Http404
        obj = get_object_or_404(BacklogItem, uuid=self.kwargs['backlog_item_uuid'])
        self.obj_for_redirect = obj
        return obj

    def get_success_url(self):
        return reverse('backlog_detail_view', kwargs={'uuid': self.obj_for_redirect.backlog.uuid})

class BacklogItemCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    As a pm I'd like to create a backog item via a form on a single page.
    """
    model = BacklogItem
    fields = ['backlog_item_type', 'who', 'what', 'why', 'acceptance_criteria', 'notes', 'story_points', 'business_value']
    template_name = "backlog_items/backlog_item_create_view.html"
    success_message = "Your backlog item was created successfully"
    def dispatch(self, *args, **kwargs):
        try:
            val = UUID(kwargs['backlog_uuid'], version=4)
        except ValueError:
            # If it's a value error, then the string
            # is not a valid hex code for a UUID.
            logger.error("An error occurred while creating backlog item: %s" % e)
            raise Http404

        self.backlog = get_object_or_404(Backlog, uuid=kwargs['backlog_uuid'])
        return super(BacklogItemCreateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('backlog_detail_view', kwargs={'uuid': self.backlog.uuid})

    def form_valid(self, form):

        #user = self.request.user
        backlog_item = form.save(commit=False)
        backlog_item.backlog = self.backlog
        backlog_item.user=self.request.user

        return super(BacklogItemCreateView, self).form_valid(form)
