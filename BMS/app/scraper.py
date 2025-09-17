import requests
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def scrape_interest_rates(url):
    """
    Scrapes interest rates from a given URL.
    Assumes interest rates are contained in elements with the class 'interest-rate'.

    Args:
        url (str): The URL of the webpage to scrape interest rates from.

    Returns:
        list: A list of strings representing interest rates found on the page.
    """
    logger.info(f"Scraping interest rates from {url}")
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    rates = [elem.text.strip() for elem in soup.select('.interest-rate')]
    logger.info(f"Found {len(rates)} interest rates")
    return rates


def fetch_exchange_rates():
    """
    Fetches currency exchange rates from x-rates.com for USD.

    Returns:
        dict: A dictionary with currency names as keys and exchange rates as values.
    """
    url = 'https://www.x-rates.com/table/?from=USD&amount=1'
    logger.info(f"Fetching exchange rates from {url}")
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', attrs={'class': 'tablesorter ratesTable'})

    rates = {}
    if table:
        rows = table.find_all('tr')[1:]  # Skip header row
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 2:
                currency = cols[0].text.strip()
                rate = cols[1].text.strip()
                rates[currency] = rate
    logger.info(f"Fetched {len(rates)} exchange rates")
    return rates


if __name__ == "__main__":
    # Example usage for interest rates scraping
    interest_url = "https://example.com/interest-rates"  # Replace with actual URL
    try:
        interest_rates = scrape_interest_rates(interest_url)
        for rate in interest_rates:
            print(rate)
    except requests.RequestException as e:
        logger.error(f"Failed to fetch interest rates: {e}")

    # Example usage for exchange rates fetching
    try:
        exchange_rates = fetch_exchange_rates()
        for currency, rate in exchange_rates.items():
            print(f"{currency}: {rate}")
    except requests.RequestException as e:
        logger.error(f"Failed to fetch exchange rates: {e}")



"""# scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_interest_rates(url):
    
    #Scrapes interest rates from a given URL.
    #Assumes interest rates are in elements with class 'interest-rate'.
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rates = [elem.text for elem in soup.select('.interest-rate')]
    return rates
"""






























'''import requests
from bs4 import BeautifulSoup


def fetch_exchange_rates():
    url = 'https://www.x-rates.com/table/?from=USD&amount=1'
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to load page {url}")

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', attrs={'class': 'tablesorter ratesTable'})

    rates = {}
    if table:
        rows = table.find_all('tr')[1:]  # skip header row
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 2:
                currency = cols[0].text.strip()
                rate = cols[1].text.strip()
                rates[currency] = rate
    return rates


if __name__ == "__main__":
    rates = fetch_exchange_rates()
    for currency, rate in rates.items():
        print(f"{currency}: {rate}")
'''