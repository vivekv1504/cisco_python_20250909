# scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_interest_rates(url):
    """
    Scrapes interest rates from a given URL.
    Assumes interest rates are in elements with class 'interest-rate'.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rates = [elem.text for elem in soup.select('.interest-rate')]
    return rates
