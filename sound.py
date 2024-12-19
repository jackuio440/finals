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

                        with sr.Microphone() as source:
                            listen_text = ''
                            r = sr.Recognizer()
                            audio = r.listen(source)
                            listen_text = r.recognize_google(
                                audio, language='zh-TW')


                except sr.UnknownValueError:
                    print("無法辨識")
                    sr_flag=True
                if "新聞" in listen_text :

                            return "1"
                elif "英文新聞" in listen_text :

                            return "2"
                elif "音樂" in listen_text :

                            return "3"
                elif "直播" in listen_text :

                            return '4'
                elif "嗨" in listen_text :

                            return '5'
                elif "結束"  in listen_text or "停止" in listen_text or "掰" in listen_text:

                            return 'end'
                else:

                            return '100'
