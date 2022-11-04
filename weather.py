import grovepi
import datetime
import requests
import json
import dict
import math
from grove_rgb_lcd import *
from grovepi import *


url = "https://api.open-meteo.com/v1/forecast?latitude=34.70&longitude=135.49&hourly=weathercode&timezone=Asia%2FTokyo"

res = requests.get(url)
res = res.text
res = json.loads(res)

grovepi.set_bus("RPI_1")


# 現在時刻を取得
dt_now = datetime.datetime.now()



# WMOcodeJsonを読み込み
WMO_open = open("WMO.json","r")
WMO_load = json.load(WMO_open)


weathercode = res['hourly']['weathercode'][dt_now.hour + 1]

weather = WMO_load[str(weathercode)]

temp = ""

for i in weather:
    temp += dict.dict[i]

print(temp)

setText(temp)