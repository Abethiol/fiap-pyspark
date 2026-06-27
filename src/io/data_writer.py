from pyspark.sql import DataFrame

class DataWriter:
    def __init__(self, config):
        self.config = config

    def write_parquet(self, df: DataFrame):
        (
            df
            .orderBy("UF", "FORMA_PAGAMENTO", "DATA_CRIACAO")
            .write
            .mode("overwrite")
            .parquet(self.config.output_path)
        )