from working_file.creat_to_csv import creat_avito_csv
from scraping.avito import avito_realty_scraping

if __name__ == '__main__':
    creat_avito_csv()
    av_url = 'Your Url'

    avito_realty_scraping(url=av_url)
