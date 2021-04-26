from backend.search_engine import Search


class GoogleSearch(Search):
    start_url = 'https://google.ru'
    input_element_name = 'q'
    x_path = '//*[@class="yuRUbf"]/a'
    pager_class = 'd6cvqb'

    def get_next_page_url(self):
        return (self.browser.find_element_by_id('pnnext')
                .get_attribute('href'))
