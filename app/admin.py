# -*- coding: utf-8 -*-
from django.contrib import admin
from app.models import Subscription, Link

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'user')

admin.site.register(Subscription, SubscriptionAdmin)

class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'user', 'created')

admin.site.register(Link, LinkAdmin)