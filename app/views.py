# -*- coding: utf-8 -*-
import feedparser
from app.models import Subscription
from django.utils import simplejson
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView, View

class SubscriptionListView(ListView):
	"""
	Loads subscriptions
	"""
	template_name='subscription_list.html'
	model=Subscription
	context_object_name='subscription_list'
	def get_queryset(self):
		if self.request.user.is_authenticated():
			return Subscription.objects.filter(user=self.request.user)
		else:
			return Subscription.objects.order_by('?')[:5]
	def get_context_data(self, **kwargs):
		context = super(SubscriptionListView, self).get_context_data(**kwargs)
		# context.update({'user': self.request.user})
		return context

class EntryListResponseView(View):
	"""
	Loads a subscription entries
	"""
	def post(self, request, *args, **kwargs):
		id = int(request.POST['id_rss'])
		subscription = Subscription.objects.filter(id=id)[0]
		feed = feedparser.parse(subscription.url)
		entries_list = []
		for entry in feed.entries:
			if "content" in entry:
				body = entry["content"][0]["value"]
			else:
				# FIXME
				# little hack: some feeds goes with summary instead content
				body = entry["summary"]
			link = entry["link"]
			# FIXME
			# Gets an error on ubuntu :S
			# date = entry["date"]
			date = ""
			entries_list.append({	
				'name': subscription.name, 
				'title': entry["title"], 
				'url': link, 
				'body': body, 
				'date': date})
		return HttpResponse(simplejson.dumps(entries_list), mimetype='application/json')




