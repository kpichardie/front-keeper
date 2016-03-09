from django.template import Context, loader
from django.http import HttpResponse
from django.conf import settings

from django.shortcuts import render

def index(request):

    #request.path
    the_title = "Frontkeeper Home";
    t = loader.get_template('index.html')
    if settings.PASSKEEPER_ENCRYPT_STATE: 
        state='Decrypted /!\/!\/!\  Don\'t forget to encrypt before leaving /!\/!\/!\ '
    else:
        state='Encrypted, you can decrypt to access password'  

    c = Context({
        'the_title': the_title,
        'request': request,
        'state': state,
    })

    return HttpResponse(t.render(c))

