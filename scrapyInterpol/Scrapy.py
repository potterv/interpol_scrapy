import requests
from notices.filter import FilterCriteria

from config import ConfigProxy
from bs4 import BeautifulSoup

from playwright.sync_api import sync_playwright


class Scrapy():
    __url:str
    __filter: FilterCriteria
    __ConfP: ConfigProxy
    def __init__(self, url,proxy):
        self.__url = url
        self.__ConfP = proxy

    def read(self):
       proxy={
            "http": '10.92.192.51:3128',
            "https": '10.92.192.51:3128',
            "ftp": '10.92.192.51:3128'
       }

       s = requests.Session()
       r = requests.get(self.__url, proxies= proxy)
       print(r.cookies)

       if r.status_code == 200:
           print('or')
           # print(r.content)
           soup = BeautifulSoup(r.text,'html.parser')
           # print(soup.prettify())

           print(soup.find_all('a'))

    def test(self):
           with sync_playwright() as p:
               proxy_to_use = {
                   'server': '10.92.192.51:3128'
               }
               browser = p.firefox.launch(proxy=proxy_to_use,slow_mo=1000)

               page = browser.new_page()
               url = "https://www.interpol.int/How-we-work/Notices/View-Yellow-Notices"
               # 'https://www.interpol.int/How-we-work/Notices/View-Yellow-Notices'
               page.goto(url)
               central = page.query_selector('div.redNoticeItem__labelText');

               print({'central': central.inner_html()})
               central.click()
               print(central.inner_html())
               href=central.query_selector('a').get_attribute('href')
               print(f'url: {url}/{href}')
               central = page.query_selector('li.nextElement')
               central.click()
               print(central.inner_html())
               # print(expect(central).to_have_attribute("href"))

               central = page.query_selector('div.redNoticeItem__labelText');
               print({'central': central.inner_html()})
               central = page.query_selector('li.nextElement')
               print(central.inner_html())
               browser.close()