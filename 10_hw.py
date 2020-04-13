# Работа с файлом json
import json
from pprint import pprint

with open(r'files/newsafr.json', encoding='utf-8') as f:
  json_news = json.load(f)
  news_list = []
  for top_news in json_news['rss']['channel']['items']:
    top_news = top_news['description'].lower()
    for word in top_news.split():
      if len(word) > 6:
        news_list.append(word)

  top_words = {}
  for afr_news in news_list:
    top_list_words = {afr_news:news_list.count(afr_news)}
    top_words.update(top_list_words)

  list_words = list(top_words.items())
  list_words.sort(key=lambda afr_news:afr_news[1])
  list_words = list_words[-10:]
  print('топ 10 самых часто встречающихся в новостях слов длиннее 6 символов:\n')
  list_words.reverse()

  for afr_news in range(10):
    print(list_words[afr_news])

#Работа с файлом XML
import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse(f'files/newsafr.xml', parser)
root = tree.getroot()

news_text_list = []
xml_news = root.findall('channel/item')
for top_news in xml_news:
  top_news = top_news.find('description').text.lower()
  news_text_list += top_news.split()

news_list = []
for word in news_text_list:
  if len (word) > 6:
    news_list.append(word)

top_word = {}
for afr_news in news_list:
  top_list_words = {afr_news:news_list.count(afr_news)}
  top_word.update(top_list_words)

list_words = list(top_word.items())
list_words.sort(key=lambda afr_news:afr_news[1])
list_words = list_words[-10:]
print('топ 10 самых часто встречающихся в новостях слов длиннее 6 символов:\n')
list_words.reverse()

for afr_news in range(10):
  print(list_words[afr_news])