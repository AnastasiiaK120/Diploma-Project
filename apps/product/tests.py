from django.test import TestCase

from .models import Category


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='christmas figure', slug='christmas-figure')

    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'christmas-figure')


    def test__category_view(self):
        response = self.client.get(self.category.get_absolute_url())

        no_response = self.client.get('/category/12345/')

        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'product/category.html')