import discord
from discord.ext import commands

import json

import os


with open('setting.json','r',encoding='utf8') as file:
    setting = json.load(file)

bot = commands.Bot(command_prefix='&')


for file in os.listdir('./functions'):
    if file.endswith('.py'):
        bot.load_extension(f'functions.{file[:-3]}')

if __name__ == '__main__':  
    bot.run(setting["token"])