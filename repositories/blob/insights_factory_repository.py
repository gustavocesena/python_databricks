from repositories.interface import AbstractRepository


class InsightsFactoryRepository(AbstractRepository):
    """
    Insights Factory Repository

    This repository will handle all the logic behind how to get
    data from some specific source

    Attributes
    ----------
    session: object = DB Session
    """
    session: object = None

    def __init__(self, session: object):
        self.session = session

    def get_data_by_customer_id(self, customer_id: int):
        """
        Simple read method to get data from the source
        :param customer_id: Insulet customer ID
        :return: dict
        """
        return self.session.read(customer_id)

    def write(self, flag_data: object):
        pass
