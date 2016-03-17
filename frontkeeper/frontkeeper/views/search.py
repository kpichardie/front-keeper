from django.conf import settings
from django.shortcuts import render
from .forms import SearchForm
import logging
import os
from passkeeper import Passkeeper


def init_logger():
    # Init logging level with debug stream handler
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    # log.setLevel(logging.DEBUG)
    logformat = '%(asctime)s %(levelname)s -: %(message)s'
    # Set logger formater
    formatter = logging.Formatter(logformat)
    # File handler
    hdl = logging.FileHandler('/tmp/%s.log' % __name__)
    hdl.setFormatter(formatter)
    log.addHandler(hdl)
    return log


#  search
def search(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            init_logger()
            mypasskeeper = Passkeeper(directory=settings.PASSKEEPER_PATH)
            (config, match) = mypasskeeper.search(
                              pattern=form.cleaned_data['search'])
            matching = {}
            for section in match:
                matching[section] = config.items(section)
            return render(request, 'result.html',
                          context=({'matching': matching}))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()
    if os.path.exists(settings.PASSKEEPER_ENCRYPT_STATE_FILE):
        state = 'Encrypted /!\/!\/!\ Decrypt first to be able to make \
search /!\/!\/!\ '
        return render(request, 'search-disabled.html',
                      context={'form': form, 'state': state})
    else:
        state = 'Decrypted, Make your search'

    return render(request, 'search.html',
                  context={'form': form, 'state': state})
