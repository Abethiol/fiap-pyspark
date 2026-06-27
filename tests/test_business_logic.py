import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType,
    LongType,
    BooleanType
)

from src.business.business_logic import BusinessLogic


@pytest.fixture(scope="session")
def spark():
    spark = (
        SparkSession.builder
        .master("local")
        .appName("test")
        .getOrCreate()
    )

    yield spark

    spark.stop()


def test_process_filters_correctly(spark):
    pedidos_schema = StructType([
        StructField("ID_PEDIDO", StringType(), True),
        StructField("PRODUTO", StringType(), True),
        StructField("VALOR_UNITARIO", DoubleType(), True),
        StructField("QUANTIDADE", LongType(), True),
        StructField("DATA_CRIACAO", StringType(), True),
        StructField("UF", StringType(), True),
        StructField("ID_CLIENTE", StringType(), True)
    ])

    pagamentos_schema = StructType([
        StructField("id_pedido", StringType(), True),
        StructField("forma_pagamento", StringType(), True),
        StructField("valor_pagamento", DoubleType(), True),
        StructField("status", BooleanType(), True),
        StructField(
            "avaliacao_fraude",
            StructType([
                StructField("fraude", BooleanType(), True),
                StructField("score", DoubleType(), True)
            ]),
            True
        )
    ])

    pedidos_data = [
        (
            "id-1",
            "PRODUTO A",
            100.0,
            2,
            "2025-03-01T00:00:00.000000",
            "SP",
            "cliente-1"
        ),
        (
            "id-2",
            "PRODUTO B",
            200.0,
            1,
            "2024-03-01T00:00:00.000000",
            "RJ",
            "cliente-2"
        ),
    ]

    pagamentos_data = [
        (
            "id-1",
            "PIX",
            200.0,
            False,
            (False, 0.1)
        ),
        (
            "id-2",
            "BOLETO",
            200.0,
            False,
            (False, 0.1)
        ),
    ]

    df_pedidos = spark.createDataFrame(
        pedidos_data,
        schema=pedidos_schema
    )

    df_pagamentos = spark.createDataFrame(
        pagamentos_data,
        schema=pagamentos_schema
    )

    logic = BusinessLogic()

    resultado = logic.process(
        df_pedidos,
        df_pagamentos
    )

    assert resultado.count() == 1

    linha = resultado.first()

    assert linha["ID_PEDIDO"] == "id-1"
    assert linha["UF"] == "SP"
    assert linha["FORMA_PAGAMENTO"] == "PIX"
    assert linha["VALOR_TOTAL_PEDIDO"] == 200.0