from unittest import TestCase, mock
from handlers.blob_handler import BlobHandler


class FakeConnection:
    @staticmethod
    def query(self, *args):
        return {
            "customer_id": 1337,
            "name": "Gus"
        }


class TestBlobHandler(TestCase):

    @mock.patch("handlers.blob_handler.BlobHandler.__init__", return_value=None)
    def setUp(self, *args) -> None:
        self.handler = BlobHandler()
        self.handler.connection = FakeConnection()

    def test_read_by_customer_id(self):
        fake_customer_id = 1337
        data = self.handler.read(fake_customer_id)
        self.assertEqual(data.get("customer_id"), fake_customer_id)
        self.assertEqual(data.get("name"), "Gus")
