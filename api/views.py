from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from client.models import *
from .serializers import *

@login_required
@api_view(['GET'])
def sections_view(request):
    try:
        sections = MenuSections.objects.all()
        serialized = MenuSectionsSerializer(sections, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(None, status=status.HTTP_400_BAD_REQUEST)

@login_required
@api_view(['GET'])
def items_view(request):
    try:
        items = MenuItems.objects.filter(active=True)
        serialized = MenuItemsSerializer(items, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return Response(None, status=status.HTTP_400_BAD_REQUEST)  

@login_required 
@api_view(['GET'])
def events_view(request, keyword):
    try:
        events = Events.objects.filter(name__icontains=keyword)
        serialized = EventsSerializer(events, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return Response(None, status=status.HTTP_400_BAD_REQUEST)  

@login_required 
@api_view(['GET'])
def event_view(request, id):
    try:
        event = Events.objects.get(id=id)
        serialized = EventsSerializer(event, many=False)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return Response(None, status=status.HTTP_400_BAD_REQUEST) 

@login_required  
@api_view(['GET'])
def gallery_view(request):
    try:
        gallery = Gallery.objects.all()
        serialized = GallerySerializer(gallery, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return Response(None, status=status.HTTP_400_BAD_REQUEST) 