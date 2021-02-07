'''
Date: 2021-02-07 11:16:07
LastEditors: Jecosine
LastEditTime: 2021-02-07 12:19:36
'''
import json


class Source:
    def __init__(self):
        self.stype = ''
        self.title = ''
        self.description = ''
    """ 
    Convert html parser(dl) to object
    """

    def parser(self, html_parser):
        self.title = html_parser.find()
