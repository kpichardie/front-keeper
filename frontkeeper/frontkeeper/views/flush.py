from django.conf import settings
from django.template import Context, loader
from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SubmitForm

import logging

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
def flush(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubmitForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            log = init_logger()
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
            #return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubmitForm()



    if os.path.exists(settings.PASSKEEPER_ENCRYPT_STATE_FILE): 
        state='Encrypted'
    else:
        state='Decrypted /!\/!\/!\  Don\'t forget to encrypt before leaving /!\/!\/!\ '

    return render(request, 'flush.html', context={'form': form, 'state': state})
