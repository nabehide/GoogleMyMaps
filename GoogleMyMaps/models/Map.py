from . import Layer


class Map:
    def __init__(self, link: str, name: str, layers: list[Layer]):
        self.link = link
        self.name = name
        self.layers = layers

    def __str__(self):
        layers_str = '\n'.join([f"  {layer}" for layer in self.layers]) if self.layers else "No layers"
        return f'Link: {self.link}\n' \
               f'Map: {self.name}\n' \
               f'{layers_str}\n'
