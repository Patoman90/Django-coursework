from django.test import TestCase
from .models import Item

# Create your tests here.


class TestViews(TestCase):
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status.code, 200)
        self.assertTemplateUsed(page, "todo_list.html")

    def test_get_add_item_page(self):
        page = self.client.get("/add")
        self.assertEqual(page.status.code, 200)
        self.assertTemplateUsed(page, "add_item.html")

    def test_get_edit_item_page(self):
        item = Item(name='Create a Test')
        item.save()

        page = self.client.get("/edit/{0}".format(item.id))
        self.assertEqual(page.status.code, 200)
        self.assertTemplateUsed(page, "add_item.html")

    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status.code, 404)
