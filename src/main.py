from src.config.app_config import AppConfig
from src.session.spark_session_manager import SparkSessionManager
from src.io.data_reader import DataReader
from src.io.data_writer import DataWriter
from src.business.business_logic import BusinessLogic
from src.pipeline.pipeline import Pipeline


def main():
    config = AppConfig()
    spark = SparkSessionManager(config).get_spark()

    try:
        reader = DataReader(spark, config)
        writer = DataWriter(config)
        business_logic = BusinessLogic()

        pipeline = Pipeline(
            reader,
            business_logic,
            writer
        )

        pipeline.run()

    finally:
        spark.stop()


if __name__ == "__main__":
    main()