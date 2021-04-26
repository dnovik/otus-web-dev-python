from backend.search_engine import Search


class MailSearch(Search):
    start_url = 'https://mail.ru'
    input_element_name = 'q'
    x_path = '//*[@class="SnippetResultTitle-title result__title"]/a'
    pager_class = 'PageNavigator-itemBlock'
