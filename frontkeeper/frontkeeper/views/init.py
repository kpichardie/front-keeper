from django.conf import settings
from django.shortcuts import render
from .forms import PasswordForm
import logging
import os
from passkeeper import Passkeeper


def init_logger():
    # Init logging level with debug stream handler
    log = logging.getLogger('passkeeper')
    log.setLevel(logging.INFO)
    # log.setLevel(logging.DEBUG)
    logformat = '%(asctime)s %(levelname)s -: %(message)s'
    # Set logger formater
    formatter = logging.Formatter(logformat)
    # File handler
    hdl = logging.FileHandler('log/%s.log' % __name__)
    hdl.setFormatter(formatter)
    log.addHandler(hdl)
    return log


#  init
def init(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PasswordForm(request.POST)
        if form.is_valid():
            init_logger()
            mypasskeeper = Passkeeper(directory=settings.PASSKEEPER_PATH)
            mypasskeeper.init_dir(passphrase=form.cleaned_data['password'])
            f = open(settings.PASSKEEPER_ENCRYPT_STATE_FILE, 'w+')
            f.write("")
            f.close()
    # if a GET (or any other method) we'll create a blank form
    else:
        if settings.DISABLE_INIT != 'True':
            form = PasswordForm()
            if os.path.exists(settings.PASSKEEPER_ENCRYPT_STATE_FILE):
                state = 'Encrypted or clean /!\/!\/!\ you will erase \
passwords if existing /!\/!\/!\ '
            else:
                state = 'Decrypted /!\/!\/!\ No need to init /!\/!\/!\ '

            return render(request, 'init.html',
                          context={'form': form, 'state': state})
        return render(request, 'init-disabled.html')
