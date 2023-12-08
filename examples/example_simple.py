from GoogleMyMaps import GoogleMyMaps

map_link = 'YOUR_MAP_LINK'


if __name__ == '__main__':
    gmm = GoogleMyMaps()
    my_map = gmm.create_map(map_link)
    print(my_map)
