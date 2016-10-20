#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    View managing the clean feature of frontkeeper
"""
from django.conf import settings
from django.http import HttpResponseRedirect
from passkeeper import Passkeeper
import os


def clean(request):
    """ 
        Clean all ini / raw files if status isn't encrypted
    """
    if not os.path.exists(settings.PASSKEEPER_ENCRYPT_STATE_FILE):
        f = open(settings.PASSKEEPER_ENCRYPT_STATE_FILE, 'w+')
        f.write("")
        f.close()
        mypasskeeper = Passkeeper(directory=settings.PASSKEEPER_PATH)
        mypasskeeper.cleanup_ini(force_remove=True)
    return HttpResponseRedirect('/')
