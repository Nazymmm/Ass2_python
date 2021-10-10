import requests
from bs4 import BeautifulSoup
from selenium import webdriver

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/70.0.3538.77 Safari/537"}
#query = input()

resp = requests.get("https://coinmarketcap.com/currencies/bitcoin/news/",headers =headers).text
soup = BeautifulSoup(resp, "lxml")

inp = input("- You can choose crypto here: ")

url = f'https://coinmarketcap.com/currencies/news/'
driver = webdriver.Firefox()


class Scrapper:
 def pars(x):
        inp = input("- You can choose crypto here: ")
        url = f'https://coinmarketcap.com/currencies/news/'

        driver = webdriver.Firefox()
        driver.get(url)
        page = driver.page_source
        
        page_soup = BeautifulSoup(page, 'html.ass2')

        print(page_soup.findAll('div',{"class": "czQlor"}))

def get_html(self, url):

        r = requests.get(url)

        return r