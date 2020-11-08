# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Mood(models.Model):
    description = models.TextField(blank=False)
    mood = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return self.description
