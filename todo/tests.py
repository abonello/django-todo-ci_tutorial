from django.test import TestCase

# Create your tests here.
class TestDjango(TestCase):
    
    def test_is_this_thing_on(self):
        print("\n==========")
        print("test_post_create_an_item")
        # self.assertEqual(1, 0)
        self.assertEqual(1, 1)
        print("Testing is working -- PASS")