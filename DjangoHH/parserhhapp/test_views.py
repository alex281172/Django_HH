from django.test import TestCase
from django.test import Client
from usersapp.models import ParsUser

class OpenViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_statutes(self):
        response = self.client.get('http://127.0.0.1:8000/users/register/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('http://127.0.0.1:8000/users/login/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('http://127.0.0.1:8000/', {'vacancy': 'Python developer', 'city': '', 'size': '20'})
        self.assertEqual(response.status_code, 302)


    def test_login_required(self):
        ParsUser.objects.create_user(username='test_user', email='test@test.com', password='1234567Alex')
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 302)

        self.client.login(username='test_user', email='test@test.com', password='1234567Alex')
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)

