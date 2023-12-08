import re

import requests
from bs4 import BeautifulSoup
from pyjsparser import PyJsParser


class GoogleMyMapsParser:
    def __init__(self):
        self.parser = PyJsParser()

    def get_map_data(self, map_link: str):
        GoogleMyMapsParser._validate_map_link(map_link)
        raw_data = GoogleMyMapsParser._fetch_data(map_link)
        parsed_data = self._parse_data(raw_data)
        return parsed_data

    @staticmethod
    def _validate_map_link(map_link: str):
        map_link_pattern = re.compile(
            r'https://www\.google\.com/maps/d/u/.*'
        )

        if not map_link_pattern.match(map_link):
            raise ValueError('Invalid map link format.')

    @staticmethod
    def _fetch_data(map_link: str):
        response = requests.get(map_link)

        if response.status_code != 200:
            raise Exception(f'Failed to fetch map data. Status code: {response.status_code}')

        return response.text

    def _parse_data(self, raw_data: str):
        soup = BeautifulSoup(raw_data, 'html.parser')
        script = soup.find_all('script')[1].text
        js = self.parser.parse(script)
        page_data = js['body'][1]['declarations'][0]['init']['value']

        data = page_data.replace('true', 'True').replace('false', 'False').replace('null', 'None')
        data = data.replace('\n', '').replace('\xa0', ' ')

        return eval(data)[1]
