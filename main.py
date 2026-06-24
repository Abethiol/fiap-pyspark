from src.config.app_config import AppConfig
from src.session.spark_session_manager import SparkSessionManager
from src.io.data_reader import DataReader

config = AppConfig()

spark_manager = SparkSessionManager(config)
spark = spark_manager.get_spark()

reader = DataReader(spark, config)

df_pedidos = reader.read_pedidos()
df_pagamentos = reader.read_pagamentos()

print("PEDIDOS")
df_pedidos.show(5)

print("PAGAMENTOS")
df_pagamentos.show(5)