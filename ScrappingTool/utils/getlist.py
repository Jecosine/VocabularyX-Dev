'''
Date: 2021-02-07 12:14:50
LastEditors: Jecosine
LastEditTime: 2021-02-07 13:41:04
'''
import requests
import pickle
import logging
import time
import random 
from bs4 import BeautifulSoup as bs

words = []
url = 'https://www.quword.com/tags/{}/{}'
available_notebook = ['GRE', 'kaoyan', 'IELTS', 'TOEFL']
proxies = {
  'http': '127.0.0.1:1081',
  'https': '127.0.0.1:1081'
}
logger = logging.getLogger()
logger.setLevel(0)
def get_lib(libname):
    global words
    words = []
    res = requests.get(url.format(libname, None))
    html = res.text
    bsobj = bs(html, 'html.parser')
    pagecount = len(list(bsobj.find('div', {'class': 'yd-tags'}).findAll('a')))
    print('\nFetching Library {}...'.format(libname))
    print('  Total page count: {}'.format(pagecount))
    for i in range(pagecount):
        get_words(libname, i)
        time.sleep(random.random() * 3)
        if i and (i % 50) == 0:
            save_words(libname)
    save_words(libname)
    print("Done adding {} words".format(len(words)))
    
def save_words(libname):
    global words
    with open('{}.pic'.format(libname), 'wb') as f:
        pickle.dump(words, f)
    print("...Saving words...")

def get_words(libname, page):
    global words
    res = requests.get(url.format(libname, None))
    html = res.text
    bsobj = bs(html, 'html.parser')
    wordsobj = list(bsobj.find('div', {'class': 'panel-body'}).findAll('a'))
    print('    Fetching page {}...{} words'.format(page, len(wordsobj)))
    for a in wordsobj:
        words.append(a.get_text().strip())

for i in available_notebook:
    get_lib(i)
    s = input()
    