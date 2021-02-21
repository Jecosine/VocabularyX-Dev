'''
Date: 2021-02-20 22:05:36
LastEditors: Jecosine
LastEditTime: 2021-02-21 15:38:24
'''
from bs4 import BeautifulSoup as bs
import requests
import sqlite3
import time
import random
import re
import sys
requests.adapters.DEFAULT_RETRIES = 5
session = requests.session()
session.keep_alive = False

url = 'https://www.etymonline.com/word/{}?utm_source=extension_searchhint'

con = sqlite3.connect('./test.db')
cursor = con.cursor()

update_sql = 'update word set en_etym=? where spell=?'
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close',
    'Cache-Control': 'max-age=0',
    # 'Cookie': '_ga=GA1.2.3862693.1612697354; __gads=ID=86ff14de8e3d4bd3-221f66e9f3c50037:T=1612697388:RT=1612697388:S=ALNI_MYm0kKIZ7MXKnc7vAdlm3M1DvDHoA; _gid=GA1.2.636938744.1613830066; _gat_gtag_UA_26425972_1=1',
    'DNT': '1',
    'Host': 'www.etymonline.com',
    'If-None-Match': 'W/"7c44-ZDH96gGi02N0bMrNWxh06pAb3DM"',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'same-origin',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
}
proxies = {
    'http': '127.0.0.1:1081',
    'https': '127.0.0.1:1081'
}


def fetch_data(word):
    global session
    resp = session.get(url.format(word), headers=header, proxies=proxies)
    if resp and resp.status_code == 404:
        return '404'
    html = resp.text
    bsobj = bs(html, 'html.parser')
    res = bsobj.findAll('div', {'class': 'word--C9UPa'})
    if not res:
        return '404'
    else:
        # process
        res = str(res)
        if res and len(res) >= 2:
            res = res[1:-1]
        else:
            return ''
        pattern = re.compile('[\w-]+="[^"]+"')
        res = re.sub(pattern, '', res, 0)
        res.replace('<div></div>', '')
        res.replace('<div ></div>', '')
        res.replace('<div  ></div>', '')
        res.replace('<p ></p>', '')
        res.replace('<p></p>', '')
        return res


if __name__ == '__main__':
    word_list = cursor.execute(
        "select spell from word where en_etym is null").fetchall()
    word_list = [i[0] for i in word_list]
    data_patch = []
    str_pattern = 'current fetching No.{} ...'
    pre = ''
    for i in range(len(word_list)):
        print('\b' * len(pre), end='')
        pre = str_pattern.format(i + 1)
        print(pre, end='')
        sys.stdout.flush()
        if i >= 50 and i % 50 == 0:
            cursor.executemany(update_sql, tuple(data_patch))
            con.commit()
            print('...saving {} to db...current {}'.format(
                len(data_patch), i + 1))
            data_patch.clear()

        time.sleep(random.random() * 2 + 1)
        res = fetch_data(word_list[i])
        if res != '':
            if res == '404':
                print(" No etym for {}".format(word_list[i]))
                data_patch.append(('no', word_list[i]))
            data_patch.append((str(res), word_list[i]))
        else:
            print(' ERROR fetching {}'.format(word_list[i]))
    cursor.executemany(update_sql, tuple(data_patch))
    con.commit()
    con.close()
    session.close()
