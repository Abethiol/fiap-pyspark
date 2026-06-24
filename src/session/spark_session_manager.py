from pyspark.sql import SparkSession

class SparkSessionManager:

    def __init__(self, config):
        self.config = config

    def get_spark(self):
        return (
            SparkSession.builder
            .appName(self.config.app_name)
            .getOrCreate()
        )