"""frontkeeper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, patterns
import logging
import os


def init_logger():
    """ 
        Initialisation for logger
        Set the format of logger
        Create log file in log/
    """
    # Init logging level with debug stream handler
    log = logging.getLogger('passkeeper')
    log.setLevel(logging.INFO)
    # log.setLevel(logging.DEBUG)
    logformat = '%(asctime)s %(levelname)s -: %(message)s'
    # Set logger formater
    formatter = logging.Formatter(logformat)
    # File handler
    hdl = logging.FileHandler('%s/log/%s.log' % (os.getcwd(),__name__))
    hdl.setFormatter(formatter)
    log.addHandler(hdl)
    return log

init_logger()

urlpatterns = patterns('frontkeeper.views',
                       url(r'^$', 'index.index'),
                       url(r'^decrypt/', 'decrypt.decrypt'),
                       url(r'^encrypt/', 'encrypt.encrypt'),
                       url(r'^init/', 'init.init'),
                       url(r'^search/', 'search.search'),
                       url(r'^flush/', 'flush.flush'),
                       url(r'^edit/(?P<filename>.+)', 'edit.edit',
                           name='edit'),
                       url(r'^new/', 'new.new'),
                       url(r'^list/', 'list.list'),
                       url(r'^clean/', 'clean.clean'),
                       )
