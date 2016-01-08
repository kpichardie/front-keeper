from django.shortcuts import  render
from django.http import HttpResponse

from django.shortcuts import render
from django.template import Context, loader


def display(request):

    the_title = "Front-keeper";
    t = loader.get_template('display.html')
    c = Context({
        'the_title': the_title,
        'request': request,
    })
    return HttpResponse(t.render(c)) 

