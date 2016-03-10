from django.conf import settings
from django.template import Context, loader
from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NewForm

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
def new(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            log = init_logger()
            filepath = os.path.join(settings.PASSKEEPER_PATH, form.cleaned_data['filename'])
            filetype = form.cleaned_data['rawfile']
            if filetype:
                rawfullpath = os_join(settings.PASSKEEPER_PATH, "default.raw",form.cleaned_data['filename'])
                if os.path.exists(rawfullpath):
                     print "file already exist"
                     return render(request, 'new.html', {'form': form})

                f = open(rawfullpath, 'w+')
                f.write(form.cleaned_data['info'])
                f.close()
            else:
                if os.path.exists(filepath + str('.ini')):
                    print "file already exist"
                    return render(request, 'new.html', {'form': form})
                f = open(filepath + str('.ini'), 'w+')
                f.write(form.cleaned_data['info'])
                f.close()
            #fc = os.open(filepath, os.O_CREAT)
            #fd = os.open(filepath, os.O_WRONLY)
            #os.write(fd, form.cleaned_data['info'])
            #os.close(fd)
            return HttpResponseRedirect('/list/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewForm()

    return render(request, 'new.html', {'form': form})
