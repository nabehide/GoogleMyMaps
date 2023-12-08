class Place:
    def __init__(self, name, coords, photos, place_type, data):
        self.name = name
        self.place_type = place_type
        self.coords = coords
        self.photos = photos if photos else None
        self.data = data

    def __str__(self):
        data_str = '\n'.join([f"          {data}" for data in self.data]) if self.data else "          No data"
        return f'Place: {self.name}\n' \
               f'        Place type: {self.place_type}\n' \
               f'        Coordinates: {self.coords}\n' \
               f'        Photos: {self.photos}\n' \
               f'        Data:\n{data_str}\n'
