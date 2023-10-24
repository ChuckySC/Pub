from django.shortcuts import render

from .helpers import *

def index(request):
    context = {
        'data': menu_data(request)
    }
    return render(request, 'components/menu.html', context)

def gallery(request):
    # TODO FE part for imgs is hardcoded because imgs exist only locally 
    context = {
        'data': gallery_data(request)
    }
    return render(request, 'components/gallery.html', context)

def events(request):
    # TODO FE part for imgs is hardcoded because imgs exist only locally 
    context = {
        'data': events_data(request)
    }
    return render(request, 'components/events.html', context)