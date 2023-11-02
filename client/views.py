from django.core.paginator import Paginator
from django.http import HttpResponseServerError
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect

#from django.views.generic import View

from .helpers import *

### FUNCTION BASED VIEWs

@require_http_methods(['GET'])
def index(request):
    try:
        context = { 'data': menu_data(request) }
        return render(request, 'components/menu.html', context)
    except Exception as e:
        # TODO add custom error page
        # return render(request, '', {})
        raise HttpResponseServerError

@require_http_methods(['GET'])
def gallery(request):
    try:
        # TODO FE part for imgs is hardcoded because imgs exist only locally 
        
        paginator = Paginator(gallery_data(request), 24)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = { 'data': page_obj }
        return render(request, 'components/gallery.html', context)
    except Exception as e:
        # TODO add custom error page
        # return render(request, '', {})
        raise HttpResponseServerError

@require_http_methods(['GET'])
def events(request):
    try:
        # TODO FE part for imgs is hardcoded because imgs exist only locally 
        
        keyword = request.GET['q'] if 'q' in request.GET else ''
        paginator = Paginator(events_data(request, keyword), 24)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = { 'data': page_obj }
        return render(request, 'components/events.html', context)
    except Exception as e:
        # TODO add custom error page
        # return render(request, '', {})
        raise HttpResponseServerError

@require_http_methods(['GET'])
def event(request, id):
    try:
        # TODO FE part for imgs is hardcoded because imgs exist only locally 
        context = { 'data': event_data(request, id) }
        
        if context['data'] is None:
            return redirect('/events/')
        return render(request, 'components/event.html', context)
    except Exception as e:
        # TODO add custom error page
        # return render(request, '', {})
        raise HttpResponseServerError

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