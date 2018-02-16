# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.models import *
# Register your models here.
admin.site.register(RiskField)
admin.site.register(RiskType)
admin.site.register(Risk)