class Map:
    def __init__(self, link, name, layers):
        self.link = link
        self.name = name
        self.layers = layers

    def __str__(self):
        layers_str = '\n'.join([f"  {layer}" for layer in self.layers]) if self.layers else "No layers"
        return f'Map: {self.name}\n' \
               f'Link: {self.link}\n\n' \
               f'Layers:\n{layers_str}\n'
