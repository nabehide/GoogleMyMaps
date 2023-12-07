class Map:
    def __init__(self, link, name, layers):
        self.link = link
        self.name = name
        self.layers = layers

    def add_layer(self, layer):
        self.layers.append(layer)
