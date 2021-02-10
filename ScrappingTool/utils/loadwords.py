'''
Date: 2021-02-08 17:00:09
LastEditors: Jecosine
LastEditTime: 2021-02-09 11:27:43
'''
import sqlite3
from util import *
# from ..models import *

con = sqlite3.connect('test.db')

cursor = con.cursor()

l, union = load_words()
data = []
data_1 = []
data = [(get_uuid(10), x) for x in union]
for i in union:
    if i == 'abortion':
        print("???")
# data = cursor.execute('select id, spell from word').fetchall()
word_dict = { i[1]: i[0]  for i in data }
for i in range(4):
    for x in l[i]:
        data_1.append((word_dict[x], notebook_id[i]))
insert_word_sql = 'insert into word (id, spell) values (?, ?)'
insert_relation = 'insert into word_notebook (word_id, notebook_id) values (?, ?)'
data = tuple(data)
data_1 = tuple(data_1)

cursor.executemany(insert_word_sql, data)
cursor.executemany(insert_relation, data_1)
con.commit()
con.close()