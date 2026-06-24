from src.config.pedidos_schema import PEDIDOS_SCHEMA
from src.config.pagamentos_schema import PAGAMENTOS_SCHEMA


class DataReader:

    def __init__(self, spark, config):
        self.spark = spark
        self.config = config

    def read_pedidos(self):
        return (
            self.spark.read
            .option("header", True)
            .option("delimiter", ";")
            .schema(PEDIDOS_SCHEMA)
            .csv(self.config.pedidos_path)
        )

    def read_pagamentos(self):
        return (
            self.spark.read
            .schema(PAGAMENTOS_SCHEMA)
            .json(self.config.pagamentos_path)
        )