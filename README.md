<h1 align="center">Gerador de Relatório de Estoque</h1>

# Descrição

Este é um aplicativo de gerador de relatórios para estoque, construído em <spam style="font-size: 18px">**Python**</spam> com **Programação Orientada a Objetos (POO)**. Ele recebe como entrada arquivos com dados de estoque, e gera um relatório acerca desses dados.

## Importação de dados



Os dados de estoque podem ser obtidos de diversas fontes, incluindo:

* Arquivos CSV
* Arquivos JSON
* Arquivos XML

## Tipos de relatórios



O aplicativo suporta duas versões de relatórios:

* Relatório simples
* Relatório completo

# Como funciona

O gerador de relatórios de estoque é composto por três módulos principais:

* **Importador de dados**: Responsável por importar os dados de estoque de arquivos CSV, JSON ou XML.

* **Relatório**: Responsável por gerar o relatório final, que pode ser completo ou simplificado.

* **Refatorador de estoque**: Responsável por integrar os dados importados e gerar o relatório final.

## Como usar

1. Instale as dependências do aplicativo com o seguinte comando:

```
pip install -r requirements.txt

```

2. Execute o aplicativo com os seguintes argumentos:

```
inventory_report <caminho_do_arquivo_input> <tipo_de_relatório>

```
