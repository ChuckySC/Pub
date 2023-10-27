from django.urls import path
from . import views

from django.views.generic import TemplateView

app_name = 'client'

urlpatterns = [
    path('', views.index, name='index'), # menu
    path('gallery/', views.gallery, name='gallery'),
    path('events/', views.events, name='events'),
    path('events/<int:id>', views.event, name='event'),

    # CASE: doesn't require DB, just a template
    path('aboutus/', TemplateView.as_view(template_name='components/aboutus.html'), name='aboutus')
]