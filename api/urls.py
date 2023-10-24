from django.urls import path
from .views import *


app_name = 'api'
urlpatterns = [
    path('sections/', sections_view, name='sections'),
    path('items/', items_view, name='items'),
    path('events/', events_view, name='events')
]