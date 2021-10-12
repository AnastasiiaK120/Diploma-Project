from django.test import TestCase, SimpleTestCase
from django.urls import reverse

class HomepageTest(SimpleTestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('frontpage'))
        self.assertEqual(response.status_code, 200)

    def setUp(self) -> None:
        url = reverse('frontpage')
        self.response = self.client.get(url)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'frontpage.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Frontpage')

    def test_homepage_doesnt_contains_correct_html(self):
        self.assertNotContains(self.response, 'Hello')
