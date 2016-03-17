from django.conf import settings
from django.template import Context, loader
from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PasswordForm


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



#  clean
def clean(request):
    # if this is a POST request we need to process the form data
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form

    if os.path.exists(settings.PASSKEEPER_ENCRYPT_STATE_FILE): 
        state='Encrypted /!\/!\/!\ It\'s already encrypted /!\/!\/!\ ' 
    else:
        state='Decrypted, you can encrypt'
        settings.PASSKEEPER_ENCRYPT_STATE = 'True'
        f = open(settings.PASSKEEPER_ENCRYPT_STATE_FILE, 'w+')
        f.write("")
        f.close()
        log = init_logger()
        mypasskeeper = Passkeeper(directory=settings.PASSKEEPER_PATH)
        mypasskeeper.cleanup_ini(force_remove=True)
        
    return HttpResponseRedirect('/')

