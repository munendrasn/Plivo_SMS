# -*- coding: utf-8 -*-

from django.db import models

class SendSMS(models.Model):
    to_number = models.CharField(max_length=30)
    from_number = models.CharField(max_length=30)
    sms_sid = models.CharField(max_length=34, default="", blank=True)
    account_sid = models.CharField(max_length=34, default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default="", blank=True)
    body = models.TextField(max_length=140, default="")
