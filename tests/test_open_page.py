from hw_1.backend import MailSearch, YandexSearch, GoogleSearch


def test_yandex_open_page():

    title_page = 'Яндекс'
    search = YandexSearch(headless=True)
    search.open_page()
    actual_title = search.browser.find_element_by_tag_name('title').parent.title
    search.close()
    assert title_page == actual_title


def test_mail_open_page():

    title_page = 'Mail.ru: почта, поиск в интернете, новости, игры'
    search = MailSearch(headless=True)
    search.open_page()
    actual_title = search.browser.find_element_by_tag_name('title').parent.title
    search.close()
    assert title_page == actual_title


def test_google_open_page():

    title_page = 'Google'
    search = GoogleSearch(headless=True)
    search.open_page()
    actual_title = search.browser.find_element_by_tag_name('title').parent.title
    search.close()
    assert title_page == actual_title
