from bs4 import BeautifulSoup
import requests
import random
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import pyttsx3

def newsFind():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
    url = 'https://www.pttweb.cc/hot/news/today'
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')
    divs = soup.find_all('div', 'e7-right-top-container e7-no-outline-all-descendants')
    articles = []
    root = 'https://www.pttweb.cc'
    for div in divs:
        link = div.find('a')['href']
        articles.append(root + link + '.html')

    url2 = articles[random.randint(0, 20)]
    print(url2)
    r = requests.get(url2, headers=headers)
    r.encoding = 'utf-8'
    sp = BeautifulSoup(r.text, 'html.parser')
    divs2 = sp.find('div', 'e7-main-content')
    spans = divs2.find_all('span')

    with open('news.txt', 'w+') as f:
        for span in spans:
            print(span.text)
            f.write(str(span.text))

def newsRead():
    with open('news.txt', 'r') as f:
        data = f.read()
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    engine.say(data)
    engine.runAndWait()
    print(data)
    print('------------------')

def newsRead_en():
    with open('news.txt', 'r') as f:
        data = f.read()
    translator = Translator()
    translated = translator.translate(data, dest="en").text
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    engine.say(translated)
    engine.runAndWait()
