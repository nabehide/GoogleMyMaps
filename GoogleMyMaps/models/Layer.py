class Layer:
    def __init__(self, name, places):
        self.name = name
        self.places = places

    def __str__(self):
        places_str = '\n'.join([f"      {place}" for place in self.places]) if self.places else "No places"
        return f'Layer: {self.name}\n' \
               f'    Places:\n{places_str}\n'
