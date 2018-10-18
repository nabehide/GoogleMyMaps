from GoogleMyMaps import GoogleMyMaps
from pprint import pprint
from private import mapID


if __name__ == "__main__":
    gmm = GoogleMyMaps()
    data = gmm.get(mapID)
    pprint(data)
