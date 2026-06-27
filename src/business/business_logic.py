import logging
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, year, to_timestamp

class BusinessLogic:
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def process(self,
                 pedidos_df: DataFrame,
                 pagamentos_df: DataFrame,
    ) -> DataFrame:

        try:
            logging.info("Iniciando processamento.")

            pedidos_2025 = pedidos_df.filter(
                year(
                    to_timestamp(
                        col("DATA_CRIACAO"),
                        "yyyy-MM-dd'T'HH:mm:ss.SSSSSS"
                    )
                )== 2025
            )

            logging.info("Pedidos de 2025 filtrados.")

            pagamentos_validos = pagamentos_df.filter(
                (col("status") == False) &
                (col("avaliacao_fraude.fraude") == False)
            )

            logging.info("Pagamentos válidos filtrados.")

            resultado = (
                pedidos_2025.alias("p")
                .join(
                    pagamentos_validos.alias("pg"),
                    col("p.ID_PEDIDO") == col("pg.id_pedido"),
                    "inner"
                )
                .select(
                    col("p.ID_PEDIDO"),
                    col("p.UF"),
                    col("pg.forma_pagamento").alias("FORMA_PAGAMENTO"),
                    (
                        col("p.VALOR_UNITARIO") *
                        col("p.QUANTIDADE")
                    ).alias("VALOR_TOTAL_PEDIDO"),
                    col("p.DATA_CRIACAO")
                )
            )

            logging.info("Processamento concluído.")

            return resultado

        except Exception as e:
            logging.error(f"Erro durante o processamento: {e}")
            raise