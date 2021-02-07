'''
Date: 2021-02-07 10:40:16
LastEditors: Jecosine
LastEditTime: 2021-02-07 12:14:37
'''
import os
import sqlite3
from models import *
import json
from bs4 import BeautifulSoup as bs
import requests

url = 'https://www.quword.com/w/{}'

api = 'https://fanyi.youdao.com/openapi.do?type=data&doctype=jsonp&version=1.1&keyfrom=neteaseopen&key=1532272597&callback=?&q='

header = {
  'Host': 'www.quword.com',
  'Connection': 'keep-alive',
  'Cache-Control': 'max-age=0',
  'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'DNT': '1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-User': '?1',
  'Sec-Fetch-Dest': 'document',
  'Referer': 'https://www.quword.com/tags/GRE',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'en-US,en;q=0.9',
  'Cookie': 'UM_distinctid=176e8e0fd15154-014f77fed1989e-c791039-144000-176e8e0fd16563; Hm_lvt_b98d5a4c985b16117a3eb5bd26322264=1610224828,1612656986; CNZZDATA1278225540=1105745206-1610223608-https%253A%252F%252Fwww.baidu.com%252F%7C1612664111; m_lpvt_b98d5a4c985b16117a3eb5bd26322264=1612667939'
}


"""return @param word: class Word"""
def query_word(text):
    res = requests.get(url.format(text), headers = header)
    bsobj = bs(res.text, 'html.parser')
    word = Word(text)
    word.parse(bsobj)

    
