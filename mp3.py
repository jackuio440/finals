def playmp3(song):
    global status,sound
    sound = mixer.music.load(song)
    mixer.music.play(loops = 0)    
    status="正在播放 {}".format(song.strip("music/"))      
    
def playNewmp3(song):
    global status,sound
    mixer.music.stop()
    sound = mixer.music.load(song)
    mixer.music.play(loops = 0)     
    status="正在播放 {}".format(song.strip("music/"))

from pygame import mixer
import glob,os,finger
mixer.init()
def musicpl():
    source_dir = "music/"
    mp3files = glob.glob(source_dir + "*.mp3")
    index=0
    status=""
    sound = mixer.music.load(mp3files[index])

    while True:
        choice = finger.hand_check()
        playmp3(mp3files[index]) 
        if choice==1:
            index +=1
            if index==len(mp3files):
                index=0 
            playNewmp3(mp3files[index])      
        elif choice==2:
            mixer.music.pause()
            status="暫停播放"
        elif choice==3:
            mixer.music.unpause()
            status="繼續播放" 
        elif choice==5:
            break
    mixer.music.stop()