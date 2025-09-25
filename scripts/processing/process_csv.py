import csv

input_file = 'base_de_dados/escolas_eei.csv'
output_file = 'data/escolas_selecionadas.csv'
columns_to_keep = ['NOMESC', 'CD_ESCOLA']
base_url = 'https://transparencia.educacao.sp.gov.br/Home/DetalhesEscola?codesc='

try:
    with open(input_file, 'r', encoding='utf-8-sig') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile)

        # Lê a linha do cabeçalho
        header = next(reader)

        # Encontra os índices das colunas a serem mantidas
        indices = [header.index(col) for col in columns_to_keep]
        cd_escola_index = header.index('CD_ESCOLA')

        # Escreve o novo cabeçalho
        writer.writerow(columns_to_keep + ['link'])

        processed_schools = set()
        # Escreve as linhas de dados
        for row in reader:
            school_code = row[cd_escola_index]
            school_tuple = tuple([row[i] for i in indices])
            
            if school_tuple not in processed_schools:
                link = base_url + school_code
                new_row = [row[i] for i in indices] + [link]
                writer.writerow(new_row)
                processed_schools.add(school_tuple)

    print(f"Arquivo '{output_file}' criado com sucesso, com escolas únicas e uma coluna de link.")

except FileNotFoundError:
    print(f"Erro: O arquivo não foi encontrado em '{input_file}'")
except ValueError as e:
    print(f"Erro: {e}. Verifique se as colunas especificadas existem no arquivo de entrada.")