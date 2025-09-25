import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_alunos_vs_docentes():
    """
    Analisa e plota a relação entre o número de alunos e professores por escola.
    """
    # Usa um estilo mais moderno
    plt.style.use('seaborn-v0_8-darkgrid')

    # Lê os dados
    escolas_path = os.path.join('base_de_dados', 'escolas.csv')
    docentes_path = os.path.join('base_de_dados', 'docentes.csv')

    df_escolas = pd.read_csv(escolas_path)
    df_docentes = pd.read_csv(docentes_path)

    # Junta os dataframes pelo identificador da escola
    # Garante que os nomes das colunas para junção sejam os mesmos
    # Calcula o Total_Docentes a partir de df_docentes
    # Conta professores únicos (Nome) por escola (CIE_Escola)
    df_total_docentes = df_docentes.groupby('CIE_Escola')['Nome'].nunique().reset_index()
    df_total_docentes = df_total_docentes.rename(columns={'Nome': 'Total_Docentes'})

    # Junta os dataframes pelo identificador da escola
    df_escolas = df_escolas.rename(columns={'CIE': 'CIE_Escola'})
    merged_df = pd.merge(df_escolas, df_total_docentes, on='CIE_Escola', how='inner')

    # Converte colunas relevantes para numérico, tratando possíveis erros
    merged_df['Total_Alunos'] = pd.to_numeric(merged_df['Total_Alunos'], errors='coerce').fillna(0)
    merged_df['Total_Docentes'] = pd.to_numeric(merged_df['Total_Docentes'], errors='coerce').fillna(0)

    # Cria o gráfico de dispersão
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.scatter(merged_df['Total_Alunos'], merged_df['Total_Docentes'], alpha=0.7, color='green')

    # Adiciona rótulos e título
    ax.set_xlabel('Número Total de Alunos')
    ax.set_ylabel('Número Total de Docentes')
    ax.set_title('Relação entre Número de Alunos e Docentes por Escola', fontsize=16)
    ax.grid(True)

    # Adiciona o texto da fonte
    fig.text(0.5, 0.01, 'Fonte: SEDUC 2025', ha='center', fontsize=10)

    # Ajusta o layout
    plt.subplots_adjust(bottom=0.1)

    # Salva o gráfico
    output_path = 'output/alunos_vs_docentes.png'
    plt.savefig(output_path)

    print(f"Gráfico salvo em {output_path}")

if __name__ == '__main__':
    plot_alunos_vs_docentes()