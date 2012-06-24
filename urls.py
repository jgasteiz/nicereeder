# -*- coding: utf-8 -*-
from django.contrib import admin
admin.autodiscover()
from app.models import Subscription
from django.views.generic.base import RedirectView, TemplateView
from django.conf.urls.defaults import patterns, include, url
from app.views import SubscriptionListView, EntryListView, EntryListResponseView

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	# Users
	url(r'^login/?', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}),
	url(r'^logout/?', 'django.contrib.auth.views.logout', {'template_name': 'users/logout.html'}),
	url(r'^register/?',
		TemplateView.as_view(
			template_name='users/register.html')),
	
	# Subscriptions
	url(r'^$', 
		SubscriptionListView.as_view(),
		name='home'),
	url(r'subscription/(?P<slug>[\w-]+)/$',
		EntryListView.as_view(),
		name='subscription'),

	# Ajax
	url(r'_ajax/load_rss/', 
		EntryListResponseView.as_view(), 
		name='load_rss'),
)
