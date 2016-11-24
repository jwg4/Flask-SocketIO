import unittest

from app import create_app, socketio

class TestSocketApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()

    def setUp(self):
        self.client = self.app.test_client()
        self.socket_client = socketio.test_client(self.app)

    def test_undelete_event(self):
        payload = '{"command": "comment foo", "auth": "1234", "name": "Jack"}'
        response = self.client.post('/admin', data=payload)
        self.assertEqual(response.status_code, 200)
        received = self.socket_client.get_received()
        self.assertEqual(len(received), 1)
