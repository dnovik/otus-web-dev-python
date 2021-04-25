from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from typing import Dict, List
import json
import csv
from pprint import pprint


class Search:

    start_url = None
    input_element_name = None
    next_page_element_name = None
    x_path = None
    pager_class = None

    def __init__(
            self,
            headless: bool = True,
            **kwargs):

        self.headless = headless
        self.query = kwargs.get('query')
        self.recursive = kwargs.get('recursive')
        self.max_result = kwargs.get('max_result')
        self.output_mode = kwargs.get('output_mode')

        if self.headless:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            self.browser = webdriver.Chrome(chrome_options=chrome_options)
        else:
            self.browser = webdriver.Chrome()

    def open_page(self, url: str = None) -> None:

        if url:
            self.browser.get(url)
        else:
            self.browser.get(self.start_url)

    def make_request(self) -> None:

        self.open_page()
        input_field = self.browser.find_element_by_name(self.input_element_name)
        input_field.send_keys(self.query)
        input_field.send_keys(Keys.RETURN)

    def collect_links(self) -> Dict:

        self.make_request()
        elements = self.browser.find_elements_by_xpath(self.x_path)
        texts = [el.text for el in elements]
        url = [el.get_attribute('href') for el in elements]
        links = dict(zip(texts, url))

        while len(links) <= self.max_result:
            next_page_url = self.browser.find_elements_by_class_name(self.pager_class)[-1]\
                .get_attribute('href')
            self.browser.get(next_page_url)
            elements = self.browser.find_elements_by_xpath(self.x_path)
            texts = [el.text for el in elements]
            url = [el.get_attribute('href') for el in elements]
            links.update(dict(zip(texts, url)))

        return links

    def collect_recursively(self) -> Dict:
        
        recursive_links = dict()
        self.open_page()
        self.make_request()
        original_links = self.collect_links()

        for link in original_links:
            self.open_page(link)
            elements = self.browser.find_elements_by_tag_name('a')
            internal_links = [elem.get_attribute('href') for elem in elements if elem not in [None, '']]
            recursive_links[link] = internal_links

        return recursive_links

    @staticmethod
    def get_result_in_json(my_dict):
        with open('links.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(my_dict, ensure_ascii=False, indent=4))

    @staticmethod
    def get_result_in_cli(my_dict):
        pprint(my_dict)

    def close(self):
        self.browser.close()


class YandexSearch(Search):

    start_url = 'https://yandex.ru'
    input_element_name = 'text'
    x_path = '//*[@id="search-result"]/li/div/h2/a'
    pager_class = 'link_target_serp'

    def __init__(
            self,
            headless: bool,
            **kwargs: Dict):
        super().__init__(headless, **kwargs)


class MailSearch(Search):

    start_url = 'https://mail.ru'
    input_element_name = 'q'
    x_path = '//*[@class="SnippetResultTitle-title result__title"]/a'
    pager_class = 'PageNavigator-itemBlock'

    def __init__(
            self,
            headless: bool,
            **kwargs: Dict):
        super().__init__(headless, **kwargs)
    

class GoogleSearch(Search):

    start_url = 'https://google.ru'
    input_element_name = 'q'
    x_path = '//*[@class="yuRUbf"]/a'

    def __init__(
            self,
            headless: bool,
            **kwargs: Dict):
        super().__init__(headless, **kwargs)
