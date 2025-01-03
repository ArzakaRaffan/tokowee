from django.test import TestCase

from django.test import TestCase, Client

class MainTest(TestCase):
    def test_main_is_exist(self):
        response = Client().get('/main')
        self.assertEqual(response.status_code, 200)

    def test_main_template(self):
        response = Client().get('/main')
        self.assertTemplateUsed(response, 'main.html')