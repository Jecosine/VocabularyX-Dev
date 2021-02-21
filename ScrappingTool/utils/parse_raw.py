'''
Date: 2021-02-21 10:02:32
LastEditors: Jecosine
LastEditTime: 2021-02-21 10:37:55
'''
import sqlite3
import json

con = sqlite3.connect('./test.db')
cursor = con.cursor()

word_list = []
error_list = []

def parse_pos(raw_data):
    tl = []
    for i in raw_data:
        i = i.strip().split('. ')
        if len(i) == 1:
            tl.append({"type": None, "definition": i[0]})
        else:
            tl.append({"type": i[0], "definition": i[1]})
    return json.dumps(tl)


def parse_data(raw_data, word):
    json.loads(raw_data)
    word_data = []
    if raw_data.get('basic'):
        raw_data = raw_data['basic']
    # pos
    if not raw_data.get('explains'):
        print('word {} doesnt have explains node')
        return False
    word_data.append(parse_pos(raw_data['explains']))
    # cn_etym

    # en_etym

    # phonetic
    word_data.append('["{}"]'.format('","'.join(
        [raw_data.get('us-phonetic') or '', raw_data.get('uk-phonetic') or ''])))
    # audio_source
    word_data.append('["{}"]'.format('","'.join(
        [raw_data.get('us-speech') or '', raw_data.get('uk-speech') or ''])))
    # word_forms
    if not raw_data.get('wfs'):
        word_data.append('[]')
    else:
        word_data.append(json.dumps([i['wf'] for i in raw_data.get('wfs') or []]))
    word_data.append(word)
    return word_data

def submit_data(data_list):
    global cursor, con
    update_sql = 'update word set pos=?, phonetic=?, audio_sources=?, word_forms=?, parsed=1 where spell=?'
    cursor.executemany(update_sql, tuple(data_list))
    con.commit()


def get_wordlist():
    global word_list, error_list
    word_list = cursor.execute('select spell, raw from word where parsed=0').fetchall()
    # word_list = [i[0] for i in word_list]
    data_list = []
    # pattern = 'Processing No.{}...'
    pre = ''
    for i in range(len(word_list)):
        # print('\b' * len(pre), end='')
        # pre = pattern.format(i + 1)
        # print(pre, end='')
        if i >= 100 and i % 100 == 0:
            submit_data(data_list)
            print('..saving to database[{} saved]...current {}'.format(len(data_list), i + 1))
            data_list.clear()
        res = parse_data(word_list[i])
        if not res:
            error_list.append(word_list[i][1])
        else:
            data_list.append(tuple(res))
    if len(data_list):
        submit_data(data_list)
        print('..saving to database[{} saved]...current {}'.format(len(data_list), i + 1))
    con.commit()
    con.close()