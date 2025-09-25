import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_tipos_ensino():
    """
    Analisa e plota o número de escolas que oferecem diferentes tipos de ensino.
    """
    # Usa um estilo mais moderno
    plt.style.use('seaborn-v0_8-darkgrid')

    # Lê os dados
    csv_path = os.path.join('base_de_dados', 'turmas_por_tipo.csv')
    df = pd.read_csv(csv_path)

    # Colunas para analisar
    tipos_ensino = [
        'Anos_Iniciais',
        'Anos_Finais',
        'EJA_Anos_Iniciais',
        'EJA_Anos_Finais',
        'EJA_Ensino_Medio',
        'Ensino_Infantil'
    ]

    # Conta as escolas para cada tipo
    counts = {}
    for tipo in tipos_ensino:
        # Preenche valores NaN com 0 antes de converter para numérico
        df[tipo] = pd.to_numeric(df[tipo], errors='coerce').fillna(0)
        counts[tipo] = (df[tipo] > 0).sum()

    # Cria um mapeamento para os rótulos
    label_mapping = {
        'Anos_Iniciais': 'Anos Iniciais',
        'Anos_Finais': 'Anos Finais',
        'EJA_Anos_Iniciais': 'EJA Anos Iniciais',
        'EJA_Anos_Finais': 'EJA Anos Finais',
        'EJA_Ensino_Medio': 'EJA Ensino Médio',
        'Ensino_Infantil': 'Ensino Infantil'
    }

    # Cria uma Series do pandas para plotagem e renomeia o índice
    counts_series = pd.Series(counts).rename(index=label_mapping).sort_values(ascending=False)

    # Cria o gráfico de barras
    fig, ax = plt.subplots(figsize=(12, 8))
    counts_series.plot(kind='bar', ax=ax, color='coral')

    # Adiciona rótulos e título
    ax.set_xlabel('Tipo de Ensino')
    ax.set_ylabel('Número de Escolas')
    ax.set_title('Número de Escolas por Tipo de Ensino Oferecido', fontsize=16)
    plt.xticks(rotation=45, ha='right')

    # Adiciona rótulos de dados às barras
    for i, v in enumerate(counts_series):
        ax.text(i, v + 0.1, str(v), ha='center', va='bottom')

    # Ajusta o layout para dar espaço ao texto da fonte
    plt.subplots_adjust(bottom=0.2)

    # Adiciona o texto da fonte
    fig.text(0.5, 0.02, 'Fonte: SEDUC 2025', ha='center', fontsize=10)

    # Salva o gráfico
    output_path = 'output/tipos_ensino.png'
    plt.savefig(output_path)

    print(f"Gráfico salvo em {output_path}")

if __name__ == '__main__':
    plot_tipos_ensino()