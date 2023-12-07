class Place:
    def __init__(self, name, coords, photos, place_type, data):
        self.name = name
        self.coords = coords
        self.photos = photos if photos else None
        self.place_type = place_type
        self.data = data
