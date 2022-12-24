import time
from gtts import gTTS
from pygame import mixer 
import tempfile
import speech_recognition as sr
from googletrans import Translator
import pygame

def sound():
        while True:
            sr_flag=True
        
            try:
                for event in pygame.event.get():
                    if event.type == pygame.USEREVENT:
                        sr_flag=True
            except:
                pass
            if sr_flag==True:
                try :
                    with sr.Microphone() as source:
                        r=sr.Recognizer()
                        r.energy_threshold = 4000
                        audio = r.listen(source)
                        listen_text= r.recognize_google(audio, language="zh-TW")
                        if "新聞" in listen_text :
                            print (report)
                            talk(report,'zh-tw')
                            sr_flag=False
                        
                        elif "結束"  in listen_text or "停止" in listen_text or "掰" in listen_text:
                            os._exit()
                        else:
                            print("我不了解什麼是:" + listen_text)
                            talk("請再說一次!",'zh-tw')
                            sr_flag=False
                except sr.UnknownValueError:
                    print("無法辨識")
                    sr_flag=True