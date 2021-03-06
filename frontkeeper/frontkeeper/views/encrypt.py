#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    View managing the encryption in passkerper
"""
from django.conf import settings
from django.shortcuts import render
from .forms import PasswordForm
from passkeeper import Passkeeper
import os



def encrypt(request):
    """
        Encrypt all files and write lock encryption file
    """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PasswordForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            mypasskeeper = Passkeeper(directory=settings.PASSKEEPER_PATH)
            mypasskeeper.encrypt(
                                 commit_message="Update encrypted files through \
frontkeeper",
                                 passphrase=form.cleaned_data['password'])
            mypasskeeper.cleanup()
            f = open(settings.PASSKEEPER_ENCRYPT_STATE_FILE, 'w+')
            f.write("")
            f.close()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PasswordForm()

    if os.path.exists(settings.PASSKEEPER_ENCRYPT_STATE_FILE):
        state = 'Encrypted /!\/!\/!\ It\'s already encrypted /!\/!\/!\ '
        return render(request, 'encrypt-disabled.html',
                      context={'form': form, 'state': state})
    else:
        state = 'Decrypted, you can encrypt'
    return render(request, 'encrypt.html',
                  context={'form': form, 'state': state})
