#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    View managing the flush feature of passkeeper
"""
from django.conf import settings
from django.shortcuts import render
from .forms import EmptyForm
import logging
from passkeeper import Passkeeper


#  flush
def flush(request):
    """
        Flush all log and git history
        To have more security
    """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubmitForm(request.POST)
        mypasskeeper = Passkeeper(directory=settings.PASSKEEPER_PATH)
        with open("log/frontkeeper.views.flush.log", "w"):
            pass
        mypasskeeper.flush_history()
        with open("log/frontkeeper.views.decrypt.log", "w"):
            pass
        with open("log/frontkeeper.views.edit.log", "w"):
            pass
        with open("log/frontkeeper.views.encrypt.log", "w"):
            pass
        with open("log/frontkeeper.views.new.log", "w"):
            pass
        with open("log/frontkeeper.views.init.log", "w"):
            pass

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmptyForm()
    if os.path.exists(settings.PASSKEEPER_ENCRYPT_STATE_FILE):
        state = 'Encrypted'
    else:
        state = 'Decrypted /!\/!\/!\  Don\'t forget to encrypt \
before leaving /!\/!\/!\ '
    return render(request, 'flush.html',
                  context={'form': form, 'state': state})
