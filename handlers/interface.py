from abc import ABC, abstractclassmethod


class AbstractDBHandler(ABC):
    """Abstract class to share between handlers"""

    @abstractclassmethod
    def read(self, customer_id: int):
        """Simple method to get data from a source"""

    @abstractclassmethod
    def write(self, flag_data: object):
        """Simple method to create data to a source"""
