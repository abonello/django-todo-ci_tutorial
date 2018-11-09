from django.test import TestCase
from .forms import ItemForm

class TestToDoItemForm(TestCase):
    
    def test_can_create_an_item_with_just_a_name(self):
        print("\n==========")
        print("test_can_create_an_item_with_just_a_name")
        form = ItemForm({'name': 'Create Test' })
        # self.assertFalse(form.is_valid())
        self.assertTrue(form.is_valid())
        print("test_can_create_an_item_with_just_a_name -- form is valid PASS")
        
    def test_correct_message_for_missing_name(self):
        print("\n==========")
        print("test_correct_message_for_missing_name")
        form = ItemForm({'name': ''})
        # self.assertTrue(form.is_valid())
        self.assertFalse(form.is_valid())
        print("test_correct_message_for_missing_name -- form is not valid PASS")
        self.assertEqual(form.errors['name'], [u'This field is required.'])
        print("test_correct_message_for_missing_name -- correct error message PASS")
        
    def test_can_create_an_item_with_name_and_done_set_to_true(self):
        print("\n==========")
        print("test_can_create_an_item_with_name_and_done_set_to_true")
        form = ItemForm({'name': 'Testing Done', 'done': True})
        self.assertTrue(form.is_valid())
        print("test_can_create_an_item_with_name_and_done_set_to_true -- form is valid PASS")