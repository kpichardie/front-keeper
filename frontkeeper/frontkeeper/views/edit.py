#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    View managing the edition of a password ini file
"""
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import EditForm
import os



def edit(request, filename):
    """
        Display the current info of the ini password file and allow edit
        Then you can save new content
    """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EditForm(request.POST)
        if form.is_valid():
            f = open(os.path.join(settings.PASSKEEPER_PATH, filename), 'w')
            f.write(form.cleaned_data['info'])
            f.close()
            return HttpResponseRedirect('/list/')

    # if a GET (or any other method) we'll create a blank form
    else:
        f = open(os.path.join(settings.PASSKEEPER_PATH, filename), 'r')
        content = f.read()
        f.close()
        content = {'info': content}
        form = EditForm(content)

    return render(request, 'edit.html', context=({'filename': filename,
                                                 'form': form}))
