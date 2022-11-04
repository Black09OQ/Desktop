import datetime
# import requests
import json

""" url = "https://api.open-meteo.com/v1/forecast?latitude=34.70&longitude=135.49&hourly=weathercode&timezone=Asia%2FTokyo"

res = requests.get(url)
res = res.text
res = json.loads(res) """


# 現在時刻を取得
dt_now = datetime.datetime.now()

# 取得した天気jsonファイルを開く 
weather_open = open("text.json","r")
# jsonとして読み込み
weather_load = json.load(weather_open)
print(type(weather_load))

# WMOcodeJsonを読み込み
WMO_open = open("WMO.json","r")
WMO_load = json.load(WMO_open)


weathercode = weather_load['hourly']['weathercode'][dt_now.hour + 1]

weather = WMO_load[weathercode]

print(weather)