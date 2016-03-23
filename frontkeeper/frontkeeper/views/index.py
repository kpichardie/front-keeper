#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    View for the home of frontkeeper
"""
from django.template import Context, loader
from django.http import HttpResponse
from django.conf import settings
import os


def index(request):
    """
        Display home page
    """
    the_title = "Frontkeeper Home"
    t = loader.get_template('index.html')
    if os.path.exists(settings.PASSKEEPER_ENCRYPT_STATE_FILE):
        state = 'Encrypted, you can decrypt to access password'
    else:
        state = 'Decrypted /!\/!\/!\  Don\'t forget to encrypt before \
leaving /!\/!\/!\ '
    c = Context({
        'the_title': the_title,
        'request': request,
        'state': state,
    })

    return HttpResponse(t.render(c))
