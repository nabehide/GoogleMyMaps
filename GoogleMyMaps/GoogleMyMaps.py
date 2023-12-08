from GoogleMyMaps.parsers import GoogleMyMapsParser
from .models import Map, Layer, Place


class GoogleMyMaps:
    def __init__(self):
        self.parser = GoogleMyMapsParser()

    def create_map(self, map_link, chosen_layers: list = None):
        data = self.parser.get_map_data(map_link)
        name = data[2] if len(data) > 2 else "Unnamed Map"
        chosen_layers = self._parse_layers(data[6], chosen_layers) if len(data) > 6 else []
        return Map(map_link, name, chosen_layers)

    def _parse_layers(self, layers_data, chosen_layers=None):
        layers = []
        for index, layer_data in enumerate(layers_data):
            if chosen_layers is None or index in chosen_layers:
                layer_name = layer_data[2] if len(layer_data) > 2 else f"Unnamed Layer {index + 1}"
                places = self._parse_places(layer_data[12][0][13][0]) if len(layer_data) > 12 else []
                layers.append(Layer(layer_name, places))
        return layers

    def _parse_places(self, places_data):
        places = []
        for place_data in places_data:
            place_type, coords = self._get_place_type_and_coords(place_data) if len(place_data) > 5 else (None, None)

            place_info = place_data[5] if len(place_data) > 5 else None
            name = place_info[0][1][0] if place_info is not None and len(place_info[0]) > 1 else "Unnamed Place"
            photos = [photo[1] for photo in place_info[2]] if len(place_info) > 2 and place_info[2] else None
            data = self._extract_place_data(place_info) if len(place_info) > 5 else None
            places.append(Place(name, coords, photos, place_type, data))
        return places

    @staticmethod
    def _get_place_type_and_coords(place):
        if place[1] is not None:
            return 'Point', place[1][0][0]
        elif place[2] is not None:
            return 'Line', [cord[0] for cord in place[2][0][0]]
        elif place[3] is not None:
            return 'Polygon', [cord[0] for cord in place[3][0][0][0][0]]

    @staticmethod
    def _extract_place_data(place_info):
        place_data = {}
        if len(place_info) > 1 and place_info[1] is not None:
            place_data[place_info[1][0]] = place_info[1][1][place_info[1][2] - 1]
        if len(place_info) > 3 and place_info[3] is not None:
            for info in place_info[3]:
                place_data[info[0]] = info[1][info[2] - 1]
        return place_data if place_data else None
