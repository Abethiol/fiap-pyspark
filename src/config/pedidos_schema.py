from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType,
    LongType
)

PEDIDOS_SCHEMA = StructType([
    StructField("ID_PEDIDO", StringType(), True),
    StructField("PRODUTO", StringType(), True),
    StructField("VALOR_UNITARIO", DoubleType(), True),
    StructField("QUANTIDADE", LongType(), True),
    StructField("DATA_CRIACAO", StringType(), True),
    StructField("UF", StringType(), True),
    StructField("ID_CLIENTE", StringType(), True)
])