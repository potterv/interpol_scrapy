from scrapy.filter import FilterCriteria

from playwright.sync_api import sync_playwright,Page,


class Scrapy():
    __url:str
    __filter: FilterCriteria
    __proxy: str
    def __init__(self, url,proxy=None):
        self.__url = url
        self.__proxy = proxy


    def test(self):
           with sync_playwright() as p:

               proxy_to_use = {
                   'server':self.__proxy
               }
               len(proxy_to_use)

               if self.__proxy==None:
                   browser = p.firefox.launch(slow_mo=1000)
               else:
                   browser = p.firefox.launch(proxy=proxy_to_use, slow_mo=1000)

               page = browser.new_page()
               url = "https://www.interpol.int/How-we-work/Notices/View-Yellow-Notices"
               # 'https://www.interpol.int/How-we-work/Notices/View-Yellow-Notices'
               page.goto(url)
               central =  await page.getByRole('textbox').fill('Peter');

               page.query_selector('button.btn').click()
               page_num=0
               page_site = 1

               page_prev = 0
               while page_num<=page_site:
                   central = page.query_selector_all('div.redNoticesList__item');
                   for cont in central:
                       print(cont.inner_text())
                       href = cont.query_selector('a').get_attribute('href')
                       print(f'id_person {href[1:]} url: {url}/{href}')
                   page_num = page_site
                   print(page_num)
                   central = page.query_selector('li.nextElement')
                   print (central.as_element())
                   central.click()
                   page_site = int(page.query_selector('a.active').inner_text())
                   print(page_site)



               # print({'central': central.inner_html()})
               # central.click()
               # print(central.inner_html())
               # href=central.query_selector('a').get_attribute('href')
               # print(f'url: {url}/{href}')
               # central = page.query_selector('li.nextElement')
               # central.click()
               # print(central.inner_html())
               # # print(expect(central).to_have_attribute("href"))
               #
               # central = page.query_selector('div.redNoticeItem__labelText');
               # print({'central': central.inner_html()})
               # central = page.query_selector('li.nextElement')
               # print(central.inner_html())
               # browser.close()