
from backend import MailSearch, YandexSearch, GoogleSearch

params = { 
    'query': 'Чехия', 
    'recursive': 0, 
    'max_result': 100, 
    'output_mode': 'csv'}


search = MailSearch(headless=False, **params)
search.make_request()
