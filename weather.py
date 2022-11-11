import grovepi
import datetime
import requests
import json
import dict
import math
from grove_rgb_lcd import *
from grovepi import *
import time


# URL設定
url = "https://api.open-meteo.com/v1/forecast?latitude=34.70&longitude=135.49&hourly=weathercode&timezone=Asia%2FTokyo"

# APIを叩いて取得した値を辞書として代入
res = requests.get(url)
res = res.text
res = json.loads(res)

grovepi.set_bus("RPI_1")

# 時刻を代入する変数（一旦絶対ありえない数字を入れる）
tmp = 25

# ローディング表示用配列
lo = ["⠙","⠸","⠴","⠦","⠇","⠋"]
try:   
    while True:
        
        # 現在時刻を取得
        dt_now = datetime.datetime.now()
        
        # 現在時間が変わるまでここで止まる
        while tmp == dt_now.hour:
            for li in range(len(lo)):
                print(f'\r{WMO_load[str(weathercode)]}{lo[li]}',end='')
                time.sleep(0.1)
        tmp = dt_now.hour  
        
        # 0時の場合API叩きなおし
        if dt_now.hour == 0:
            res = requests.get(url)
            res = res.text
            res = json.loads(res) 


        # WMOcodeJsonを読み込み
        WMO_open = open("WMO.json","r")
        WMO_load = json.load(WMO_open)

        # 現在時刻の一時間後のデータを取る
        weathercode = res['hourly']['weathercode'][dt_now.hour + 1]

        # ウェザーコードをカタカナに変換
        weather = WMO_load[str(weathercode)]

        # LCD表示用文字列
        temp = ""
        
        # カタカナを表示可能な形に変換
        for i in weather:
            temp += dict.dict[i]

        # LCD出力
        setText(f"{temp}\n{dt_now.hour}:00 update")
        setRGB(255,255,255)
        
except KeyboardInterrupt:
    print("")
    setText("")
    setRGB(0,0,0)