from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
from requests import Response
import time
from datetime import datetime
import random
from random import choice
import webbrowser

r = sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan anlayamadı")
        except sr.RequestError:
            print("Sistem çalışmıyor")
        return voice


def responso(voice):
    if "merhaba" in voice:
        Speek("sanada selam küçükk adamm")

    if "nasılsın" in voice:
        Speek("yeni bir buluş bulmuş kadar iyiyim")

    if "teşekkür ederim" in voice or "teşekkürler" in voice:
        Speek("Rica ederim ")

    if "espri yap" in voice:
        selection = ["Esprin yolda", "Hemen geliyor", "işte sana buz gibi bir espri",
                     "bu espriye bayılacaksın"]
        selection = random.choice(selection
                                  )
        humor = ["Baykuşlar vedalaşırken ne der BAY BAY BAYKUŞ",
                 "Yemeğin suyuna kim bandı KOLİ BANDI",
                 "Türkiye’nin en yeni şehri hangisidir NEVŞEHİR",
                 "bir adam kitap okurken neden ölmüş çünkü satır başına gelmiş"]
        humor = random.choice(humor)

        Speek(selection + humor)

    if "görüşürüz" in voice:
        Speek("elveda dostum")
        exit()

    if "hangi gün" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today = "pazar"
        elif today == "Tuesday":
            today = "salı"
        elif today == "Wednesday":
            today = "çarşamba"
        elif today == "Thursday":
            today = "perşembe"
        elif today == "Friday":
            today = "cuma"
        elif today == "Saturday":
            today = "cumartesi"
        elif today == "Sunday":
            today = "pazar"

        Speek(today)

    if "saat kaç" in voice:
        Selection = ["Saat", "Hemen bakıyorum dostum", "Zorlu bir görev ama başarabilirim"]
        clock = datetime.now().strftime("%H:%M")
        Selection = random.choice(Selection)
        Speek(Selection + clock)

    if "uygulama aç" in voice:
        Speek("hangi uygulamayı açmamı istersin kullanıcı")
        runApp = record()
        runApp = runApp.lower()
        if "resim" in runApp:
            print(runApp)
            os.startfile(r"C:\Users\Mustafa\Desktop\Yeni klasör")
            Speek("uygulama açılıyor")
        else:
            print(runApp)
            Speek("Uygulama bulunamadı ya da sistem anlamadı")

    if "google'da ara" in voice:
        Speek("Ne aramamı istersiniz")
        search = record()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        Speek("{} için Google'da bulduklarımı listeliyorum.".format(search))

    if "youtube'da ara" in voice:
        Speek("Ne aramamı istersin brom")
        search = record()
        url = "https://www.youtube.com/results?search_query=" + search
        webbrowser.get().open(url)
        Speek(search + " için Youtubedan bulduklarımı listeliyorum")

    if "not et" in voice:
        Speek("notun ismi ne olsun")
        textfile = record() + ".txt"
        print(textfile)
        Speek("notun içine ne yazayım")
        thetext = record()
        print(thetext)
        f = open(textfile, "w", encoding="utf-8")
        f.writelines(thetext)
        f.close()


def Speek(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

Speek("ben embia seninle konuşmak için programlandım")

print (
"""***Sorulabilecek sorular***\n1 - Merhaba\n2 - Nasılsın\n3 - Teşekkürler ve Teşekkür edereim\n4 - Espri yap
5 - Görüşürüz\n6 - Hangi gündeyiz\n7 - Saat kaç\n8 - Googlede ara\n9 - Youtubede ara\n10 - Not et"""
      )

while True:
    voice = record()
    if voice != "":
        voice = voice.lower()
        print(voice)
        responso(voice)
