from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from models import Backlog
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from backlog_items.models import BacklogItem
import logging

logger = logging.getLogger('backlogr')

# Create your views here.
class BacklogListView(LoginRequiredMixin, View):

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        """
        @STORY: As a product manager I want to get a list of all my private backlogs, so that I can access them on a dedicated page.
        @ACCEPTANCE_CRITERIA:
        * User must be logged in to get a list of all backlogs
        * The template gets a list of all backlogs related to the user and sorts them by updated date ascending.
        * Every backlog item links to the backlog detail view that lists all
        user stories, etc. of the related backlog.
        * If no backlogs exist yet, the product manager gets a message to create
        his first backlog.
        """
        username = None
        if request.user.is_authenticated():
            username = request.user.username
        user = User.objects.get(username=username) #Fix that

        backlogs = Backlog.objects.filter(user=user).order_by('-updated_on')

        return render_to_response('backlogs/backlog_list_view.html',
                                    {'backlogs': backlogs},
                                    context_instance=RequestContext(request))

class BacklogDetailView(LoginRequiredMixin, View):

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        """
        @STORY: As a product manager I want to get a list of all user stories, epics and functional requirements related to a backlog, so that the backlog items can be resorted, updated and created, etc.
        @ACCEPTANCE_CRITERIA:
        * User must be logged in to get the list of his private backlog items on this page
        * The view can be sorted by different settings
        * Each backlog item in the list links to a detail/update view.
        * The user can create a new backlog item rom this list.
        """
        username = None
        if request.user.is_authenticated():
            username = request.user.username

        user = User.objects.get(username=username)

        backlog_items = BacklogItem.objects.filter(user=user).filter(backlog__uuid=kwargs['uuid'])

        return render_to_response('backlogs/backlog_detail_view.html',
                            {'backlog_items': backlog_items,
                            'backlog_uuid': kwargs['uuid']},
                            context_instance=RequestContext(request))
