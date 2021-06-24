import json
import re
import hashlib

COUNTRIES_FILE = 'countries.json'
WIKI_URL = 'https://en.wikipedia.org/wiki/'
COUNTRIES_OUTPUT_FILE = 'countries.txt'


# Класс для первого задания по итераторам.
class GetCountriesPages:

    def __init__(self, countries_json_file, url):
        self.url = url
        self.countries_json_file = countries_json_file

    def __iter__(self):
        with open(self.countries_json_file, 'r', encoding='utf-8') as f:
            self.countries_json_content = json.load(f)
        return self

    def __next__(self):
        if not self.countries_json_content:
            raise StopIteration
        current_country = self.countries_json_content.pop(0)
        current_country_name = current_country['name']['common']
        current_country_url = WIKI_URL + re.sub(r'\s', '_', current_country_name)
        return current_country_name, current_country_url


# Функция для задания 2 по генераторам
def gethash(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        line = f.readline().strip()
        while line:
            yield hashlib.md5(line.encode()).hexdigest()
            line = f.readline().strip()


if __name__ == '__main__':

    # Задание 1
    with open(COUNTRIES_OUTPUT_FILE, 'w', encoding='utf-8') as f:
        for country, url in GetCountriesPages(COUNTRIES_FILE, WIKI_URL):
            f.write(f'{country} - {url}\n')

    # Задание 2
    for line_hash in gethash(COUNTRIES_OUTPUT_FILE):
        print(line_hash)
