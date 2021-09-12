# import requests
# import time
# import datetime
# from pprint import pprint

# url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-D0047-091?Authorization=CWB-97AF1200-D64F-4BD7-BFBA-C8E9892538FC&downloadType=WEB&format=JSON'

# res = requests.get(url)
# data_we = res.json()
# description = data_we['cwbopendata']['dataset']['locations']['location'][19]['weatherElement'][14]['time'][0]['elementValue']['value'] # 氣象描
# location = data_we['cwbopendata']['dataset']['locations']['location']


# dic = {}
# for i in range(len(location)):
#     dic[location[i]['locationName']] = i

# print(dic)


from random import randint
import math
from PIL import Image, ImageDraw


RGB = [hex(randint(0,255))[2:] for i in range(3)]
RGB = ["0" + i if len(i) == 1 else i for i in RGB] 
color = "#"
for i in RGB:
    color += i
print(color)


w, h = 200, 200
shape = [(w, h), (0, 0)]

img = Image.new("RGB", (w, h))

draw = ImageDraw.Draw(img)  
draw.rectangle(shape, fill = color)
img = img.save("color.jpg")