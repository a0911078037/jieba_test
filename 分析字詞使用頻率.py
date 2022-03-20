# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 13:40:56 2022

@author: xvideo
"""

from wordcloud import WordCloud
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import jieba
from collections import Counter

text = open('data/news1.txt', 'r', encoding='utf-8').read()

jieba.set_dictionary('dict/dict.txt.big.txt')
with open('dict/stopWord_cloud.txt', 'r', encoding='utf-8-sig') as f:
    stops = f.read().split('\n')
    
terms = []
for t in jieba.cut(text, cut_all=False):
    if t not in stops:
        terms.append(t)
        
diction = Counter(terms)

font = '_data/msyh.ttc'
mask = np.array(Image.open('_data/heart.png'))
wordcloud = WordCloud(font_path=font, mask=mask)
wordcloud.generate_from_frequencies(frequencies=diction)

plt.figure(figsize=(6,6))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()