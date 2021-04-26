from backend.search_engine import Search


class YandexSearch(Search):
    start_url = 'https://yandex.ru'
    input_element_name = 'text'
    x_path = '//*[@id="search-result"]/li/div/h2/a'
    pager_class = 'link_target_serp'
