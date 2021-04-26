import csv
import json
from typing import Dict, Union

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
        return self.browser.find_elements_by_class_name(self.pager_class)[-1] \
            .get_attribute('href')

    def collect_links(self):

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
        link_list = self.collect_links()
        with open('results/links.csv', 'w',
                  encoding='cp1251', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            for link in link_list:
                text, url = link[0], link[1]
                writer.writerow([text, url])

        print('Готово!')

    def get_result_in_json(self):
        link_list = self.collect_links()
        links = dict()
        for lines in link_list:
            links[lines[0]] = lines[1]

        with open('results/links.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(links, ensure_ascii=False, indent=2))

        print('Готово!')

    def get_result_in_cli(self):
        link_list = self.collect_links()
        for lines in link_list:
            print(f'{lines[0]}: {lines[1]}\n')


class YandexSearch(Search):
    start_url = 'https://yandex.ru'
    input_element_name = 'text'
    x_path = '//*[@id="search-result"]/li/div/h2/a'
    pager_class = 'link_target_serp'

    def __init__(
            self,
            **kwargs: Dict):
        super().__init__(**kwargs)


class MailSearch(Search):
    start_url = 'https://mail.ru'
    input_element_name = 'q'
    x_path = '//*[@class="SnippetResultTitle-title result__title"]/a'
    pager_class = 'PageNavigator-itemBlock'

    def __init__(
            self,
            **kwargs: Dict):
        super().__init__(**kwargs)


class GoogleSearch(Search):
    start_url = 'https://google.ru'
    input_element_name = 'q'
    x_path = '//*[@class="yuRUbf"]/a'
    pager_class = 'd6cvqb'

    def __init__(
            self,
            **kwargs: Dict):
        super().__init__(**kwargs)

    def get_next_page_url(self):
        return self.browser.find_element_by_id('pnnext') \
            .get_attribute('href')
