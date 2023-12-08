class Place:
    def __init__(self,
                 place_type: str,
                 name: str,
                 coords: list[float] or list[list[float]],
                 photos: list[str] or None,
                 data: dict or None):
        self.place_type = place_type
        self.name = name
        self.coords = coords
        self.photos = photos
        self.data = data

    def __str__(self):
        photos_str = ('      Photos:\n'
                      + ''.join([f"        {photo}\n" for photo in self.photos])) \
            if self.photos else ''
        data_str = ('      Data:\n'
                    + ''.join([f"        {data}: {self.data[data]}\n" for data in self.data])) \
            if self.data else ''

        return f'{self.place_type}: {self.name}\n' \
               f'      Coordinates: {self.coords}\n' \
               f'{photos_str}' \
               f'{data_str}'
