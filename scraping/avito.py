import requests
import time

from datetime import datetime
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

from working_file.save_to_file import save_data_avito_file

# Generation of user agents and acceptances
ua = UserAgent()

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'User-Agent': ua.random
}

# The task of a proxy for scraping
proxies = {
    'https': 'http://209.141.36.83:3317'
}


def avito_realty_scraping(url: str):
    #
    total_card = 0
    error_connecting = 0

    # Time start program
    time1 = datetime.now().time()

    #
    print(url)

    # Getting the page and checking the status code
    response = requests.get(url, headers=headers, proxies=proxies)
    print(f"[{datetime.now().time()}]\tCheck Main Link Status Code: {response.status_code}" + "\n")

    #
    time.sleep(3)

    #  Checking the status of the page code if 200 then Scraping begins
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        # Dynamic class_ | 'iva-item-sliderLink-uLz1v'
        all_link = soup.find_all("a", class_="iva-item-sliderLink-uLz1v")

        #
        total_card = len(all_link)

        # The beginning of the search for links
        for link in all_link:
            link = ("https://www.avito.ru" + link["href"])
            _link = link
            # Getting the status code of the pages that were pulled from the links
            response_link = requests.get(link, headers=headers, proxies=proxies)
            print(f"[{datetime.now().time()}]\tCheck Child Link: {response_link.status_code}")

            # The program falls asleep in order to slow down the ip ban
            time.sleep(3)

            # Checking the status of the page code if 200 then Scraping begins
            if response_link.status_code == 200:
                soup_link = BeautifulSoup(response_link.text, 'lxml')

                # Getting the time when the product card was added to the board
                card_adding_time = soup_link.find('div', class_='style-item-footer-Ufxh_').text

                # Getting the name of the product card
                card_name = soup_link.find('span', class_='title-info-title-text').text

                # Dynamic class_
                card_price = soup_link.find('span', class_='style-price-value-main-TIg6u')

                # Checking the code for the presence of card_price
                if card_price is not None:
                    card_price = card_price.text
                else:
                    card_price = 'The price is not specified'

                # Dynamic class_
                card_about = soup_link.find('div', class_='style-item-view-block-SEFaY style-item-view-params-iniLD style-new-style-iX7zV')

                # Checking the code for the presence of card_about
                if card_about is not None:
                    card_about = card_about.text
                else:
                    card_about = "None About"

                # Dynamic class_
                card_rules = soup_link.find('div', class_='style-item-params-xx_h_')

                # Checking the code for the presence of card_rules
                if card_rules is not None:
                    card_rules = card_rules.text
                else:
                    card_rules = "No rules"

                # Dynamic class_
                card_address = soup_link.find('div', class_='style-item-map-location-wbfMT').text

                #
                card_description = soup_link.find('div', class_='style-item-description-pL_gy').text

                # Save data CSV
                save_data_avito_file(card_adding_time, card_name, card_price, "---", card_about, card_rules,
                                     card_address, card_description, "---", datetime.now(), _link)
                time.sleep(5)

            #
            else:
                error_connecting += 1

    #
    else:
        error_connecting += 1
    print(f"Start: {time1} | End {datetime.now().time()} | Total card: {total_card}| Error: {error_connecting}")
