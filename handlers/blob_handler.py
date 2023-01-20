from handlers.interface import AbstractDBHandler


class BlobHandler(AbstractDBHandler):
    """
    Class to handle the connection to the BLOB storage service
    in Azure
    """
    connection = None

    def __init__(self):
        database_server = dbutils.secrets.get(scope=secret_scope, key='DatabaseHost')
        database_user = dbutils.secrets.get(scope=secret_scope, key='DatabaseUser')
        database_password = dbutils.secrets.get(scope=secret_scope, key='DatabasePassword')
        database_name = dbutils.secrets.get(scope=secret_scope, key='InsightsFactoryDatabaseName')
        insight_factory_db_url = 'jdbc:postgresql://%s:5432/%s?sslmode=require' % (database_server, database_name)

        self.connection = (
            spark.read
            .format("jdbc")
            .option("url", self.insight_factory_db_url)
            .option("user", self.database_user)
            .option("password", self.database_password)
            .option("driver", DRIVER)
            .load()
        )

    def read(self, customer_id: int):
        query = "SELECT * FROM insights_status WHERE customer_id=%s" % customer_id
        return self.connection.query("query", query)

    def write(self, flag_data: object):
        pass
