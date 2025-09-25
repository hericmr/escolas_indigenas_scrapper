
import pandas as pd
import os

def analyze_student_distribution():
    """
    Analyzes and prints the distribution of schools by the number of students.
    """
    # Read the data
    csv_path = os.path.join('base_de_dados', 'escolas.csv')
    df = pd.read_csv(csv_path)

    # Convert 'Total_Alunos' to numeric, coercing errors to NaN and then filling with 0
    df['Total_Alunos'] = pd.to_numeric(df['Total_Alunos'], errors='coerce').fillna(0)

    # Define the bins and labels for the student count ranges
    bins = [0, 10, 25, 50, 100, float('inf')]
    labels = ['Até 10 alunos', '11 a 25 alunos', '26 a 50 alunos', '51 a 100 alunos', 'Mais de 100 alunos']

    # Create a new column with the student count category
    df['Faixa_Alunos'] = pd.cut(df['Total_Alunos'], bins=bins, labels=labels, right=True)

    # Count the number of schools in each category
    distribution = df['Faixa_Alunos'].value_counts().sort_index()

    # Print the result as a markdown table
    print("Distribuição de Escolas por Número de Alunos")
    print("| Faixa de Alunos      | Número de Escolas |")
    print("|----------------------|-------------------|")
    # Use a dictionary to map the labels to the desired output order and format
    output_order = {
        'Até 10 alunos': 'Até 10 alunos',
        '11 a 25 alunos': '11 - 25 alunos',
        '26 a 50 alunos': '26 - 50 alunos',
        '51 a 100 alunos': '51 - 100 alunos',
        'Mais de 100 alunos': 'Mais de 100 alunos'
    }
    for label in labels:
        if label in distribution.index:
            count = distribution[label]
            # Format the output string for alignment
            print(f"| {output_order.get(label, label):<20} | {count:<17} |")

if __name__ == '__main__':
    analyze_student_distribution()
