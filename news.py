import time
from gtts import gTTS
from pygame import mixer 
import tempfile
import speech_recognition as sr
from googletrans import Translator
import pygame

def talk(sentence,lang):
    with tempfile.NamedTemporaryFile(delete=True) as f:
        tts = gTTS(text=sentence,lang = lang)
        tts.save('{}.mp3'.format(f.name))
        mixer.music.load('{}.mp3'.format(f.name))
        mixer.music.set_endevent(pygame.USEREVENT)
        mixer.music.play(loops=0)
        
def google_translator(texts,target_lang):
    translator = Translator()
    return translator.trans(texts,dest=target_lang).text

mixer.init()
pygame.display.init()
news=[]
with open ('news.txt','r',encoding='utf-8') as f:
    for line in f:
        news.append(line)

n=0
report=news[n]
print(report)
sr_flag=True
while True:
    try:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                sr_flag=True
    except:
        pass
    if sr_flag==True:
        try :
            with sr.Microphone() as source:
                print ("說些話吧:")
                r=sr.Recognizer()
                r.energy_threshold = 4000
                audio = r.listen(source)
                listen_text= r.recognize_google(audio, language="zh-TW")
                print(listen_text)
                if "報" in listen_text :
                    print (report)
                    talk(report,'zh-tw')
                    sr_flag=False
                elif "翻譯" in listen_text or "英文" in listen_text:
                    res_text = google_translator(report,target_lang='en')
                    print(res_text)
                    talk(res_text,'en')
                    sr_flag=False
                elif "下一篇" in listen_text or "下" in listen_text:
                    n+=1
                    if n==len(news):
                        n=0
                    report = news[n]
                    print(report)
                elif "上一篇" in listen_text or "上" in listen_text:
                    n-=1
                    if n<0:
                        n=len(news)-1
                    report = news[n]
                    print(report)
                elif "結束"  in listen_text or "停止" in listen_text or "掰" in listen_text:
                    break
                else:
                    print("我不了解什麼是:" + listen_text)
                    talk("請再說一次!",'zh-tw')
                    sr_flag=False
        except sr.UnknownValueError:
            print("無法辨識")
            sr_flag=True
        except sr.RequestError as e:
            print("無法辨識{0}" .format(e))
            sr_flag=True