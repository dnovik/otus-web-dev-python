
from backend.search_engine import MailSearch, \
    YandexSearch, GoogleSearch


def get_engine(engine):

    engines = {
        'mail': MailSearch,
        'яндекс': YandexSearch,
        'google': GoogleSearch
    }

    return engines[engine]


def main():
    query = input('Что будем искать: ')
    try:
        engine = get_engine(input('В какой системе вести поиск (Яндекс, Mail, Google): ').lower())
    except KeyError:
        print('Вы ввели неизвестный поисковик')
        print('Выберите 1 из 3 предложенных')
        engine = get_engine(input('В какой системе вести поиск (Яндекс, Mail, Google): ').lower())
    try:
        max_results = int(input('Какое максимальное кол-во ссылок нужно собрать: '))
    except ValueError:
        print('Похоже вы ввели не число, попробуйте еще раз')
        max_results = int(input('Какое максимальное кол-во ссылок нужно собрать: '))
    output_mode = input('В каком виде вывести результат(console, csv, json): ').lower()
    print('Выполняю...')

    search = engine(query=query, max_result=max_results)
    if output_mode == 'csv':
        search.get_result_in_csv()
    elif output_mode == 'json':
        search.get_result_in_json()
    else:
        search.get_result_in_cli()
    search.close()


if __name__ == '__main__':
    main()