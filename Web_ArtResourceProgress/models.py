#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.db import connection

class Designers(models.Model):

    id = models.IntegerField(primary_key= True)
    popo_mail = models.CharField(max_length= 40)
    nickname = models.CharField(max_length= 40)
    
    class Meta:
        db_table = 'designers'

class ResourcesDetails(models.Model):
    
    date = models.DateTimeField()
    designer = models.CharField(max_length= 40)
    initiator = models.CharField(max_length= 40)
    content = models.TextField()

    class Meta:
        db_table = 'artresourceprogress'
        