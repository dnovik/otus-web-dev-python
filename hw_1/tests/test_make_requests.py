from backend.search_engine import MailSearch, YandexSearch, GoogleSearch


def test_yandex_request():

    query = 'Python'
    search = YandexSearch(headless=True, query=query)
    search.open_page()
    search.make_request()
    title = search.browser.find_element_by_tag_name('title').parent.title
    search.close()
    assert query in title


def test_mail_request():

    query = 'Python'
    search = MailSearch(headless=True, query=query)
    search.open_page()
    search.make_request()
    title = search.browser.find_element_by_tag_name('title').parent.title
    search.close()
    assert query in title


def test_google_request():

    query = 'Python'
    search = GoogleSearch(headless=True, query=query)
    search.open_page()
    search.make_request()
    title = search.browser.find_element_by_tag_name('title').parent.title
    search.close()
    assert query in title
