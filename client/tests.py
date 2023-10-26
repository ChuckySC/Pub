from django.test import TestCase

from .models import MenuSections
from .models import TypeChoices

class MenuSectionsTestCase(TestCase):
    def create_section(self):
        data = [
            {'name': 'Coffee', 'type': 'D'},
            {'name': 'Cider', 'type': 'D'},
            {'name': 'Salad', 'type': 'F'}
        ]
        
        self.draft_a = MenuSections.objects.create(**data[0])
        self.draft_b = MenuSections.objects.create(**data[1])
        self.draft_c = MenuSections.objects.create(**data[2])
        
        self.sec_tcount = 3
        self.sec_dcount = 2
        self.sec_fcount = 1
        
    def setUp(self):
        self.create_section()
        
    def test_section_type(self):
        qs = MenuSections.objects.filter(type=TypeChoices.DRINKS.value)
        self.assertTrue(qs.exists())
        
    def test_section_count(self):
        qs = MenuSections.objects.all()
        self.assertEqual(qs.count(), self.sec_tcount)
        self.assertNotEqual(qs.count(), self.sec_dcount)
        self.assertNotEqual(qs.count(), self.sec_fcount)
        
        qs = MenuSections.objects.filter(type=TypeChoices.DRINKS.value)
        self.assertEqual(qs.count(), self.sec_dcount)
        self.assertNotEqual(qs.count(), self.sec_fcount)
        self.assertNotEqual(qs.count(), self.sec_tcount)
        
        qs = MenuSections.objects.filter(type=TypeChoices.FOOD.value)
        self.assertEqual(qs.count(), self.sec_fcount)
        self.assertNotEqual(qs.count(), self.sec_dcount)
        self.assertNotEqual(qs.count(), self.sec_tcount)
        
    def test_section_rid(self):
        qs = MenuSections.objects.get(id=self.draft_a.id)
        self.assertNotEqual(qs.rid, None)
        
    def test_section_rud(self):
        qs = MenuSections.objects.get(id=self.draft_a.id)
        self.assertNotEqual(qs.rud, None)