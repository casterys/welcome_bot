import aiogram
import logging
import config
import hashlib
#import requests
#import re
#from bs4 import BeautifulSoup
from config import *
from aiogram import Bot, types, Dispatcher, executor
from handlerw import *
from filter import IsAdminFilter
from youtube_search import YoutubeSearch
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle

def searcher(text):
    res = YoutubeSearch(text, max_results=10).to_dict()
    return res

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.filters_factory.bind(IsAdminFilter)

if __name__=="__main__":
    from handlerw import *
    executor.start_polling(dp, skip_updates=True)