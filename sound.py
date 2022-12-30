import time
from gtts import gTTS
from pygame import mixer 
import tempfile
import speech_recognition as sr
from googletrans import Translator
import pygame

def sound():
        
            sr_flag=True
        
            try:
                for event in pygame.event.get():
                    if event.type == pygame.USEREVENT:
                        sr_flag=True
            except:
                pass
            if sr_flag==True:
                try :
                    try:
                        with sr.Microphone() as source:
                            r = sr.Recognizer()
                            audio = r.listen(source, timeout=3)
                            listen_text = r.recognize_google(audio, language='zh-TW')
                    except sr.WaitTimeoutError:
                        listen_text = ''

                        if "新聞" in listen_text :
                            return 1
                        elif "英文新聞" in listen_text :
                            return 2
                        
                        elif "結束"  in listen_text or "停止" in listen_text or "掰" in listen_text:
                            return end
                        else:
                            sr_flag=False
                            return 100
                except sr.UnknownValueError:
                    print("無法辨識")
                    sr_flag=True