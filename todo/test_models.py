from django.test import TestCase
from .models import Item

class TestItemModel(TestCase):
    def test_done_defaults_to_False(self):
        print("\n==========")
        print("test_done_defaults_to_False")
        item = Item(name='Create a Test')
        item.save()
        self.assertEqual(item.name, 'Create a Test')
        print("test_done_defaults_to_False -- Name is correct PASS")
        self.assertFalse(item.done)
        print("test_done_defaults_to_False -- Done defaults to False PASS")
        
    def test_can_create_item_with_name_and_done_is_True(self):
        print("\n==========")
        print("test_can_create_item_with_name_and_done_is_True")
        item = Item(name='Create a Test', done=True)
        item.save()
        self.assertEqual(item.name, 'Create a Test')
        print("test_can_create_item_with_name_and_done_is_True -- Name is correct PASS")
        self.assertTrue(item.done)
        print("test_can_create_item_with_name_and_done_is_True -- Done is True PASS")
        
    def test_item_as_a_string(self):
        print("\n==========")
        print("test_item_as_a_string")
        item = Item(name='Create a Test')
        item.save()
        self.assertEqual("Create a Test", str(item))
        print("test_item_as_a_string -- String representation PASS")