import csv
import json
from typing import Union

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class Search:
    start_url = None
    input_element_name = None
    next_page_element_name = None
    x_path = None
    pager_class = None

    def __init__(
            self,
            **kwargs: Union[str, None, int, bool]):

        self.headless = kwargs.get('headless', True)
        self.query = kwargs.get('query')
        self.max_result = kwargs.get('max_result')

        if self.headless:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            self.browser = webdriver.Chrome(chrome_options=chrome_options)
        else:
            self.browser = webdriver.Chrome()

    def close(self):
        self.browser.close()

    def open_page(self, url: str = None) -> None:
        '''open default page or input url'''

        if url:
            self.browser.get(url)
        else:
            self.browser.get(self.start_url)

    def make_request(self) -> None:
        '''submit input query in search field of selected search system'''

        self.open_page()
        input_field = self.browser.find_element_by_name(
            self.input_element_name)
        input_field.send_keys(self.query)
        input_field.send_keys(Keys.RETURN)

    def get_next_page_url(self):
        '''return url of next page'''
        return self.browser.find_elements_by_class_name(self.pager_class)[-1] \
            .get_attribute('href')

    def collect_links(self):
        '''return list of collected links'''
        links = []
        self.make_request()
        elements = self.browser.find_elements_by_xpath(self.x_path)
        texts = [el.text for el in elements]
        url = [el.get_attribute('href') for el in elements]
        links.extend(zip(texts, url))

        while len(links) <= self.max_result:
            self.browser.get(self.get_next_page_url())
            elements = self.browser.find_elements_by_xpath(self.x_path)
            texts = [el.text for el in elements]
            url = [el.get_attribute('href') for el in elements]
            links.extend(zip(texts, url))

        return links[:self.max_result]

    def get_result_in_csv(self):
        '''create csv file and write collected links into the file'''
        link_list = self.collect_links()
        with open('results/links.csv', 'w',
                  encoding='cp1251', newline='') as f:
            print('Записываю данные в results/links.csv')
            writer = csv.writer(f, delimiter=';')
            for link in link_list:
                text, url = link[0], link[1]
                writer.writerow([text, url])

        print('Готово!')

    def get_result_in_json(self):
        '''create json file and write collected links into the file'''
        link_list = self.collect_links()
        links = dict()
        for lines in link_list:
            links[lines[0]] = lines[1]

        with open('results/links.json', 'w', encoding='utf-8') as f:
            print('Записываю данные в results/links.json')
            f.write(json.dumps(links, ensure_ascii=False, indent=2))

        print('Готово!')

    def get_result_in_cli(self):
        '''return found results in console'''
        link_list = self.collect_links()
        print('Найдены следующие ссылки: ')
        for lines in link_list:
            print(f'{lines[0]}: {lines[1]}\n')
