# Tech Challenge - Pipeline Batch Bovespa

Este projeto faz parte do Tech Challenge da Fase 2 de Machine Learning Avançado. Ele envolve a construção de um pipeline de dados completo para extrair, processar e analisar dados do pregão D-1 da B3, utilizando serviços da AWS como S3, Glue, Lambda e Athena.

## Descrição do Projeto

O objetivo deste projeto é desenvolver um pipeline batch para a ingestão e arquitetura de dados da Bovespa, com a finalidade de automatizar o processo de extração, transformação e carga (ETL) dos dados do pregão D-1. O pipeline será implementado utilizando os seguintes serviços da AWS:

- **S3**: Armazenamento de dados brutos e refinados em formato Parquet.
- **Glue**: Execução de jobs de ETL no modo visual.
- **Lambda**: Trigger para iniciar o job Glue.
- **Athena**: Consulta dos dados refinados.




