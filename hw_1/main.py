
from backend import MailSearch, YandexSearch, GoogleSearch

params = { 
    'query': 'Динамо',
    'recursive': 0, 
    'max_result': 100, 
    'output_mode': 'csv'}


search = MailSearch(headless=False, **params)
links = search.collect_links()
search.close()
