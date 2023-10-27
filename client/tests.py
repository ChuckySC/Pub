from django.test import TestCase

from .models import (
    Units,
    TypeChoices,
    MenuSections
)

from datetime import datetime

class MenuUnitsTestCase(TestCase):
    def create(self):
        data = [
            {'name': 'kg'},
            {'name': 'l'}
        ]
        
        self.a = Units.objects.create(**data[0])
        self.b = Units.objects.create(**data[1])
        
        self.count = 2
        
    def setUp(self):
        self.create()
        
    def test_unit_count(self):
        qs = Units.objects.all()
        self.assertEqual(qs.count(), self.count)
    
    def test_rid(self):
        qs = Units.objects.get(id=self.a.id)
        self.assertNotEqual(qs.rid, None)
        self.assertIsInstance(qs.rid, datetime)
        
    def test_rud(self):
        qs = Units.objects.get(id=self.a.id)
        self.assertNotEqual(qs.rud, None)
        self.assertIsInstance(qs.rud, datetime)
        
class MenuSectionsTestCase(TestCase):
    def create(self):
        data = [
            {'name': 'Coffee', 'type': 'D'},
            {'name': 'Cider', 'type': 'D'},
            {'name': 'Salad', 'type': 'F'}
        ]
        
        self.a = MenuSections.objects.create(**data[0])
        self.b = MenuSections.objects.create(**data[1])
        self.c = MenuSections.objects.create(**data[2])
        
        self.tcount = 3
        self.dcount = 2
        self.fcount = 1
        
    def setUp(self):
        self.create()
 
    def test_count(self):
        qs = MenuSections.objects.all()
        self.assertEqual(qs.count(), self.tcount)
        self.assertNotEqual(qs.count(), self.dcount)
        self.assertNotEqual(qs.count(), self.fcount)
        
        qs = MenuSections.objects.filter(type=TypeChoices.DRINKS.value)
        self.assertEqual(qs.count(), self.dcount)
        self.assertNotEqual(qs.count(), self.fcount)
        self.assertNotEqual(qs.count(), self.tcount)
        
        qs = MenuSections.objects.filter(type=TypeChoices.FOOD.value)
        self.assertEqual(qs.count(), self.fcount)
        self.assertNotEqual(qs.count(), self.dcount)
        self.assertNotEqual(qs.count(), self.tcount)
    
    def test_type(self):
        qs = MenuSections.objects.filter(type=TypeChoices.DRINKS.value)
        self.assertTrue(qs.exists())
        
    def test_rid(self):
        qs = MenuSections.objects.get(id=self.a.id)
        self.assertNotEqual(qs.rid, None)
        self.assertIsInstance(qs.rid, datetime)
        
    def test_rud(self):
        qs = MenuSections.objects.get(id=self.a.id)
        self.assertNotEqual(qs.rud, None)
        self.assertIsInstance(qs.rud, datetime)