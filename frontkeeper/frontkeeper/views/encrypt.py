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



#  encrypt
def encrypt(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PasswordForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            log = init_logger()
            mypasskeeper = Passkeeper(directory=settings.PASSKEEPER_PATH)
            LOG.info('test %s' % mypasskeeper.directory)
            mypasskeeper.encrypt(commit_message="Update encrypted files through frontkeeper",passphrase=form.cleaned_data['password'])
            mypasskeeper.cleanup_ini(force_remove=True)
            f = open(settings.PASSKEEPER_ENCRYPT_STATE_FILE , 'w+')
            f.write("")
            f.close()
            #return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PasswordForm()

    if os.path.exists(settings.PASSKEEPER_ENCRYPT_STATE_FILE): 
        state='Encrypted /!\/!\/!\ It\'s already encrypted /!\/!\/!\ ' 
        return render(request, 'encrypt-disabled.html', context={'form': form, 'state': state})
    else:
        state='Decrypted, you can encrypt'

    return render(request, 'encrypt.html', context={'form': form, 'state': state})
