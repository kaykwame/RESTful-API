from django.test import TestCase
from webbackend.models import Items

# Create your tests here.


"""
Testing model
"""


class ItemsTest(TestCase):
    def setUp(self):
        self.items = Items.objects.create(title="test", description="test")

    def test_items_name(self):
        self.assertEqual(self.items.title, "test")

    def test_items_creation(self):
        self.assertTrue(isinstance(self.items, Items))

    def test_items_str(self):
        self.assertEqual(str(self.items), self.items.title)
