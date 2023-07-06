# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 13:17:05 2022

@author: xvideo
"""
import jieba

jieba.set_dictionary('dict/dict.txt.big.txt')
with open('dict/stop_words.txt', 'r', encoding='utf-8-sig') as f:
    stops = f.read().split('\n')
    
sentence = '大家好， 今天天氣不錯。'
breakwords = jieba.cut(sentence, cut_all=False)
words = []
for word in breakwords:
    if word not in stops:
        words.append(word)
        
print('|'.join(words))
