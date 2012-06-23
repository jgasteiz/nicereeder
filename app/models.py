# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):
    name = models.CharField(max_length=100, blank=False)
    url = models.URLField(blank=False, verify_exists=True, max_length=200)
    user = models.ForeignKey(User)
    class Meta:
        ordering = ['name']
    def __unicode__(self):
        return unicode(self.name)

class Link(models.Model):
    name = models.CharField(max_length=100, blank=False)
    domain = models.TextField(blank=False)
    url = models.URLField(blank=False, verify_exists=True, max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    class Meta:
        ordering = ['-created']
    def __unicode__(self):
        return unicode(self.name)