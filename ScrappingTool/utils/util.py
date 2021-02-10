'''
Date: 2021-02-08 17:01:02
LastEditors: Jecosine
LastEditTime: 2021-02-09 11:27:12
'''
import uuid
import random
import pickle

word_dict = []
available_notebook = ['GRE', 'kaoyan', 'IELTS', 'TOEFL']
notebook_id = ['87868101a6', '78d70f31c8', 'a341126eae', '335da764db']
words = []

def get_uuid(n):
    s = ''
    while n > 0:
        s += str(uuid.uuid4()).replace('-', '')[:min(n, 32)]        
        n -= 32
    return s
    

def load_words():
    global word_dict
    word_dict = []
    l = [[] for i in range(4)]

    for i in range(4):
        with open('{}.pic'.format(available_notebook[i]), 'rb') as f:
            l[i] += list(pickle.load(f))
            print(len(l[i]))
    gre, kaoyan, ielts, toefl = l
    union = set()
    union = union.union(kaoyan)
    union = union.union(toefl)
    union = union.union(ielts)
    union = union.union(gre)
    with open('union.pic', 'wb') as f:
        pickle.dump(union, f)
    # print (union)
    maxlen = -1
    totallen = 0
    for i in l:
        for w in i:
            maxlen = max(maxlen, len(w))
            totallen += len(w)
    print(len(union))
    print(maxlen)
    print(totallen)
    return l, union


