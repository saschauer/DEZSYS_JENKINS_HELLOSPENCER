import unittest
import json
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from hello import app

class TestHelloSpencer(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_endpoint_status_code(self):
        response = self.app.get('/api/hello')
        self.assertEqual(response.status_code, 200)

    def test_hello_endpoint_content_type(self):
        response = self.app.get('/api/hello')
        self.assertEqual(response.content_type, 'application/json')

    def test_hello_endpoint_data(self):
        response = self.app.get('/api/hello')
        data = json.loads(response.data.decode())
        self.assertEqual(data['message'], 'Hello Stefan')
        self.assertEqual(data['status'], 'success')

if __name__ == '__main__':
    unittest.main()