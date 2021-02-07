'''
Date: 2021-02-07 10:52:30
LastEditors: Jecosine
LastEditTime: 2021-02-07 18:09:51
'''


class Word:
    """
    @param: text   string  spelling
    @param: pos    dict    part of speech
    @param: tag    list    notebook list
    """

    def __init__(self, text):
        self.text = text
        self.pos = {}
        self.tags = []
        self.qm = []
        self.cs = []
        self.es = []
