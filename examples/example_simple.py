from GoogleMyMaps import GoogleMyMaps

map_link = "YOUR MAP LINK"


if __name__ == "__main__":
    gmm = GoogleMyMaps()
    my_map = gmm.create_map(map_link, [1])
    print(my_map.name, end='\n\n')

    for layer in my_map.layers:
        print(f"Layer: {layer.name}")
        for place in layer.places:
            print(f"  Place: {place.name}")
