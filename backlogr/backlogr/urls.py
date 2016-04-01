"""backlogr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from backlogs.views import BacklogListView, BacklogDetailView
from backlog_items.views import BacklogItemCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #Auth Views
    #url(r'^accounts/login/$', auth_views.login),
    url('^', include('django.contrib.auth.urls')),

    #Backlog Views
    url(r'^backlogs/$',
        BacklogListView.as_view(),
        name="backlog_list_view"),

    url(r'^backlogs/(?P<uuid>[^/]+)/$',
      BacklogDetailView.as_view(),
      name="backlog_detail_view"),

    #Backlog Item Views
    url(r'^backlog_items/create/(?P<backlog_uuid>[^/]+)/$',
      BacklogItemCreateView.as_view(),
      name="backlog_item_create_view"),

]

"""
^login/$ [name='login']
^logout/$ [name='logout']
^password_change/$ [name='password_change']
^password_change/done/$ [name='password_change_done']
^password_reset/$ [name='password_reset']
^password_reset/done/$ [name='password_reset_done']
^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
^reset/done/$ [name='password_reset_complete']
"""
