'''
Date: 2021-02-18 15:00:50
LastEditors: Jecosine
LastEditTime: 2021-02-19 09:45:12
'''
import sqlite3
import requests
import pickle
from faker import Faker
import random
import time
import json
import sys
from api import *
# get all word
word_list = []
data = []
error_list = []
fobj = Faker()
session = requests.session()
session.keep_alive = False
pattern_word = {
    'id': 'xxxx',
    'phonetic': '["us","en"]',
    'spell': 'abandon',
    'word_forms': '[{"wf":{"name":"xxx","value":"xxx"}},{"wf":{"name":"xx","value":"xxx"}}]',
    'pos': '{"noun": "noun definition", "verb": "verb definition"}',
    'cn_etym': 'html code of etym in cn',
    'en_etym': 'html code of etym'
}
header = {
    'Host': 'aidemo.youdao.com',
    'Content-Length': '',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'DNT': '1',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://ai.youdao.com',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'http://ai.youdao.com/'
}
# get spell and phonetic

url = 'https://aidemo.youdao.com/trans'
proxies = {
    'http': '127.0.0.1:1081',
    'https': '127.0.0.1:1081'
}


def parse_pos(raw_data):
    tl = []
    for i in raw_data:
        i = i.strip().split('. ')
        tl.append({"type": i[0], "definition": i[1]})
    return json.dumps(tl)


def fetch_data(word):
    global header, error_list, session
    word_data = []
    # header['User-Agent'] = fobj.user_agent()
    params = {
        'q': (None, word.strip()),
        'from': (None,'en'),
        'to': (None,'zh-CHS')
    }
    header1 = {
        'Content-Length': str(20 + len(word))
    }
    header['Content-Length'] = str(20 + len(word))
    resp = session.post(url.format(word), files=params, headers=header1, proxies=proxies)
    text = ''
    # print(header)
    # print(resp.text)
    try:
        text = resp.text
        text = text.encode('utf-8').decode('utf-8')
        d = json.loads(resp.text)
    except Exception as e:
        print('Error parsing to json, word {} failed, type1'.format(word))
        error_list.append(word)

    if d.get('basic'):
        d = d["basic"]
        # pos
        word_data.append(parse_pos(d['explains']))
        # cn_etym

        # en_etym

        # phonetic
        word_data.append('["{}"]'.format('","'.join(
            [d.get('us-phonetic') or '', d.get('uk-phonetic') or ''])))
        # audio_source
        word_data.append('["{}"]'.format('","'.join(
            [d.get('us-speech') or '', d.get('uk-speech') or ''])))
        # word_forms
        word_data.append(json.dumps([i['wf'] for i in d.get('wfs') or []]))
        word_data.append(word)
        return word_data
    else:
        print('No basic node, word: {}'.format(word))
        error_list.append(word)
        print('failed:' + text)
        return False


def load_words():
    for i in word_list:
        time.sleep(random.random() * 3 + 1.5)
        try:
            temp = fetch_data(i)
        except Exception as e:
            print('Error fetching word: %s, error message: %s' % (i, e.message))
        if temp:
            data.append(temp)
        else:
            print('Error fetching word: %s' % i)


def db():
    # connect to database
    con = sqlite3.connect('../test.db')
    cursor = con.cursor()
    # cursor.execute(update_sql, tuple(data))
    # con.commit()
    # con.close()
    return con, cursor
    # test code

    # for i in range(100):
    #     time.sleep(0.4)
    #     if i:
    #         print(len(str(i-1)) * '\b', end='')
    #     sys.stdout.flush()
    #     print(i, end='')


def submit_data(cursor, data):
    global error_list
    # update_sql = 'update word set pos=?, phonetic=?, audio_sources=?, word_forms=?, updated=1 where spell=?'
    update_sql = 'update word set raw=?, updated=1 where spell=?'
    try:
        cursor.executemany(update_sql, data)
    except Exception as e:
        print(e)
        print('[Error inserting database] ' + data[-1])
        error_list.append(data[-1])

def get_data(word):
    global header, error_list, session
    params = {
        'q': (None, word.strip()),
        'from': (None,'en'),
        'to': (None,'zh-CHS')
    }
    header1 = {
        'Content-Length': str(20 + len(word))
    }
    header['Content-Length'] = str(20 + len(word))
    resp = session.post(url.format(word), files=params, headers=header1, proxies=proxies)
    text = ''
    # print(header)
    # print(resp.text)
    try:
        text = resp.text
        text = text.encode('utf-8').decode('utf-8')
        d = json.loads(resp.text)
    except Exception as e:
        print('Error parsing to json, word {} failed, type1'.format(word))
        error_list.append(word)

    if d.get('basic'):
        return (json.dumps(d.get('basic')), word)
    else:
        print('No basic node, word: {}'.format(word))
        print('failed:' + text)
        error_list.append(word)
        return False


def mainprocess():
    global error_list, word_list
    data_patch = []
    con, cursor = db()
    # get word list
    word_list = cursor.execute(
        'select spell from word where updated=0').fetchall()
    word_list = [i[0] for i in word_list]
    pattern = 'Fetching No.{}'
    pre = ''
    for i in range(len(word_list)):
        if len(error_list) > 10:
            return
        if (i >= 50) and (i % 50 == 0):
            submit_data(cursor, data_patch)
            con.commit()
            data_patch.clear()
            print('...saving ...')
            print('[Error List]: {}(total)'.format(
                len(error_list)) + str(error_list[:20]))
            print()
        temp = None
        time.sleep(random.random())
        print('\b' * len(pre), end='')
        pre = pattern.format(i + 1, word_list[i], len(error_list))
        print(pre, end='')
        try:
            temp = fetch(word_list[i])
            temp = (temp.decode('utf-8'), word_list[i])
        except Exception as e:
            print(e)
            print('[Error getting data] ' + word_list[i])
            error_list.append(word_list[i])
        if temp:
            data_patch.append(temp)

    submit_data(cursor, data_patch)
    con.commit()
    con.close()
    with open('error_list.pic', 'wb') as f:
        pickle.dump(error_list, f)

# db(data)

if __name__ == '__main__':
    mainprocess()
    
