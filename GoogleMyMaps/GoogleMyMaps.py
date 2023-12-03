import requests
from bs4 import BeautifulSoup
from pyjsparser import PyJsParser


class GoogleMyMaps:

    def __init__(self):
        self.parser = PyJsParser()

    @staticmethod
    def get_from_my_map(map_id):
        r = requests.get(
            "https://www.google.com/maps/d/edit?&mid=" + map_id)
        return r

    def parse_data(self, r):
        soup = BeautifulSoup(r.text, "html.parser")
        script = soup.find_all("script")[1].text
        js = self.parser.parse(script)
        page_data = js["body"][1]["declarations"][0]["init"]["value"]

        data = page_data.replace("true", "True")
        data = data.replace("false", "False")
        data = data.replace("null", "None")
        data = data.replace("\n", "")
        data = data.replace('\xa0', ' ')

        data = eval(data)
        return data[1]

    @staticmethod
    def get_place_type_and_cords(place):
        if place[1] is not None:
            return 'Point', place[1][0][0]
        elif place[2] is not None:
            return 'Line', [cord[0] for cord in place[2][0][0]]
        elif place[3] is not None:
            return 'Polygon', [cord[0] for cord in place[3][0][0][0][0]]

    @staticmethod
    def extract_place_data(place_info):
        place_data = {}
        if len(place_info) > 1 and place_info[1] is not None:
            place_data[place_info[1][0]] = place_info[1][1][place_info[1][2] - 1]
        if len(place_info) > 3 and place_info[3] is not None:
            for info in place_info[3]:
                place_data[info[0]] = info[1][info[2] - 1]
        return place_data if place_data else None

    def parse_layer_data(self, layer_data):
        # layerName = layerData[2] # TODO: Use

        places = layer_data[12][0][13][0]
        # places_icons = layerData[12][0][13][1] -> [0][0]

        parsed = []
        for place in places:
            place_type, place_cords = self.get_place_type_and_cords(place)

            place_info = place[5]
            place_name = place_info[0][1][0]

            place_photos = [photo[1] for photo in place_info[2]] \
                if len(place_info) > 2 and place_info[2] is not None else None

            place_data = self.extract_place_data(place_info)

            parsed.append({
                "Cords": place_cords,
                "Data": place_data,
                "Name": place_name,
                "Photos": place_photos,
                "Type": place_type,
            })

        return parsed

    def get(self, map_id, layers=[0]):
        r = self.get_from_my_map(map_id)
        if r.status_code != 200:
            print("status_code:", r.status_code)
            raise

        data = self.parse_data(r)

        # mapName = data[2] # TODO: Use

        parsed = []
        for layer in layers:
            layer_data = data[6][layer]
            parsed += self.parse_layer_data(layer_data)

        return parsed
