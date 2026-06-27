# FIAP PySpark - Projeto Final

Projeto desenvolvido como atividade final da disciplina de Engenharia de Dados utilizando **Python**, **PySpark** e **Programação Orientada a Objetos (POO)**.

O objetivo do projeto é processar dois conjuntos de dados (pedidos e pagamentos), aplicar filtros, transformações e junções entre os datasets para gerar um relatório consolidado em formato **Apache Parquet**.

---

# Tecnologias utilizadas

- Python 3.13+
- Apache Spark (PySpark)
- Apache Parquet
- PyYAML
- Pytest

---

# Arquitetura

O projeto foi desenvolvido seguindo os princípios da Programação Orientada a Objetos, separando cada responsabilidade em uma classe específica.

```text
                    main.py
                       │
       ┌───────────────┴───────────────┐
       │                               │
AppConfig                  SparkSessionManager
       │                               │
       └───────────────┬───────────────┘
                       │
                    Pipeline
                       │
        ┌──────────────┼──────────────┐
        │              │              │
   DataReader    BusinessLogic   DataWriter
```

Cada classe possui uma única responsabilidade:

| Classe | Responsabilidade |
|---------|------------------|
| AppConfig | Leitura das configurações da aplicação |
| SparkSessionManager | Criação da Spark Session |
| DataReader | Leitura dos datasets |
| BusinessLogic | Aplicação das regras de negócio |
| DataWriter | Escrita do relatório em formato Parquet |
| Pipeline | Orquestração da aplicação |
| main.py | Inicialização da aplicação (Aggregation Root) |

---

# Estrutura do projeto

```text
fiap-pyspark/
│
├── data/
│   ├── dataset-json-pagamentos/
│   ├── datasets-csv-pedidos/
│   └── .gitignore
│
├── src/
│   ├── business/
│   ├── config/
│   ├── io/
│   ├── pipeline/
│   ├── session/
│   └── main.py
│
├── tests/
│
├── README.md
├── requirements.txt
├── pyproject.toml
└── MANIFEST.in
```

---

# Regras de negócio

Durante a execução do pipeline são realizadas as seguintes etapas:

1. Leitura do dataset de pedidos (CSV);
2. Leitura do dataset de pagamentos (JSON);
3. Filtragem de pedidos criados no ano de **2025**;
4. Filtragem de pagamentos recusados (`status = false`);
5. Remoção de pagamentos classificados como fraude;
6. INNER JOIN entre os datasets de pedidos e pagamentos;
7. Cálculo do valor total do pedido (`VALOR_UNITARIO × QUANTIDADE`);
8. Geração do relatório contendo:

- ID do pedido;
- UF;
- Forma de pagamento;
- Valor total do pedido;
- Data de criação.

O resultado é gravado em formato **Apache Parquet**, ordenado por:

- UF;
- Forma de pagamento;
- Data de criação.

---

# Datasets

> **Importante**

Este repositório **não contém os datasets utilizados pelo projeto**.

A pasta `data/` encontra-se no `.gitignore`, portanto é necessário clonar os repositórios disponibilizados pelo professor antes da execução da aplicação.

```bash
git clone https://github.com/infobarbosa/datasets-csv-pedidos
git clone https://github.com/infobarbosa/dataset-json-pagamentos
```

Após realizar o clone, mantenha exatamente a seguinte estrutura de diretórios:

```text
data/
├── dataset-json-pagamentos/
│   └── data/
│       └── pagamentos/
│           ├── pagamentos-2024-01.json.gz
│           ├── pagamentos-2024-02.json.gz
│           └── ...
│
└── datasets-csv-pedidos/
    └── data/
        └── pedidos/
            ├── pedidos-2024-01.csv.gz
            ├── pedidos-2024-02.csv.gz
            └── ...
```

Caso essa estrutura seja alterada, os caminhos definidos em `src/config/settings.yaml` também deverão ser atualizados.

---

# Pré-requisitos

- Python 3.13+
- Java 11 ou superior (necessário para o Spark)

Para instalar o Java no Linux:

```bash
sudo apt install default-jdk
```

Para verificar se está instalado:

```bash
java -version
```
---

# Instalação

Clone este repositório:

```bash
git clone https://github.com/Abethiol/fiap-pyspark.git
```

Entre na pasta do projeto:

```bash
cd fiap-pyspark
```

Crie um ambiente virtual:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Atualize o pip:

```bash
python -m pip install --upgrade pip
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# Configuração

As configurações da aplicação encontram-se em:

```text
src/config/settings.yaml
```

Nesse arquivo são definidos:

- nome da aplicação Spark;
- localização dos datasets;
- diretório de saída;
- opções de leitura do arquivo CSV.

---

# Execução

Execute a aplicação com:

```bash
python -m src.main
```

---

# Executando os testes

Para executar todos os testes do projeto:

```bash
pytest tests/
```

---

# Saída

O relatório será gerado em formato **Apache Parquet** no diretório:

```text
output/relatorio/
```

---

# Autores

- Aldrin Lucas Bethiol
- João Vitor Pereira Pinto
- Maria Eduarda Magalhães Moura
- Pedro Sanders Garcia
