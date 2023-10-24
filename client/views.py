from django.shortcuts import render

from .helpers import *

def index(request):
    context = {
        'data': menu(request)
    }
    return render(request, 'components/menu.html', context)

def gallery(request):
    context = {
        
    }
    return render(request, 'components/gallery.html', context)

def events(request):
    context = {
        
    }
    return render(request, 'components/events.html', context)