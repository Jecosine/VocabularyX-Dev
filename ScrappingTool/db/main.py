'''
Date: 2021-02-08 16:49:07
LastEditors: Jecosine
LastEditTime: 2021-02-08 16:58:28
'''
import sqlite3
import os

class DB:
    def __init__(self, filename):
        self.con = sqlite3.connect(filename)
        self.cursor = self.con.cursor()
    def query(self, sql, data):
        return self.cursor.execute(sql, data)

    def querymany(self, sql, data):
        return self.cursor.executemany(sql, data)