#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    View managing the list of file in you passkeeper
"""
from django.conf import settings
from django.shortcuts import render
import logging
import os


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


def list(request):
    """
       Display list of ini / raw files
       Allow click on ini file to edit content
       Display a button to remove ini / raw files
    """
    if request.method == 'POST':
        os.remove(os.path.join(settings.PASSKEEPER_PATH,
                  request.POST['fileid']))
    files = []
    for fname in os.listdir(settings.PASSKEEPER_PATH):
        file_path = os.path.join(settings.PASSKEEPER_PATH, fname)
        if (fname.endswith('.ini') and os.path.isfile(file_path)):
            files.append(fname)
    filesraw = {}
    for fname in os.listdir(settings.PASSKEEPER_PATH):
        file_path = os.path.join(settings.PASSKEEPER_PATH, fname)
        if (fname.endswith('.raw') and os.path.isdir(file_path)):
            for f in os.listdir(file_path):
                filesraw[f] = {'path': file_path, 'name': f}
    the_title = "Front-keeper"
    if os.path.exists(settings.PASSKEEPER_ENCRYPT_STATE_FILE):
        state = 'Encrypted'
    else:
        state = 'Decrypted'
    return render(request, 'list.html',
                  context=({'the_title': the_title, 'request': request,
                            'files': files, 'filesraw': filesraw,
                            'state': state}))
