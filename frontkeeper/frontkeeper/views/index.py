from django.template import Context, loader
from django.http import HttpResponse

from django.shortcuts import render

def index(request):

    #request.path
    the_title = "Frontkeeper Home";
    t = loader.get_template('index.html')
    c = Context({
        'the_title': the_title,
        'request': request,
    })
    return HttpResponse(t.render(c))

