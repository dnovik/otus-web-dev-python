from backend.search_engine import MailSearch, YandexSearch, GoogleSearch
from logger import logger
import pytest


def test_yandex_collector():
    query = 'Python'
    search = YandexSearch(headless=True, query=query, max_result=20)
    logger.info('running yandex search')
    results = len(search.collect_links())
    logger.info('closing yandex search')
    search.close()
    logger.info(f'comparing {search.max_result} with {results}')
    assert results == search.max_result


def test_mail_collector():
    query = 'Python'
    search = MailSearch(headless=True, query=query, max_result=30)
    logger.info('running mail search')
    results = len(search.collect_links())
    logger.info('closing mail search')
    search.close()
    logger.info(f'comparing {search.max_result} with {results}')
    assert results == search.max_result


def test_google_collector():
    query = 'Python'
    search = GoogleSearch(headless=True, query=query, max_result=40)
    logger.info('running google search')
    results = len(search.collect_links())
    logger.info('closing google search')
    search.close()
    logger.info(f'comparing {search.max_result} with {results}')
    assert results == search.max_result
