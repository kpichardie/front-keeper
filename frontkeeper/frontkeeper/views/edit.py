from django.conf import settings
from django.template import Context, loader
from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import EditForm

import logging
import os

from passkeeper import *

def init_logger():
       # Init logging level with debug stream handler
       log = logging.getLogger('passkeeper')
       log.setLevel(logging.INFO)
       #log.setLevel(logging.DEBUG)
       logformat =  '%(asctime)s %(levelname)s -: %(message)s'
       # Set logger formater
       formatter = logging.Formatter(logformat)
       # Stream handler
       #hdl = logging.StreamHandler()
       #hdl.setFormatter(formatter)
       #log.addHandler(hdl)
       ## File handler
       hdl = logging.FileHandler('log/%s.log' % __name__)
       hdl.setFormatter(formatter)
       log.addHandler(hdl)
       return log



#  flush
def edit(request, filename):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EditForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            log = init_logger()
            print filename
            f = open(os.path.join(settings.PASSKEEPERPATH, filename), 'w')
            f.write(form.cleaned_data['info'])
            f.close()
            #fd = os.open(os.path.join(passkeeperpath, filename), os.O_WRONLY)
            #os.write(fd, form.cleaned_data['info'])
            #os.close(fd)
            return HttpResponseRedirect('/list/')

    # if a GET (or any other method) we'll create a blank form
    else:
        f = open(os.path.join(settings.PASSKEEPERPATH, filename), 'r')
        content = f.read()
        f.close()
        #fd = os.open(os.path.join(passkeeperpath, filename), os.O_RDONLY)
        #content = os.read(fd, 99999999)
        #content = {'info': content}
        #os.close(fd)
        content = {'info': content}
        #os.close(fd)
        form = EditForm(content)

    return render(request, 'edit.html', context=({'filename': filename, 'form': form}))
