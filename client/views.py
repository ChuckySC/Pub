from django.shortcuts import render, redirect

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

def event(request, id):
    # TODO FE part for imgs is hardcoded because imgs exist only locally 
    context = {
        'data': event_data(request, id)
    }
    
    if context['data'] is None:
        return redirect('/events/')
    return render(request, 'components/event.html', context)