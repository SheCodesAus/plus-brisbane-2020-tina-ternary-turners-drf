from django.db import models
from django.contrib.auth import get_user_model

from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from datetime import datetime, timedelta 
from django.utils import timezone



# Create your models here.
class Bucket(models.Model):
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField(default = timezone.now)
    is_open = models.BooleanField(default = True)
    source_bsb_number = models.IntegerField()
    source_account_number = models.IntegerField()
    source_account_name = models.TextField()
    source_balance = models.IntegerField()
    owner = models.CharField(max_length=200)
    #owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='owner_buckets')

    def __str__(self):
        return self.title

class Pipe(models.Model):
    pipe_name = models.CharField(max_length=200)
    dest_bsb_number =  models.IntegerField()
    dest_account_number = models.IntegerField()
    dest_account_name = models.TextField()
    dest_balance = models.IntegerField()
    amount_dollar = models.IntegerField()
    amount_percent = models.IntegerField() 
    statement_text = models.CharField(max_length=200,default='Text')
   
    bucket = models.ForeignKey(
    'Bucket',
    on_delete=models.CASCADE,
    related_name='pipes'
    )
    # supporter = models.CharField(max_length=200)
    #destination is like supporter
    destination = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    related_name='destination_pipes'
    )