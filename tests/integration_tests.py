import requests
import unittest

class IntegrationTest(unittest.TestCase):
    def test_refresh(self):
        response = requests.get('http://localhost:8080/_refresh/')         
        self.assertEqual(200, response.status_code)