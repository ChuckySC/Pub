from django.db import models
from django_resized import ResizedImageField
#from django.utils import timezone

#from PIL import Image

class Units(models.Model):
    '''Example: litar, kilogram ...'''
    id = models.BigAutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=255, verbose_name='Unit')
    
    class Meta:
        managed = True
        verbose_name_plural = 'Units'
        ordering = ['name']
        constraints = [models.UniqueConstraint(fields=['name'], name='unique_unit')]
        db_table = 'Units'
    
    def __str__(self):
        return f'{self.name}'
    
class MenuSections(models.Model):
    '''Example: Breakfast, Lunch, Coffee, Alcohol ...'''
    id = models.BigAutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=255, verbose_name='Menu Section')
    
    TYPE_CHOICES =(
        ('D', 'Drink'),
        ('F', 'Food')
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='D', verbose_name='Type')
    
    class Meta:
        managed = True
        verbose_name_plural = 'Menu Sections'
        ordering = ['type', 'id']
        constraints = [models.UniqueConstraint(fields=['name'], name='unique_section')]
        db_table = 'MenuSections'
    
    def __str__(self):
        return f'{self.name}'
    
class MenuItems(models.Model): 
    '''Example: Espresso, Cappuccino, Ice tea ...''' 
    id = models.BigAutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=255, verbose_name='Name')
    type = models.ForeignKey(
        MenuSections, 
        models.DO_NOTHING, 
        db_column='menuSectionId', 
        verbose_name='Menu section'
    )
    description = models.TextField(db_column='description', blank=True, verbose_name='Description')
    quantity = models.FloatField(db_column='quantity', blank=True, null=True, verbose_name='Quantity')
    unitId = models.ForeignKey(
        Units, 
        models.DO_NOTHING, 
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
        verbose_name_plural = 'Menu Items'
        ordering = ['name']
        constraints = [models.UniqueConstraint(fields=['name', 'type'], name='unique_item')]
        db_table = 'MenuItems'
    
    def __str__(self):
        # if str(self.description).strip() not in ['', 'None']:
        #     return f'{self.name} --> {self.description}'
        return f'{self.name}'

class Events(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=255, verbose_name='Event name')
    description = models.TextField(db_column='description', blank=True, verbose_name='Event description')
    date = models.DateField(db_column='date', verbose_name='Date')
    img = ResizedImageField(
        size=[1000, 1000], 
        crop=['middle', 'center'], 
        default='default_square.jpg', 
        upload_to='uploads',
        verbose_name='Event logo'
    )
    
    class Meta:
        managed = True
        verbose_name_plural = 'Events'
        ordering = ['date', 'name']
        constraints = [models.UniqueConstraint(fields=['name', 'date'], name='unique_event')]
        db_table = 'Events'
    
    def __str__(self):
        return f'{self.name}'