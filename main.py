import requests
import datetime
from urllib.request import urlretrieve
import json
import time

screenWidth = '1920'
screenHeight = '1080'
currentCulture = 'en-US'
currentRegion = 'us'

def return_img(address):
    data = json.loads(requests.get(address).content)
    item = json.loads(data['batchrsp']['items'][0]['item'])
    return item['ad']['image_fullscreen_001_landscape']['u']
    
for i in range(5):
    utc_datetime = str(datetime.datetime.utcnow()).replace(' ','T').split('.')[0] + 'Z'
    urlretrieve(return_img(f'https://arc.msn.com/v3/Delivery/Cache?pid=209567&fmt=json&rafb=0&ua=WindowsShellClient%2F0&disphorzres={screenWidth}&dispvertres={screenHeight}&lo=80217&pl={currentCulture}&lc={currentCulture}&ctry={currentRegion}&time={utc_datetime}'),f'spotlight{i}.jpg')
    time.sleep(1)