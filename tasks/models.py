# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Tasks(models.Model):
    """
    Model to store info about tasks
    """
    FIELDS_CHARACTER_LIMIT = {
        'TITLE': 35,
        'CONTENT': 255,
    }

    title = models.CharField(max_length=FIELDS_CHARACTER_LIMIT['TITLE'], blank=True, null=True)
    content = models.CharField(max_length=FIELDS_CHARACTER_LIMIT['CONTENT'], blank=True, null=True)
    owner = models.ForeignKey(get_user_model(), help_text='Owner of this task')

    def __unicode__(self):
        return '{}:{}'.format(self.owner, self.title)