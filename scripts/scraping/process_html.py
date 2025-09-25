import os
import csv
from bs4 import BeautifulSoup
import re

def get_text_or_na(element):
    return element.text.strip() if element else 'N/A'

def process_html_files():
    output_dir = 'base_de_dados'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    csv_files = {
        'escolas': ['CIE', 'Nome', 'Tipo', 'Diretoria', 'Endereço', 'Bairro', 'Município', 'Telefone', 'Email', 'Total_Alunos', 'Total_Turmas'],
        'gestores': ['CIE_Escola', 'Função', 'Nome'],
        'docentes': ['CIE_Escola', 'Função', 'Disciplina', 'Módulo', 'Nome'],
        'infraestrutura': ['CIE_Escola', 'Ambiente', 'Item', 'Quantidade'],
        'equipamentos': ['CIE_Escola', 'Grupo', 'Equipamento', 'Quantidade'],
        'servicos': ['CIE_Escola', 'Serviço', 'Detalhe'],
        'vacinacao': ['CIE_Escola', 'Grupo', 'Status', 'Valor'],
        'alunos_faixa_etaria': ['CIE_Escola', 'Faixa_Etaria', 'Anos_Iniciais', 'Anos_Finais', 'EJA_Anos_Iniciais', 'EJA_Anos_Finais', 'EJA_Ensino_Medio', 'Ensino_Infantil'],
        'turmas_por_tipo': ['CIE_Escola', 'Anos_Iniciais', 'Anos_Finais', 'EJA_Anos_Iniciais', 'EJA_Anos_Finais', 'EJA_Ensino_Medio', 'Ensino_Infantil']
    }

    for filename, headers in csv_files.items():
        filepath = os.path.join(output_dir, f"{filename}.csv")
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow(headers)

    html_dir = 'data/html'
    for html_filename in os.listdir(html_dir):
        if not html_filename.endswith('.html'):
            continue

        filepath = os.path.join(html_dir, html_filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

        cie_element = soup.find(string=re.compile(r'Código identificador da escola \(CIE\):'))
        cie = cie_element.split(':')[1].strip() if cie_element else 'N/A'
        if cie == 'N/A':
            print(f"Could not find CIE for {html_filename}, skipping...")
            continue

        # --- ESCOLAS ---
        nome = get_text_or_na(soup.find('h2', class_='escola-titulo'))
        tipo = get_text_or_na(soup.find('p', class_=re.compile(r'tags EEI -')))
        diretoria = get_text_or_na(soup.find(string=re.compile(r'Diretoria de Ensino:'))).split(':')[-1].strip()
        endereco = get_text_or_na(soup.find(string=re.compile(r'RUA .* CEP:')))
        bairro = get_text_or_na(soup.find(string=re.compile(r'Bairro:'))).split(':')[-1].strip()
        municipio = get_text_or_na(soup.find(string=re.compile(r'Município:'))).split(':')[-1].strip()
        telefone = get_text_or_na(soup.find(string=re.compile(r'\(\d{2}\)')))
        email = get_text_or_na(soup.find(string=re.compile(r'[A-Z0-9._%+-]+@EDUCACAO\.SP\.GOV\.BR')))
        total_alunos = get_text_or_na(soup.find('div', class_='alunos').find('span', class_='numero-alunos'))
        total_turmas_element = soup.find('h2', string='Total de Turmas')
        total_turmas = 'N/A'
        if total_turmas_element:
            total_turmas = get_text_or_na(total_turmas_element.find_next('div', class_='dados-alunos').find('span', class_='numero-alunos'))
        escola_row = [cie, nome, tipo, diretoria, endereco, bairro, municipio, telefone, email, total_alunos, total_turmas]
        with open(os.path.join(output_dir, 'escolas.csv'), 'a', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow(escola_row)

        # --- GESTORES ---
        gestores_table = soup.find('h2', string='Gestores')
        if gestores_table:
            for row in gestores_table.find_next('table').find('tbody').find_all('tr'):
                cols = row.find_all('td')
                gestor_row = [cie, get_text_or_na(cols[0]), get_text_or_na(cols[1])]
                with open(os.path.join(output_dir, 'gestores.csv'), 'a', newline='', encoding='utf-8') as f:
                    csv.writer(f).writerow(gestor_row)

        # --- DOCENTES ---
        docentes_table = soup.find('h2', string='Docentes')
        if docentes_table:
            for row in docentes_table.find_next('table').find('tbody').find_all('tr'):
                cols = row.find_all('td')
                docente_row = [cie, get_text_or_na(cols[0]), get_text_or_na(cols[1]), get_text_or_na(cols[2]), get_text_or_na(cols[3])]
                with open(os.path.join(output_dir, 'docentes.csv'), 'a', newline='', encoding='utf-8') as f:
                    csv.writer(f).writerow(docente_row)

        # --- INFRAESTRUTURA ---
        infra_section = soup.find('div', class_='infraestrutura-escola')
        if infra_section:
            for box in infra_section.find_all('div', class_='box'):
                ambiente = get_text_or_na(box.find('b'))
                for item in box.find_all('li'):
                    parts = item.text.strip().split()
                    quantidade = parts[0]
                    nome_item = ' '.join(parts[1:])
                    infra_row = [cie, ambiente, nome_item, quantidade]
                    with open(os.path.join(output_dir, 'infraestrutura.csv'), 'a', newline='', encoding='utf-8') as f:
                        csv.writer(f).writerow(infra_row)

        # --- EQUIPAMENTOS ---
        equip_section = soup.find('div', class_='equipamentos-escola')
        if equip_section:
            for grupo_equip in equip_section.find_all('div', class_='equipamentos'):
                grupo = get_text_or_na(grupo_equip.find('h5'))
                for box in grupo_equip.find_all('div', class_='box'):
                    equipamento = get_text_or_na(box.find('span'))
                    quantidade = get_text_or_na(box.find('b')).split()[0]
                    equip_row = [cie, grupo, equipamento, quantidade]
                    with open(os.path.join(output_dir, 'equipamentos.csv'), 'a', newline='', encoding='utf-8') as f:
                        csv.writer(f).writerow(equip_row)

        # --- SERVICOS ---
        servicos_section = soup.find('div', class_='servicos-oferecidos-escola')
        if servicos_section:
            for box in servicos_section.find_all('div', class_='box'):
                servico = get_text_or_na(box.find('b'))
                detalhe = get_text_or_na(box.find('span', id='numeroServicos'))
                servico_row = [cie, servico, detalhe]
                with open(os.path.join(output_dir, 'servicos.csv'), 'a', newline='', encoding='utf-8') as f:
                    csv.writer(f).writerow(servico_row)

        # --- VACINACAO ---
        vacinacao_section = soup.find('div', class_='vacina-escola-faixa-etaria')
        if vacinacao_section:
            for box in vacinacao_section.find_all('div', class_='box-idades'):
                grupo = get_text_or_na(box.find(class_='topo-idade'))
                for dl in box.find_all('dl'):
                    status = get_text_or_na(dl.find('dt'))
                    valor = get_text_or_na(dl.find('dd'))
                    vacinacao_row = [cie, grupo, status, valor]
                    with open(os.path.join(output_dir, 'vacinacao.csv'), 'a', newline='', encoding='utf-8') as f:
                        csv.writer(f).writerow(vacinacao_row)

        # --- ALUNOS FAIXA ETARIA ---
        alunos_table = soup.find('div', class_='info-alunos')
        if alunos_table and alunos_table.find('table'):
             for row in alunos_table.find('table').find_all('tr')[1:]:
                cols = row.find_all('td')
                faixa_etaria_row = [cie] + [get_text_or_na(c) for c in cols]
                with open(os.path.join(output_dir, 'alunos_faixa_etaria.csv'), 'a', newline='', encoding='utf-8') as f:
                    csv.writer(f).writerow(faixa_etaria_row)

        # --- TURMAS POR TIPO ---
        turmas_table = total_turmas_element.find_next('table') if total_turmas_element else None
        if turmas_table:
            row = turmas_table.find_all('tr')[1]
            cols = row.find_all('td')
            turmas_row = [cie] + [get_text_or_na(c) for c in cols]
            with open(os.path.join(output_dir, 'turmas_por_tipo.csv'), 'a', newline='', encoding='utf-8') as f:
                csv.writer(f).writerow(turmas_row)

    print(f"Processing complete. Data saved in '{output_dir}' directory.")

if __name__ == '__main__':
    process_html_files()