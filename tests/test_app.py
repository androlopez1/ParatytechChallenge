import unittest
from system_module_2 import create_app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    def test_load_from_csv(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_load_data_endpoint_post(self):
        json_data = {
            "show_id" : "s5000",
            "type": "test",
            "title": "test",
            "director": "test",
            "cast": "test",
            "date_added": "test",
            "release_year": "test",
            "rating": "test",
            "duration": "test",
            "listed_in": "test",
            "description": "test",
            }
        response = self.app.post('/load', json=json_data)
        self.assertEqual(response.status_code, 200)

    def test_query_data_endpoint(self):
        response = self.app.get('/query')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
