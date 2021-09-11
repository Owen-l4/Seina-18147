import requests
import time
import datetime
from pprint import pprint

url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-D0047-091?Authorization=CWB-97AF1200-D64F-4BD7-BFBA-C8E9892538FC&downloadType=WEB&format=JSON'

res = requests.get(url)
data_we = res.json()
description = data_we['cwbopendata']['dataset']['locations']['location'][19]['weatherElement'][14]['time'][0]['elementValue']['value'] # 氣象描
location = data_we['cwbopendata']['dataset']['locations']['location']


dic = {}
for i in range(len(location)):
    dic[location[i]['locationName']] = i

print(dic)