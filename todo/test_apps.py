from django.apps import apps
from django.test import TestCase
from .apps import TodoConfig

class TestTodoConfig(TestCase):
    def test_app(self):
        print("\n==========")
        print("test_app")
        self.assertEqual("todo", TodoConfig.name)
        print("test_app -- app name PASS")
        self.assertEqual("todo", apps.get_app_config("todo").name)
        print("test_app -- can get app configuration PASS")