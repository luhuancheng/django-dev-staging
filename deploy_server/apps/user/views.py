import logging
from django.http import HttpResponse
from django.shortcuts import render


LOGGER = logging.getLogger('apps')


def index(request):
    return HttpResponse('ok')
