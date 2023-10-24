from rest_framework import serializers
from client.models import *

class MenuSectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuSections
        fields = [
            'id',
            'name',
            'type'
        ]

class MenuItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = [
            'id',
            'name',
            'type',
            'description',
            'quantity',
            'unitId',
            'price',
            'currency',
            'active'
        ]
        
class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = [
            'id',
            'name',
            'description',
            'date',
            'img'
        ]