# Tech Challenge - Pipeline Batch Bovespa

Este projeto faz parte do Tech Challenge da Fase 2 de Machine Learning Avançado. Ele envolve a construção de um pipeline de dados completo para extrair, processar e analisar dados do pregão D-1 da B3, utilizando serviços da AWS como S3, Glue, Lambda e Athena.

## Índice

- [Descrição do Projeto](#descrição-do-projeto)
- [Requisitos do Pipeline](#requisitos-do-pipeline)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Executar](#como-executar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Descrição do Projeto

O objetivo deste projeto é desenvolver um pipeline batch para a ingestão e arquitetura de dados da Bovespa, com a finalidade de automatizar o processo de extração, transformação e carga (ETL) dos dados do pregão D-1. O pipeline será implementado utilizando os seguintes serviços da AWS:

- **S3**: Armazenamento de dados brutos e refinados em formato Parquet.
- **Glue**: Execução de jobs de ETL no modo visual.
- **Lambda**: Trigger para iniciar o job Glue.
- **Athena**: Consulta dos dados refinados.

## Requisitos do Pipeline

1. **Scraping de Dados**: Extração de dados do site da B3 com informações do pregão D-1.
2. **Ingestão de Dados**: Armazenamento dos dados brutos no S3 em formato Parquet, particionados por data.
3. **Trigger Lambda**: O bucket S3 aciona uma Lambda que inicia o job Glue.
4. **Transformações Glue**:
   - Agrupamento numérico, sumarização, contagem ou soma.
   - Renomeação de duas colunas existentes.
   - Cálculo com campos de data, como duração ou diferença entre datas.
5. **Armazenamento Refinado**: Os dados refinados devem ser salvos no S3 em uma pasta `refined`, particionados por data e pelo nome ou abreviação da ação do pregão.
6. **Catálogo Glue**: O job Glue deve catalogar automaticamente os dados no Glue Catalog e criar uma tabela no banco de dados default.
7. **Consulta no Athena**: Os dados devem estar disponíveis e legíveis no Athena.
8. **Visualização Opcional**: Construção opcional de um notebook no Athena para visualização gráfica dos dados ingeridos.

## Tecnologias Utilizadas

- **AWS S3**
- **AWS Glue**
- **AWS Lambda**
- **AWS Athena**
- **Python (para a Lambda)**
- **Parquet (formato de armazenamento)**

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/tech-challenge-pipeline-bovespa.git
   cd tech-challenge-pipeline-bovespa

