from abc import ABC, abstractclassmethod


class AbstractRepository(ABC):
    """Abstract class to share between repository"""

    @abstractclassmethod
    def get_data_by_customer_id(self, customer_id: int):
        """Simple method to get data from a source"""

    @abstractclassmethod
    def write(self, flag_data: object):
        """Simple method to create data to a source"""
