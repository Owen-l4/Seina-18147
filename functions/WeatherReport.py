import discord
from discord.ext import commands

from BotCore import BotCore

import requests
import time
import datetime
from pprint import pprint

class WeatherReport(BotCore):
    @commands.command()
    async def weather(self,ctx,location):
        await ctx.message.delete()
        url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-D0047-091?Authorization=CWB-97AF1200-D64F-4BD7-BFBA-C8E9892538FC&downloadType=WEB&format=JSON'

        res = requests.get(url)

        location_to_code = {
            '連江': 0, 
            '金門': 1, 
            '宜蘭': 2, 
            '新竹': 3, 
            '苗栗': 4, 
            '彰化': 5, 
            '南投': 6, 
            '雲林': 7, 
            '嘉義': 8, 
            '屏東': 9, 
            '臺東': 10, '台東': 10,
            '花蓮': 11, 
            '澎湖': 12, 
            '基隆': 13, 
            '新竹': 14, 
            '嘉義': 15, 
            '臺北': 16, '台北': 16,
            '高雄': 17, 
            '新北': 18, 
            '臺中': 19, '台中': 19,
            '臺南': 20, '台南': 20,
            '桃園': 21
        }

        data_we = res.json()
        description = data_we['cwbopendata']['dataset']['locations']['location'][location_to_code[location]]['weatherElement'][14]['time'][0]['elementValue']['value'] # 氣象描述

        location = data_we['cwbopendata']['dataset']['locations']['location'][location_to_code[location]]['locationName']

        await ctx.send(location+"天氣:\n"+"```\n"+description+"```\n")

def setup(bot):
    bot.add_cog(WeatherReport(bot))