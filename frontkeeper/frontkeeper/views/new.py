# -*- coding: utf-8 -*-

"""
    View managing the creation of new ini / raw files
"""
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NewForm
from .forms import EmptyForm
import os


def new(request):
    """ 
        Display the newform to create new ini / raw file
        A checkbox allow to check if it's a raw file
    """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewForm(request.POST)
        if form.is_valid():
            filepath = os.path.join(settings.PASSKEEPER_PATH,
                                    form.cleaned_data['filename'])
            filetype = form.cleaned_data['rawfile']
            if filetype == "True":
                rawfullpath = os.path.join(settings.PASSKEEPER_PATH,
                                           "default.raw",
                                           form.cleaned_data['filename'])
                if os.path.exists(rawfullpath):
                    print "raw file already exist"
                    return render(request, 'new.html', {'form': form})

                f = open(rawfullpath, 'w+')
                f.write(form.cleaned_data['info'])
                f.close()
                return HttpResponseRedirect('/list/')
            else:
                if os.path.exists(filepath + str('.ini')):
                    print "ini file already exist"
                    return render(request, 'new.html', {'form': form})
                f = open(filepath + str('.ini'), 'w+')
                f.write(form.cleaned_data['info'])
                f.close()
                return HttpResponseRedirect('/list/')
    # if a GET (or any other method) we'll create a blank form
    else:
        if os.path.exists(settings.PASSKEEPER_ENCRYPT_STATE_FILE):
            form = EmptyForm()
            return render(request, 'new-disabled.html', {'form': form})
        else:
            form = NewForm()
            return render(request, 'new.html', {'form': form})
    return render(request, 'new.html', {'form': form})
