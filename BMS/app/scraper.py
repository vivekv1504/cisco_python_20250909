import requests
from bs4 import BeautifulSoup

def scrape_interest_rates(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Example: get all interest rates found on page (customize as needed)
    rates = [elem.text for elem in soup.select('.interest-rate')]
    return rates
