import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

def plot_student_distribution():
    """
    Analisa e plota a distribuição de escolas pelo número de alunos como um gráfico de pizza
    com um estilo visual aprimorado.
    """
    # Usa um estilo mais moderno
    plt.style.use('seaborn-v0_8-darkgrid')

    # Lê os dados
    csv_path = os.path.join('base_de_dados', 'escolas.csv')
    df = pd.read_csv(csv_path)

    # Converte 'Total_Alunos' para numérico
    df['Total_Alunos'] = pd.to_numeric(df['Total_Alunos'], errors='coerce').fillna(0)

    # Define os intervalos e rótulos
    bins = [0, 10, 25, 50, 100, float('inf')]
    labels = ['Até 10 alunos', '11 a 25 alunos', '26 a 50 alunos', '51 a 100 alunos', 'Mais de 100 alunos']

    # Cria a coluna de categoria
    df['Faixa_Alunos'] = pd.cut(df['Total_Alunos'], bins=bins, labels=labels, right=True)

    # Obtém a contagem de valores
    distribution = df['Faixa_Alunos'].value_counts().sort_index()

    # Explode todas as fatias um pouco
    explode = [0.05] * len(distribution)

    # Cria o gráfico de pizza
    fig, ax = plt.subplots(figsize=(12, 9))
    colors = plt.get_cmap('viridis')(np.linspace(0, 1, len(distribution)))
    
    def autopct_format(values):
        def my_format(pct):
            total = sum(values)
            val = int(round(pct*total/100.0))
            return f'{pct:.1f}% ({val:d})'
        return my_format

    ax.pie(distribution, labels=distribution.index, autopct=autopct_format(distribution), startangle=140,
           explode=explode, colors=colors)
            
    ax.set_title('Distribuição de Escolas por Número de Alunos', fontsize=16)
    
    # Adiciona o texto da fonte na parte inferior
    fig.text(0.5, 0.05, 'Fonte: SEDUC 2025', ha='center', fontsize=10)
    ax.axis('equal')

    # Salva o gráfico
    output_path = 'output/distribuicao_alunos_final_posicionado_v2.png'
    plt.savefig(output_path, bbox_inches='tight')

    print(f"Gráfico salvo em {output_path}")

if __name__ == '__main__':
    plot_student_distribution()