from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Item

class TestViews(TestCase):
    def test_get_home_page(self):
        print("\n==========")
        print("test_get_home_page")
        page = self.client.get("/")
        # self.assertEqual(page.status_code, 400)
        self.assertEqual(page.status_code, 200)
        print("test_get_home_page -- Status code 200 PASS")
        self.assertTemplateUsed(page, "todo_list.html")
        print("test_get_home_page -- Template PASS")
        
    def test_get_todo_list(self):
        print("\n==========")
        print("test_get_todo_list")
        page = self.client.get("/todo_list/")
        self.assertEqual(page.status_code, 200)
        print("test_get_todo_list -- Status code 200 PASS")
        self.assertTemplateUsed(page, "todo_list.html")
        print("test_get_todo_list -- Template PASS")
    
    def test_get_add_item_page(self):
        print("\n==========")
        print("test_get_add_item_page")
        page = self.client.get("/add/")
        self.assertEqual(page.status_code, 200)
        print("test_get_add_item_page -- Status code 200 PASS")
        self.assertTemplateUsed(page, "item_form.html")
        print("test_get_add_item_page -- Template PASS")
        
    def test_get_edit_item_page(self):
        item = Item(name='Create A Test')
        item.save()
        print("\n==========")
        print("test_get_edit_item_page")
        page = self.client.get("/edit/{0}".format(item.id))
        self.assertEqual(page.status_code, 200)
        print("test_get_edit_item_page -- Status code 200 PASS")
        self.assertTemplateUsed(page, "item_form.html")
        print("test_get_edit_item_page -- Template PASS") 
        
    def test_get_edit_page_for_nonexisting_item(self):
        print("\n==========")
        print("test_get_edit_page_for_nonexisting_item")
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)
        print("test_get_edit_page_for_nonexisting_item -- Status code 404 Object does not exist PASS")

    

    def test_toggle_status(self):
        print("\n==========")
        print("test_toggle_status")
        item = Item(name='Create a Test')
        item.save()
        self.assertFalse(item.done)
        print("test_toggle_status -- Done defaults to False PASS")
        id = item.id
        response = self.client.post("/toggle/{0}".format(id))
        item = get_object_or_404(Item, pk=id)
        self.assertTrue(item.done)
        print("test_toggle_status -- Done changed from False to True PASS")
        response = self.client.post("/toggle/{0}".format(id))
        item = get_object_or_404(Item, pk=id)
        self.assertFalse(item.done)
        print("test_toggle_status -- Done changed from True to False PASS")
        
    def test_post_create_an_item(self):
        print("\n==========")
        print("test_post_create_an_item")
        response = self.client.post("/add/", {"name": "Create an Item"})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)
        print("test_post_create_an_item -- done is False PASS")
        
    def test_post_edit_an_item(self):
        print("\n==========")
        print("test_post_edit_an_item")
        item = Item(name='Create a Test')
        item.save()
        id = item.id
        
        response = self.client.post("/edit/{0}".format(id), {"name": "Changed name"})
        item = get_object_or_404(Item, pk=id)
        self.assertEqual("Changed name", item.name)
        print("test_post_edit_an_item -- Name edited PASS")
        