from unittest import TestCase
from repositories.blob.insights_factory_repository import InsightsFactoryRepository


class FakeSession:

    @staticmethod
    def read(customer_id: int):
        return {
            "customer_id": customer_id,
            "name": "Gus",
            "last_name": "Cesena"
        }


class TestInsightsFactoryRepository(TestCase):
    fake_customer_id = 1337

    def setUp(self) -> None:
        self.repository = InsightsFactoryRepository(FakeSession())

    def test_read_method_to_get_customer_id(self):
        data = self.repository.get_data_by_customer_id(self.fake_customer_id)

        self.assertEqual(data.get("customer_id"), self.fake_customer_id)
        self.assertEqual(data.get("name"), "Gus")
        self.assertEqual(data.get("last_name"), "Cesena")
        self.assertFalse(True)
