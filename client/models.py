from django.db import models

from PIL import Image

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
    
    class Meta:
        managed = True
        verbose_name_plural = 'Menu Sections'
        ordering = ['name']
        constraints = [models.UniqueConstraint(fields=['name'], name='unique_section')]
        db_table = 'MenuSections'
    
    def __str__(self):
        return f'{self.name}'
    
# class Events(models.Model):
#     id = models.BigAutoField(db_column='id', primary_key=True)
#     name = models.CharField(db_column='name', max_length=255, verbose_name='Event name')
#     description = models.TextField(db_column='description', blank=True, verbose_name='Event description')
#     date = models.DateField(db_column='date', verbose_name='Date')
#     img = models.ImageField(db_column='img', null=True, blank=True, upload_to='images/', verbose_name='Event logo')

#TODO check how django works with imgs https://www.youtube.com/watch?v=eOM4e6N7fuc
    
#     class Meta:
#         managed = True
#         verbose_name_plural = 'Events'
#         ordering = ['date', 'name']
#         constraints = [models.UniqueConstraint(fields=['name', 'date'], name='unique_event')]
#         db_table = 'Events'
    
#     def save(self):
#       super().save()
#       image = Image.open(self.img.path)
#       if image.height > 150 or image.width > 150:
#          output_size = (150, 150)
#          image.thumbnail(output_size)
#          image.save(self.img.path)
    
#     def __str__(self):
#         return f'{self.name}'