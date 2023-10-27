from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

#from django.views.generic import View

from .helpers import *

### FUNCTION BASED VIEWs

@require_http_methods(['GET'])
def index(request):
    context = {
        'data': menu_data(request)
    }
    return render(request, 'components/menu.html', context)

@require_http_methods(['GET'])
def gallery(request):
    # TODO FE part for imgs is hardcoded because imgs exist only locally 
    context = {
        'data': gallery_data(request)
    }
    return render(request, 'components/gallery.html', context)

@require_http_methods(['GET'])
def events(request):
    # TODO FE part for imgs is hardcoded because imgs exist only locally 
    context = {
        'data': events_data(request)
    }
    return render(request, 'components/events.html', context)

@require_http_methods(['GET'])
def event(request, id):
    # TODO FE part for imgs is hardcoded because imgs exist only locally 
    context = {
        'data': event_data(request, id)
    }
    
    if context['data'] is None:
        return redirect('/events/')
    return render(request, 'components/event.html', context)

### CLASS BASED VIEW -> simple example

# class AboutUs(View):
#     template_name = 'components/aboutus.html'
#
#     def get(self, request, *args, **kwargs):
#         return render(request, 'components/aboutus.html', {})
#    
#     def post(self, request, *args, **kwargs):
#         # DjangoModelForm
#         return