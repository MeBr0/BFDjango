import logging

from rest_framework.test import APITestCase


class ToDoListTest(APITestCase):

    # noinspection DuplicatedCode
    def setUp(self):
        logging.disable(logging.CRITICAL)

        self.user = {
            'username': 'mebr9',
            'password': 'qweqweqwe'
        }

        self.client.post('/auth/register/', self.user)
        self.client.login(username=self.user['username'], password=self.user['password'])

        self.todo_list = {'name': 'test list'}
        self.client.post('/lists/', self.todo_list)

    def test_list_todo_list(self):
        response = self.client.get('/lists/')

        self.assertEqual(response.status_code, 200)

        todo_list = response.data

        self.assertIsNotNone(todo_list)
        self.assertEqual(self.todo_list['name'], todo_list[0].get('name'))

    def test_create_todo_list(self):
        self.client.login(username=self.user['username'], password=self.user['password'])

        todo_list = {'name': 'test list'}
        response = self.client.post('/lists/', todo_list)

        self.assertEqual(response.status_code, 201)

        data = response.data

        self.assertEqual(data.get('name'), todo_list['name'])
        self.assertEqual(data.get('owner').get('username'), self.user['username'])

    def test_create_blank_todo_list(self):
        self.client.login(username=self.user['username'], password=self.user['password'])

        todo_list = {'name': ''}
        response = self.client.post('/lists/', todo_list)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.get('name')[0], 'This field may not be blank.')

    def test_create_unauthorized_todo_list(self):
        self.client.logout()

        todo_list = {'name': 'test list'}
        response = self.client.post('/lists/', todo_list)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data.get('detail'), 'Authentication credentials were not provided.')

    def test_retrieve_todo_list(self):
        _id = 1
        response = self.client.get(f'/lists/{_id}/')

        self.assertEqual(response.status_code, 200)
        todo_list = response.data

        self.assertIsNotNone(todo_list)
        self.assertEqual(self.todo_list['name'], todo_list.get('name'))

    def test_retrieve_404_todo_list(self):
        _id = 2
        response = self.client.get(f'/lists/{_id}/')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data['detail'], 'Not found.')

    def test_update_todo_list(self):
        _id = 1
        task_list = {'name': 'updated test list'}
        response = self.client.put(f'/lists/{_id}/', task_list)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], task_list['name'])

    def test_update_blank_todo_list(self):
        _id = 1
        task_list = {'name': ''}
        response = self.client.put(f'/lists/{_id}/', task_list)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.get('name')[0], 'This field may not be blank.')

    def test_update_404_todo_list(self):
        _id = 2
        task_list = {'name': ''}
        response = self.client.put(f'/lists/{_id}/', task_list)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data['detail'], 'Not found.')

    def test_delete_todo_list(self):
        _id = 1
        response = self.client.delete(f'/lists/{_id}/')

        self.assertEqual(response.status_code, 204)

    def test_delete_404_todo_list(self):
        _id = 2
        response = self.client.delete(f'/lists/{_id}/')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data['detail'], 'Not found.')


class ToDoTest(APITestCase):

    # noinspection DuplicatedCode
    def setUp(self):
        logging.disable(logging.CRITICAL)

        self.user = {
            'username': 'mebr9',
            'password': 'qweqweqwe'
        }

        self.client.post('/auth/register/', self.user)
        self.client.login(username=self.user['username'], password=self.user['password'])

        self.todo_list = {'name': 'test list'}
        self.client.post('/lists/', self.todo_list)

    def test_list_todos(self):
        _id = 1
        response = self.client.get(f'/lists/{_id}/todo/')

        self.assertEqual(response.status_code, 200)
        items = response.data

        self.assertIsNotNone(items)
        self.assertEqual(len(items), 1)

        item = items[0]

        self.assertIsNotNone(item)
        self.assertEqual(item.get('name'), 'Empty todo')

    def test_create_todos(self):
        self.client.login(username=self.user['username'], password=self.user['password'])

        _id = 1
        todo = {'name': 'test todo'}
        response = self.client.post(f'/lists/{_id}/todo/', todo)

        self.assertEqual(response.status_code, 201)
        created_todo = response.data

        self.assertIsNotNone(created_todo)
        self.assertEqual(created_todo.get('name'), 'test todo')

        response = self.client.get(f'/lists/{_id}/todo/', todo)

        self.assertEqual(response.status_code, 200)
        items = response.data

        self.assertIsNotNone(items)
        self.assertEqual(len(items), 2)

        item = items[0]

        self.assertIsNotNone(item)
        self.assertEqual(item.get('name'), 'Empty todo')

        item = items[1]

        self.assertIsNotNone(item)
        self.assertEqual(item.get('name'), 'test todo')

