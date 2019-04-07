# import sys
import requests
from bs4 import BeautifulSoup
from pyjsparser import PyJsParser


class GoogleMyMaps():

    def __init__(self):
        self.parser = PyJsParser()

    def getFromMyMap(self, mapID):
        r = requests.get(
            "https://www.google.com/maps/d/edit?hl=ja&mid=" + mapID)
        return r

    def parseData(self, r):
        soup = BeautifulSoup(r.text, "html.parser")
        script = soup.find_all("script")[1].text
        js = self.parser.parse(script)
        pagedata = js["body"][1]["declarations"][0]["init"]["value"]

        data = pagedata.replace("true", "True")
        data = data.replace("false", "False")
        data = data.replace("null", "None")
        data = data.replace("\n", "")
        # exec("data = " + data)
        data = eval(data)
        return data[1]

    def parseLayerData(self, layerData):
        # layerName = layerData[2]

        places = layerData[4]
        # url = places[0][0]

        parsed = []
        for place in places:
            placeName = place[5][0][0]

            info = place[4]
            point = info[4]

            parsed.append({
                "placeName": placeName,
                "point": point,
            })

        return parsed

    def get(self, mapID, layers=[0]):
        r = self.getFromMyMap(mapID)
        if r.status_code != 200:
            print("status_code:", r.status_code)
            raise

        data = self.parseData(r)
        # mapID = data[1]
        # mapName = data[2]

        parsed = []
        for layer in layers:
            layerData = data[6][layer]
            parsed += self.parseLayerData(layerData)

        return parsed
