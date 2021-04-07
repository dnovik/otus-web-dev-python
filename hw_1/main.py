import requests

"""
 Пользователь вводит текст запроса, поисковую систему (google.com, yandex.ru, ...), 
 количество результатов, рекурсивный поиск или нет, 
 формат вывода (в консоль, в файл json, в csv) 
 Программа находит в интернете начиная от стартовой точки все ссылки на веб-странице в заданном количестве (название ссылки и саму ссылку) 
 Если поиск не рекурсивный, то берем ссылки только из поисковика, если рекурсивный, то берем первую ссылку, переходим, находим там ссылки, переходим, ... 
 В зависимости от выбранного формата вывода сохраняем результат (текст ссылки: ссылка) либо в консоль либо в файл выбранного формата"""

 
''' def get_links(
     search_type: str, 
     max_result: int, 
     output_mode: str):
     '''



def make_yandex_search(query):

    base_url = 'https://yandex.ru/search/'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0'}

    params = {
        'lr': 213,
        'text': query
    }
    response = requests.post(base_url, headers=headers, params=params)
    
    return response.url




def make_google_search(query):

    base_url = 'https://www.google.com/search'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0'}

    params = {
        'q': query
    }
    response = requests.post(base_url, headers=headers, params=params)
    
    return response.url


print(make_google_search('Дом с привидениями'))
