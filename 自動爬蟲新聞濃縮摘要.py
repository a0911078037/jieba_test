import data.AutoSummary as ausu
import requests
from bs4 import BeautifulSoup as soup

stops = []
with open('dict/stopWord_cloud.txt', 'r' , encoding='utf-8') as f:
    for line in f.readlines():
        stops.append(line.strip())
        
urls = []
url = 'https://www.chinatimes.com/realtimenews/?chdtv' #中時新聞
html = requests.get(url)
sp = soup(html.text, 'html.parser')
data1 = sp.select('.article-list a')
for d in data1:
    news_url = 'https://www.chinatimes.com' + d.get('href')
    if (len(news_url)>58) and (news_url not in urls):
        urls.append(news_url)
        
i = 1
for url in urls:
    html = requests.get(url)
    sp = soup(html.text, 'html.parser')
    data1 = sp.select('.article-body p')
    print('處理第{}則新聞'.format(i))
    text = ''
    for d in data1:
        if d.text != '':
            text+=d.text
            
    sentences,indexs = ausu.split_sentence(text)  #按標點分割句子
    tfidf = ausu.get_tfidf_matrix(sentences,stops)  #移除停用詞並轉換為矩陣
    word_weight = ausu.get_sentence_with_words_weight(tfidf)  #計算句子關鍵詞權重
    posi_weight = ausu.get_sentence_with_position_weight(sentences)  #計算位置權重
    scores = ausu.get_similarity_weight(tfidf)  #計算相似度權重
    sort_weight = ausu.ranking_base_on_weigth(word_weight, posi_weight, scores, feature_weight = [1,1,1])
    summar = ausu.get_summarization(indexs,sort_weight,topK_ratio = 0.3)  #取得摘要
    print(summar)
    print('==========================================================')
    i += 1