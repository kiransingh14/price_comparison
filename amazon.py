  
from lxml import html
import csv, os, json
import requests

from time import sleep
import urllib

AsinList = []
extracted_data_amazon_india = []
amazindialist = []


def AmazonParser(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0 '}
    page = requests.get(url, headers=headers)
    while True:
        sleep(2)
        try:
            doc = html.fromstring(page.content)
            XPATH_NAME = '//h1[@id="title"]//text()'
            XPATH_SALE_PRICE = '//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()'
            XPATH_ORIGINAL_PRICE = '//td[contains(text(),"List Price") or contains(text(),"M.R.P") or contains(text(),"Price")]/following-sibling::td/text()'
            XPATH_CATEGORY = '//a[@class="a-link-normal a-color-tertiary"]//text()'
            XPATH_AVAILABILITY = '//div[@id="availability"]//text()'
            site = "Amazon.in"
            RAW_NAME = doc.xpath(XPATH_NAME)
            RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
            RAW_CATEGORY = doc.xpath(XPATH_CATEGORY)
            RAW_ORIGINAL_PRICE = doc.xpath(XPATH_ORIGINAL_PRICE)
            RAw_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)

            NAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
            SALE_PRICE = ' '.join(''.join(RAW_SALE_PRICE).split()).strip() if RAW_SALE_PRICE else None
            CATEGORY = ' > '.join([i.strip() for i in RAW_CATEGORY]) if RAW_CATEGORY else None
            ORIGINAL_PRICE = ''.join(RAW_ORIGINAL_PRICE).strip() if RAW_ORIGINAL_PRICE else None
            AVAILABILITY = ''.join(RAw_AVAILABILITY).strip() if RAw_AVAILABILITY else None

            if not ORIGINAL_PRICE:
                ORIGINAL_PRICE = SALE_PRICE

            if page.status_code != 200:
                raise ValueError('captha')
            data = {
                'NAME': NAME,
                'SALE_PRICE': SALE_PRICE,
                'CATEGORY': CATEGORY,
                'ORIGINAL_PRICE': ORIGINAL_PRICE,
                'AVAILABILITY': AVAILABILITY,
                'URL': url,
                'SITE': site,
            }

            return data
        except ValueError:
            print("e") 


def ReadAsin(link):
    # AsinList = csv.DictReader(open(os.path.join(os.path.dirname(__file__),"Asinfeed.csv")))
    url = "http://www.amazon.in/dp/" + link
    print("Processing: " + url)
    extracted_data_amazon_india.append(AmazonParser(url))
    sleep(2)


def initialamazon_India(data):
    counterinamazon=0
    urlprod = "http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + data
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0 '}
    page = requests.get(urlprod, headers=headers)
    dom = html.fromstring(page.content)
    for link in dom.xpath('//li[@id="result_0"]/@data-asin'):  # select the url in href for all a tags(links)
        if counterinamazon < 1:
            print(link)
            ReadAsin(link)
            counterinamazon = 1