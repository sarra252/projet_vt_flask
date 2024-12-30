import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

#def scrape_data():
    url = 'https://dataprotection.ie'
    soup = fetch_data(url)
    data = []
    for item in soup.find_all('div', class_='item'):
        title = item.find('h2').text
        data.append({'title': title})
    return data


# scraper/scraper.py
def scrape_data():
    # Retourner seulement deux articles pour le test
    return [
        {'title': 'Article 1', 'summary': 'Summary of article 1', 'date': '2024-01-01', 'url': 'https://dataprotection.ie'},
        {'title': 'Article 2', 'summary': 'Summary of article 2', 'date': '2024-01-02', 'url': 'https://dataprotection.ie'}
    ]

# Testez cette fonction séparément
#if __name__ == "__main__":
    print(scrape_data())