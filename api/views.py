from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from client.models import *
from .serializers import *

@api_view(['GET'])
def sections_view(request):
    try:
        sections = MenuSections.objects.all()
        serialized = MenuSectionsSerializer(sections, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(None, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def items_view(request):
    try:
        items = MenuItems.objects.filter(active=True)
        serialized = MenuItemsSerializer(items, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return Response(None, status=status.HTTP_400_BAD_REQUEST)    