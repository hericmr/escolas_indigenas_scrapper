import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_escolas_por_diretoria():
    """
    Analisa e plota o número de escolas por 'Diretoria de Ensino' como um gráfico de barras horizontais.
    """
    # Usa um estilo mais moderno
    plt.style.use('seaborn-v0_8-darkgrid')

    # Lê os dados
    csv_path = os.path.join('base_de_dados', 'escolas.csv')
    df = pd.read_csv(csv_path)

    # Conta as escolas por 'Diretoria'
    diretoria_counts = df['Diretoria'].value_counts().sort_values(ascending=True)

    # Cria o gráfico de barras horizontais
    fig, ax = plt.subplots(figsize=(12, 10))
    diretoria_counts.plot(kind='barh', ax=ax, color='skyblue')

    # Adiciona rótulos e título
    ax.set_xlabel('Número de Escolas')
    ax.set_ylabel('Diretoria de Ensino')
    ax.set_title('Número de Escolas por Diretoria de Ensino', fontsize=16)

    # Adiciona rótulos de dados às barras
    for index, value in enumerate(diretoria_counts):
        ax.text(value, index, str(value), va='center')

    # Ajusta o layout para dar espaço ao texto da fonte
    plt.subplots_adjust(bottom=0.1)

    # Adiciona o texto da fonte
    fig.text(0.5, 0.02, 'Fonte: SEDUC 2025', ha='center', fontsize=10)

    # Salva o gráfico
    output_path = 'output/escolas_por_diretoria.png'
    plt.savefig(output_path)

    print(f"Gráfico salvo em {output_path}")

if __name__ == '__main__':
    plot_escolas_por_diretoria()