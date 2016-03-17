
from django.template import Context, loader
from django.http import HttpResponse


#  result
def result(request, config, match, pattern):
    the_title = "Matches : "
    t = loader.get_template('result.html')
    c = Context({
       'the_title': the_title,
       'match': match,
       'request': request,
    })
    return HttpResponse(t.render(c))
