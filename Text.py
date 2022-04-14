import json

import requests


def get_text():
    url = 'http://api.forismatic.com/api/1.0/'
    payload = {'method': 'getQuote', 'format': 'json', 'lang': 'ru'}
    res = requests.get(url, params=payload)
    string = res.text
    res_dict = json.loads(string)
    return res_dict['quoteText']
