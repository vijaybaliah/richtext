# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.db import models

# Create your models here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
