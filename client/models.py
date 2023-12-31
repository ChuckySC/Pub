from django.db import models
from django.utils import timezone

from django.conf import settings
from django_resized import ResizedImageField

from admin.db.models import BaseTimestampModel


User = settings.AUTH_USER_MODEL

class Units(BaseTimestampModel):
    '''Example: litar, kilogram ...'''
    id = models.BigAutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=255, unique=True, verbose_name='Unit')

    class Meta:
        managed = True
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'
        ordering = ['name']
        db_table = 'Units'
    
    def __str__(self):
        return f'{self.name}'

class TypeChoices(models.TextChoices):    
    # DB_VALUE, USER_FACING_VALUE
    DRINKS = 'D', 'Drinks'
    FOOD = 'F', 'Food'

class MenuSections(BaseTimestampModel):
    '''Example: Breakfast, Lunch, Coffee, Alcohol ...'''
    id = models.BigAutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=255, unique=True, verbose_name='Menu Section')
    type = models.CharField(max_length=1, choices=TypeChoices.choices, default=TypeChoices.DRINKS, verbose_name='Type')
    
    class Meta:
        managed = True
        verbose_name = 'Menu Section'
        verbose_name_plural = 'Menu Sections'
        ordering = ['type', 'id']
        db_table = 'MenuSections'
    
    def __str__(self):
        return f'{self.name}'
    
class MenuItems(BaseTimestampModel): 
    '''Example: Espresso, Cappuccino, Ice tea ...''' 
    id = models.BigAutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=255, verbose_name='Name')
    type = models.ForeignKey(
        MenuSections, 
        models.CASCADE, 
        db_column='menuSectionId', 
        verbose_name='Menu section'
    )
    description = models.TextField(db_column='description', blank=True, verbose_name='Description')
    quantity = models.FloatField(db_column='quantity', blank=True, null=True, verbose_name='Quantity')
    unitId = models.ForeignKey(
        Units, 
        models.SET_NULL, 
        blank=True, 
        null=True, 
        db_column='unitId', 
        verbose_name='Unit'
    )
    price = models.FloatField(db_column='price', verbose_name='Price')
    currency = models.CharField(db_column='currency', max_length=255, default='rsd', verbose_name='Currency')
    active = models.BooleanField(db_column='active', verbose_name='Offer is available?')

    class Meta:
        managed = True
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'
        ordering = ['name']
        constraints = [models.UniqueConstraint(fields=['name', 'type'], name='unique_item')]
        db_table = 'MenuItems'
    
    def __str__(self):
        return f'{self.name}'

class Events(BaseTimestampModel):
    id = models.BigAutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=255, verbose_name='Event name')
    description = models.TextField(db_column='description', blank=True, verbose_name='Event description')
    date = models.DateField(db_column='date', auto_now_add=False, auto_now=False, default=timezone.now, verbose_name='Date')
    img = ResizedImageField(
        size=[2878, 1618], 
        crop=['middle', 'center'], 
        default='uploads/default.jpg', 
        upload_to='uploads',
        verbose_name='Event logo'
    )
    
    class Meta:
        managed = True
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['date', 'name']
        constraints = [models.UniqueConstraint(fields=['name', 'date'], name='unique_event')]
        db_table = 'Events'
    
    def __str__(self):
        return f'{self.name}'

class Gallery(BaseTimestampModel):
    id = models.BigAutoField(db_column='id', primary_key=True)
    eventId = models.ForeignKey(
        Events, 
        models.CASCADE, 
        db_column='eventId', 
        verbose_name='Event'
    )
    img = ResizedImageField(
        size=[2878, 1618], 
        crop=['middle', 'center'], 
        default='uploads/default.jpg', 
        upload_to='uploads',
        verbose_name='Photo for gallery'
    )
    
    class Meta:
        managed = True
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'
        ordering = ['id']
        constraints = [models.UniqueConstraint(fields=['img'], name='unique_event_photo')]
        db_table = 'Gallery'
    
    def __str__(self):
        return f'{self.id}'