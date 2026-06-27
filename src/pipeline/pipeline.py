import logging

class Pipeline:
    def __init__(self, reader, business_logic, writer):
        self.reader = reader
        self.business_logic = business_logic
        self.writer = writer

    def run(self):
        try:
            logging.info("Iniciando pipeline.")

            df_pedidos = self.reader.read_pedidos()
            df_pagamentos = self.reader.read_pagamentos()

            resultado = self.business_logic.process(
                df_pedidos,
                df_pagamentos
            )

            self.writer.write_parquet(resultado)

            logging.info("Pipeline finalizado.")

        except Exception as e:
            logging.error(f"Erro no pipeline: {e}")
            raise