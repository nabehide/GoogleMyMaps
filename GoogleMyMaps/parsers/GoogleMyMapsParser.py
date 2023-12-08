import requests
from bs4 import BeautifulSoup
from pyjsparser import PyJsParser


class GoogleMyMapsParser:
    def __init__(self):
        self.parser = PyJsParser()

    def get_map_data(self, map_id):
        raw_data = self._fetch_data(map_id)
        parsed_data = self._parse_data(raw_data)
        return parsed_data

    @staticmethod
    def _fetch_data(map_link: str):
        # TODO: map_link validation
        url = map_link
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"Failed to fetch map data. Status code: {response.status_code}")

        return response.text

    def _parse_data(self, raw_data):
        soup = BeautifulSoup(raw_data, "html.parser")
        script = soup.find_all("script")[1].text
        js = self.parser.parse(script)
        page_data = js["body"][1]["declarations"][0]["init"]["value"]

        data = page_data.replace("true", "True").replace("false", "False").replace("null", "None")
        data = data.replace("\n", "").replace('\xa0', ' ')

        return eval(data)[1]
