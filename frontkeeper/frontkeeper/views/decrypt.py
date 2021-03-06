#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    View for the decryption of passkeeper
"""
from django.conf import settings
from django.shortcuts import render
from passkeeper import Passkeeper
from .forms import PasswordForm
import os



#  decrypt
def decrypt(request):
    """
        Display the formular to decrypt passkeeper files
        Remove encryption lock file
    """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PasswordForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            mypasskeeper = Passkeeper(directory=settings.PASSKEEPER_PATH)
            decryption = mypasskeeper.decrypt(
                         passphrase=form.cleaned_data['password'])
            if decryption:
                os.remove(settings.PASSKEEPER_ENCRYPT_STATE_FILE)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PasswordForm()

    if os.path.exists(settings.PASSKEEPER_ENCRYPT_STATE_FILE):
        state = 'Encrypted, you can decrypt'
    else:
        state = 'Decrypted /!\/!\/!\ No need to do it again /!\/!\/!\ '
        return render(request, 'decrypt-disabled.html',
                      context={'form': form, 'state': state})
    return render(request, 'decrypt.html',
                  context={'form': form, 'state': state})
