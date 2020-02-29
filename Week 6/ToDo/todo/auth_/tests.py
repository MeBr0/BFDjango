from django.test import TestCase


class AuthTest(TestCase):

    def setUp(self):
        self.user = {
            'username': 'mebr9',
            'password': 'qweqweqwe'
        }

        self.client.post('/auth/register/', self.user)

    def test_register(self):
        user = {
            'username': 'mebr8',
            'password': 'qweqweqwe'
        }

        response = self.client.post('/auth/register/', user)

        self.assertTrue(response.status_code == 201)
        data = response.data

        self.assertEqual(data.get('username'), user['username'])
        self.assertFalse(data.get('is_superuser'))

    def test_user_already_exists(self):
        response = self.client.post('/auth/register/', self.user)

        self.assertTrue(response.status_code == 400)
        self.assertEqual(response.data.get('username')[0], 'A user with that username already exists.')

    def test_login(self):
        response = self.client.post('/auth/login/', self.user)

        self.assertTrue(response.status_code == 200)
        self.assertIsNotNone(response.data.get('token'))

    def test_wrong_login(self):
        # change user's password
        user = self.user
        user['password'] = user['password'] + '1'

        response = self.client.post('/auth/login/', user)

        self.assertTrue(response.status_code == 400)
        self.assertEqual(response.data.get('non_field_errors')[0], 'Unable to log in with provided credentials.')


