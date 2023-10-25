from django.urls import path
from . import views

app_name = 'client'

urlpatterns = [
    path('', views.index, name='index'), # menu
    path('gallery/', views.gallery, name='gallery'),
    path('events/', views.events, name='events'),
    path('events/<int:id>', views.event, name='event')
]