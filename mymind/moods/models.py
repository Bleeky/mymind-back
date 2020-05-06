# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Mood(models.Model):
    description = models.TextField(blank=True)

    def __str__(self):
        return self.description