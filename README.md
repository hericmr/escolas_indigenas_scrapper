# Análise de Dados de Escolas Indígenas

Scripts para a coleta, processamento e visualização de dados sobre escolas indígenas da SEDUC, usando web scraping e análise de dados com Python.

## Estrutura

```
/
├── base_de_dados/ - Armazena os arquivos CSV gerados.
├── data/ - Contém os arquivos HTML brutos e processados.
├── output/ - Salva os gráficos gerados.
├── reports/ - Contém o dicionário de dados e o planejamento.
├── scripts/
│   ├── plotting/ - Scripts para gerar os gráficos.
│   ├── processing/ - Scripts para processar os dados.
│   └── scraping/ - Scripts para web scraping.
└── README.md
```

## Funcionamento

### 1. Web Scraping

O script `scripts/scraping/school_scraper.py` é responsável por baixar as páginas HTML das escolas e salvá-las no diretório `data/html/`. Ele é feito a partir dos microdados das escolas do estado de SP, ja filtrados, contem apenas as escola Indígenas no estado. Em seguida, o `scripts/scraping/process_html.py` processa esses arquivos HTML para extrair as informações relevantes de cada escola.

### 2. Tratamento de Dados

Os dados extraídos são processados e organizados em tabelas. O script `scripts/processing/process_csv.py` consolida as informações extraídas em arquivos CSV, que são armazenados em `base_de_dados/`. O script `scripts/processing/analise_alunos.py` realiza análises específicas sobre os dados dos alunos.

### 3. Visualização

Os scripts no diretório `scripts/plotting/` utilizam as tabelas de dados para gerar visualizações. Cada script é responsável por criar um gráfico específico, como a distribuição de alunos, a quantidade de escolas por diretoria de ensino, e a relação entre o número de alunos e docentes. Os gráficos gerados são salvos no diretório `output/`.

## Como Usar

Para executar o projeto, siga os passos abaixo:

1.  **Web scraping:**
    ```bash
    python scripts/scraping/school_scraper.py
    python scripts/scraping/process_html.py
    ```

2.  **Processamento de dados:**
    ```bash
    python scripts/processing/process_csv.py
    python scripts/processing/analise_alunos.py
    ```

3.  **Plotagem dos gráficos:**
    ```bash
    python scripts/plotting/plot_alunos.py
    python scripts/plotting/plot_alunos_vs_docentes.py
    python scripts/plotting/plot_distribuicao.py
    python scripts/plotting/plot_equipamentos_distribuicao.py
    python scripts/plotting/plot_escolas_por_diretoria.py
    python scripts/plotting/plot_tipos_ensino.py
    ```
# escolas_indigenas_scrapper
