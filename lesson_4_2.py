from requests import get, utils

response = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))


def currency_rates(code):
    value_list = response.split('<Valute ID=')
    for i in value_list:
        if code.upper() in i:
            return float(i.replace('/', '').split('<Value>')[-2].replace(',', '.'))


print(currency_rates(input("Введите код валюты: ")))
