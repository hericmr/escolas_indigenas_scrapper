
import requests
from bs4 import BeautifulSoup
import csv

def scrape_school_data(school_code):
    """
    Scrapes data for a given school code from the transparencia.educacao.sp.gov.br website.

    Args:
        school_code (int): The school code (codesc).

    Returns:
        dict: A dictionary containing the scraped school data, or None if an error occurs.
    """
    url = f"https://transparencia.educacao.sp.gov.br/Home/DetalhesEscola?codesc={school_code}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    
    data = {}

    # School Details
    details_card = soup.find('div', class_='card-body')
    print(f'details_card: {details_card}')
    if details_card:
        data['Nome da Escola'] = details_card.find('h4', class_='card-title').text.strip() if details_card.find('h4', class_='card-title') else 'N/A'
        
        # Extracting details from the list
        details_list = details_card.find_all('p', class_='card-text')
        for p in details_list:
            text = p.text.strip()
            if 'Tipo:' in text:
                data['Tipo'] = text.split('Tipo:')[1].strip()
            elif 'Código CIE:' in text:
                data['Código CIE'] = text.split('Código CIE:')[1].strip()
            elif 'Diretoria de Ensino:' in text:
                data['Diretoria de Ensino'] = text.split('Diretoria de Ensino:')[1].strip()
            elif 'Endereço:' in text:
                data['Endereço'] = text.split('Endereço:')[1].strip()
            elif 'E-mail:' in text:
                data['E-mail'] = text.split('E-mail:')[1].strip()
            elif 'Vice-Diretor(a):' in text:
                data['Vice-Diretor(a)'] = text.split('Vice-Diretor(a):')[1].strip()


    # Student Information
    students_card = soup.find('div', class_='card-body text-center')
    print(f'students_card: {students_card}')
    if students_card:
        data['Total de Alunos'] = students_card.find_all('h3')[0].text.strip() if len(students_card.find_all('h3')) > 0 else 'N/A'
        data['Total de Turmas'] = students_card.find_all('h3')[1].text.strip() if len(students_card.find_all('h3')) > 1 else 'N/A'

    # Age Range
    age_range_chart = soup.find('canvas', {'id': 'chartFaixaEtaria'})
    if age_range_chart:
        # This part is tricky as the data is in a script tag.
        # For this example, we will skip it as it requires more advanced parsing.
        pass

    # Infrastructure
    infra_card = None
    all_cards = soup.find_all('div', class_='card')
    for card in all_cards:
        title = card.find('h5', class_='card-title')
        if title and 'Infraestrutura' in title.text:
            infra_card = card.find('div', class_='card-body')
            break
    print(f'infra_card: {infra_card}')

    if infra_card:
        items = infra_card.find_all('div', class_='col-md-4')
        if len(items) > 0:
            data['Salas de Aula'] = items[0].find('h3').text.strip()
        if len(items) > 1:
            data['Cozinhas'] = items[1].find('h3').text.strip()
        if len(items) > 2:
            data['Banheiros para Alunos'] = items[2].find('h3').text.strip()


    return data

def save_to_csv(data, filename='escolas.csv'):
    """
    Saves a list of school data dictionaries to a CSV file.

    Args:
        data (list): A list of dictionaries, where each dictionary represents a school's data.
        filename (str): The name of the CSV file to save.
    """
    if not data:
        print("No data to save.")
        return

    # Make sure all dictionaries have the same keys
    fieldnames = sorted(list(set(key for d in data for key in d.keys())))
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to {filename}")


if __name__ == '__main__':
    school_codes = [469774]  # Start with the test school code
    
    # You can add more school codes to this list to scrape multiple schools
    # school_codes.extend([123456, 789012]) 

    all_school_data = []
    for code in school_codes:
        print(f"Scraping school with code: {code}")
        school_data = scrape_school_data(code)
        if school_data:
            all_school_data.append(school_data)
            print("Scraping successful.")
            print(school_data)
        else:
            print(f"Failed to scrape school with code: {code}")
        print("-" * 20)

    if all_school_data:
        save_to_csv(all_school_data, 'base_de_dados/escolas.csv')
