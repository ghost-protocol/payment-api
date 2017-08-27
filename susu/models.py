# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models

# Create your models here.
# .customer_name
# .account_number
# .phone_number
# .
# .customer data
# .customer passbook
class Client(models.Model):
    lastName = models.CharField(max_length=100, blank=False)
    firstName = models.CharField(max_length=100, blank=False)
    otherName = models.CharField(max_length=100, blank=True)
    phoneNumber = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s %s" % (self.lastName, self.firstName)

class Account(models.Model):
    client = models.ForeignKey(Client)
    number = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s %s" % (self.client, self.number)

class Payment(models.Model):
    client = models.ForeignKey(Client)
    amount = models.FloatField(max_length=30, default=0.00)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return "%s %s" % (self.client, self.amount)




