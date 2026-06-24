from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType,
    BooleanType
)

PAGAMENTOS_SCHEMA = StructType([
    StructField(
        "avaliacao_fraude",
        StructType([
            StructField("fraude", BooleanType(), True),
            StructField("score", DoubleType(), True)
        ]),
        True
    ),
    StructField("data_processamento", StringType(), True),
    StructField("forma_pagamento", StringType(), True),
    StructField("id_pedido", StringType(), True),
    StructField("status", BooleanType(), True),
    StructField("valor_pagamento", DoubleType(), True)
])