from django.test import TestCase

from .models import Category


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='christmas figure', slug='christmas-figure')

    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'christmas-figure')
