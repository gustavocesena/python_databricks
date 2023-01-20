from repositories.blob.insights_factory_repository import InsightsFactoryRepository


class BGEventsUOW:
    def __init__(self, insights_factory_repository: InsightsFactoryRepository):
        self.insights_factory_repository = insights_factory_repository
