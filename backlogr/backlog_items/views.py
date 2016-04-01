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
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from uuid import UUID

# Create your views here.
"""
## Backlog Item Requirements

* As a pm I'd like to create a backog item via a form on a single page.

* As a pm I'd like to create a backlog item via a form in a modal.

## Non functional requirements
* User sees all form fields except User and backlog field
* For the single create view the user gets redirected to the referring backlog
* For the modal view from the backlog view, the whole creation story should work via ajax.
** The user creates the item, the model closes, the backlog list gets updated.
** In an advanced step anagular or similar should do the job
"""

class BacklogItemCreateView(LoginRequiredMixin, CreateView):
    model = BacklogItem
    fields = ['backlog_item_type', 'who', 'what', 'why', 'acceptance_criteria', 'notes', 'story_points', 'business_value']

    template_name = "backlog_items/backlog_item_create_view.html"
    #http://localhost:8000/backlog_items/create/47c11d38-cd95-4d63-86fd-612d4c88f106/
    success_url = reverse_lazy('backlog_detail_view')
    def dispatch(self, *args, **kwargs):
        try:
            val = UUID(kwargs['backlog_uuid'], version=4)
        except ValueError:
            # If it's a value error, then the string
            # is not a valid hex code for a UUID.
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
