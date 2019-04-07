from GoogleMyMaps import GoogleMyMaps
from pprint import pprint

mapID = "YOUR_MAP_ID"


if __name__ == "__main__":
    gmm = GoogleMyMaps()
    data = gmm.get(mapID)
    pprint(data)
