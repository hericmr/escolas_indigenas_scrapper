import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_students_per_school():
    """
    Lê os dados da escola, filtra para escolas indígenas e plota o número de alunos por escola.
    """
    # Lê os dados
    csv_path = os.path.join('base_de_dados', 'escolas.csv')
    df = pd.read_csv(csv_path)

    # Filtra para escolas indígenas
    indigenous_schools = df[df['Tipo'] == 'EEI - INDIGENA'].copy()

    # Converte 'Total_Alunos' para numérico, transformando erros em NaN e depois preenchendo com 0
    indigenous_schools['Total_Alunos'] = pd.to_numeric(indigenous_schools['Total_Alunos'], errors='coerce').fillna(0).astype(int)

    # Ordena pelo número de alunos para melhor visualização
    indigenous_schools = indigenous_schools.sort_values(by='Total_Alunos', ascending=False)

    # Cria o gráfico
    plt.figure(figsize=(12, 8))
    bars = plt.bar(indigenous_schools['Nome'], indigenous_schools['Total_Alunos'])

    # Adiciona o número total de alunos no topo de cada barra
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom', ha='center') # va='bottom' para colocar acima da barra

    plt.xlabel('Escola')
    plt.ylabel('Número de Alunos')
    plt.suptitle('Número de Alunos por Escola Indígena', fontsize=16)
    plt.title('Fonte: SEDUC 2025', fontsize=10)
    plt.xticks(rotation=90)
    plt.tight_layout(rect=[0, 0, 1, 0.96]) # Ajusta o layout para dar espaço para o supertítulo

    # Salva o gráfico
    output_path = 'output/alunos_por_escola_com_total.png'
    plt.savefig(output_path)

    print(f"Gráfico salvo em {output_path}")

if __name__ == '__main__':
    plot_students_per_school()