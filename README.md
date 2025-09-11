# Project Repository - Analysis and Specifications

Este repositório contém os arquivos e recursos utilizados na análise de três projetos descritos no artigo. O objetivo principal do projeto é realizar uma análise estatística dos dados coletados, além de gerar visualizações gráficas que facilitam a compreensão das informações. O repositório está estruturado em três pastas principais, cada uma com um propósito específico.

## Estrutura do Repositório

### 1. **code/**
A pasta `code` contém o código responsável pela análise dos projetos. O código aceita como entrada dois arquivos CSV contendo os dados a serem analisados. Ele realiza análises estatísticas e gera gráficos para facilitar a interpretação dos dados.

O código está dividido em três menus principais:
- **Comparadores**: Permite realizar comparações entre diferentes conjuntos de dados.
- **Visualizadores**: Gera gráficos e imagens para uma visualização mais clara dos dados analisados.
- **Descrevedores**: Fornece uma análise mais detalhada dos dados e descreve as informações de maneira mais profunda.

#### Como Executar
Para executar o código, forneça os caminhos absolutos dos dois arquivos CSV como argumentos. O código processará os dados e apresentará as análises e gráficos correspondentes.

### 2. **data/**
A pasta `data` está estruturada em 4 subdiretórios principais. O primeiro, intitulado "questionnaires", arquiva os dados coletados de dois questionários distintos. O primeiro, "firstquestionnaire", contém suas respectivas respostas, enquanto o segundo, "secondquestionnaire", é apresentado em uma pasta com dois arquivos específicos: "subjectiveAnswers", destinado ao registro das respostas subjetivas dos participantes, e "objectiveAnswers", que exibe um gráfico consolidado das respostas objetivas. O segundo subdiretório, "spreadsheets", possui as planilhas contendo os atributos considerados para a análise, incluindo tanto os que foram utilizados quanto os que foram posteriormente descartados, além do scriptdos dados para serem executados no ambiente Google Apps Script. Além disso, temos mais 2 arquivos, são esses: 

- **median_comparison**: Este arquivo apresenta uma análise comparativa da variação das medianas (ou médias) entre os projetos pós-intervenção.

- **Describers**: Reúne todas as estatísticas descritivas — como média, variância, e valores de máximo e mínimo — que foram empregadas para a análise dos parâmetros da pesquisa.

### 3. **specifications/**
A pasta `specifications` contém o documento fornecido pelo professor, que descreve os requisitos para o desenvolvimento dos projetos analisados. Este documento especifica as funcionalidades e diretrizes dos três projetos abordados neste estudo: o **Jogo**, o **Robô** e os **Pós-Intervenção**.

Este arquivo serve como base para os requisitos dos trabalhos da disciplina, orientando o desenvolvimento e as expectativas dos projetos analisados.

### 4. **complementary_figures/**
O diretório `complementary_figures` armazena gráficos gerados por meio do código desenvolvido para este estudo, os quais servem para fortalecer as conclusões apresentadas no artigo. O conteúdo está organizado da seguinte forma:

- **cognitive_complexity-QP.1**: Apresenta os histogramas da complexidade cognitiva (cognitive complexity) ao longo dos semestres. Esta análise comparativa subsidia a resposta à Questão de Pesquisa 1 (QP1).
- **cyclomatic_complexity-QP.1**: Contém os histogramas da complexidade ciclomática (cyclomatic complexity) distribuídos por semestre, fornecendo dados para a resposta à Questão de Pesquisa 1 (QP1).
- **density_duplication-QP.2**: Exibe os boxplots da densidade de duplicação de código nos projetos analisados após a intervenção. Essa comparação é fundamental para a resposta da Questão de Pesquisa 2 (QP2).
- **open_issues-QP.1**: Contém os histogramas do open issues distribuídos por semestre, fornecendo dados para a resposta à Questão de Pesquisa 1 (QP1).
- **debt_ratio-QP.1**: Mostra os histogramas do debt_ratio durante os semestres, reforçando a resposta da Questão de Pesquisa 1 (QP1).

---
