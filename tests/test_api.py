import unittest
import requests
import os
from urllib.parse import urljoin

class TestAPIEndpoints(unittest.TestCase):
    def setUp(self):
        # Wenn wir in Jenkins (Docker) laufen, nutzen wir host.docker.internal, sonst localhost
        self.base_url = "http://host.docker.internal:5556"
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def test_hello_endpoint_success(self):
        response = requests.get(urljoin(self.base_url, '/api/hello'), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('application/json', response.headers['Content-Type'])

        data = response.json()
        self.assertEqual(data['message'], 'Hello Spencer')
        self.assertEqual(data['status'], 'success')

    def test_api_response_time(self):
        response = requests.get(urljoin(self.base_url, '/api/hello'), headers=self.headers)
        self.assertLess(response.elapsed.total_seconds(), 1.0)

if __name__ == '__main__':
    unittest.main()