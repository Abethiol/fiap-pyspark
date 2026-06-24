import yaml


class AppConfig:

    def __init__(self, config_file="src/config/settings.yaml"):
        with open(config_file, "r", encoding="utf-8") as file:
            self.config = yaml.safe_load(file)

    @property
    def pedidos_path(self):
        return self.config["paths"]["pedidos"]

    @property
    def pagamentos_path(self):
        return self.config["paths"]["pagamentos"]

    @property
    def output_path(self):
        return self.config["paths"]["output"]

    @property
    def app_name(self):
        return self.config["spark"]["app_name"]