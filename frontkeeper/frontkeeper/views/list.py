from django.conf import settings
from django.template import Context, loader
from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SubmitForm

import logging

from passkeeper import *
import os

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
def list(request):
    ## if this is a POST request we need to process the form data
    #if request.method == 'POST':
    #    # create a form instance and populate it with data from the request:
    #    form = listForm(request.POST)
    #    # check whether it's valid:
    #    if form.is_valid():
    #        # process the data in form.cleaned_data as required
    #        # ...
    #        # redirect to a new URL:
    #        log = init_logger()
    #        mypasskeeper = Passkeeper(directory='/opt/mypasskeeper')
    #        mypasskeeper.flush_history()
    #        #return HttpResponseRedirect('/')

    ## if a GET (or any other method) we'll create a blank form
    #else:
    #    form = SubmitForm()

    #return render(request, 'flush.html', {'form': form})
    files = []
    for fname in os.listdir(path=settings.PASSKEEPERPATH):
        file_path = os_join(passkeeperdir, fname)
        if (fname.endswith('.ini') and os.path.isfile(file_path)):
            files.append(fname)

    the_title = "Front-keeper"
    t = loader.get_template('list.html')
    c = Context({
        'the_title': the_title,
        'request': request,
        'files': files,
    })
    return HttpResponse(t.render(c))
