#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    View managing the clean feature of frontkeeper
"""
from django.conf import settings
from django.http import HttpResponseRedirect
from passkeeper import Passkeeper
import os
import logging


def init_logger():
    """ 
        Initialisation for logger
        Set the format of logger
        Create log file in log/
    """
    # Init logging level with debug stream handler
    log = logging.getLogger('passkeeper')
    log.setLevel(logging.INFO)
    # log.setLevel(logging.DEBUG)
    logformat = '%(asctime)s %(levelname)s -: %(message)s'
    # Set logger formater
    formatter = logging.Formatter(logformat)
    # File handler
    hdl = logging.FileHandler('log/%s.log' % __name__)
    hdl.setFormatter(formatter)
    log.addHandler(hdl)
    return log


def clean(request):
    """ 
        Clean all ini / raw files if status isn't encrypted
    """
    if not os.path.exists(settings.PASSKEEPER_ENCRYPT_STATE_FILE):
        f = open(settings.PASSKEEPER_ENCRYPT_STATE_FILE, 'w+')
        f.write("")
        f.close()
        init_logger()
        mypasskeeper = Passkeeper(directory=settings.PASSKEEPER_PATH)
        mypasskeeper.cleanup_ini(force_remove=True)
    return HttpResponseRedirect('/')
