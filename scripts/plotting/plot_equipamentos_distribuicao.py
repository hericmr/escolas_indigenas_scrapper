import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_equipamentos_distribuicao():
    """
    Analisa e plota a distribuição de tipos de equipamentos pelas escolas.
    """
    # Usa um estilo mais moderno
    plt.style.use('seaborn-v0_8-darkgrid')

    # Lê os dados
    csv_path = os.path.join('base_de_dados', 'equipamentos.csv')
    df = pd.read_csv(csv_path)

    # Soma a 'Quantidade' para cada 'Equipamento'
    equipment_counts = df.groupby('Equipamento')['Quantidade'].sum().sort_values(ascending=True)

    # Cria o gráfico de barras
    fig, ax = plt.subplots(figsize=(12, 10))
    equipment_counts.plot(kind='barh', ax=ax, color='purple')

    # Adiciona rótulos e título
    ax.set_xlabel('Quantidade Total')
    ax.set_ylabel('Tipo de Equipamento')
    ax.set_title('Distribuição de Equipamentos nas Escolas', fontsize=16)

    # Adiciona rótulos de dados às barras
    for index, value in enumerate(equipment_counts):
        ax.text(value, index, str(value), va='center')

    # Adiciona o texto da fonte
    fig.text(0.5, 0.01, 'Fonte: SEDUC 2025', ha='center', fontsize=10)

    # Ajusta o layout
    plt.subplots_adjust(left=0.3, bottom=0.1) # Ajusta a margem esquerda para nomes de equipamentos longos

    # Salva o gráfico
    output_path = 'output/equipamentos_distribuicao.png'
    plt.savefig(output_path)

    print(f"Gráfico salvo em {output_path}")

if __name__ == '__main__':
    plot_equipamentos_distribuicao()