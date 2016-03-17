from django.template import Context, loader
from django.http import HttpResponse
from django.conf import settings

import os
from django.shortcuts import render

def index(request):

    #request.path
    the_title = "Frontkeeper Home";
    t = loader.get_template('index.html')
    if os.path.exists(settings.PASSKEEPER_ENCRYPT_STATE_FILE): 
        state='Encrypted, you can decrypt to access password'  
    else:
        state='Decrypted /!\/!\/!\  Don\'t forget to encrypt before leaving /!\/!\/!\ '


    c = Context({
        'the_title': the_title,
        'request': request,
        'state': state,
    })

    return HttpResponse(t.render(c))

