import sys
import tkinter as tk
import random
from PIL import Image, ImageTk
import pygame as pygame
import cv2
import datetime
import time
import threading
import tkinter.font as tkFont
from time import perf_counter#0125trycatch
import asyncio
pygame.init()
ima = time.time()
soundp = pygame.mixer.Sound("imgSS/pinchSS.wav")
soundp2 = pygame.mixer.Sound("imgSS/stupid5.wav")
soundp3 = pygame.mixer.Sound("imgSS/pinpon.wav")
sounde1 = pygame.mixer.Sound("imgSS/nippon103.wav")
sounde2 = pygame.mixer.Sound("imgSS/Folk_Chinese.wav")
sounde3 = pygame.mixer.Sound("imgSS/VietnamBoatSong.wav")
def play():
    sounda = pygame.mixer.Sound("imgSS/charin.wav")   
    sounda.play()
    
def play3():
    global soundp
    
    soundp.set_volume(0)
    soundp.play()
    
def play4():
    global soundp2
    
    soundp2.set_volume(100)
    soundp2.play()
    
def play5():
    global soundp3
    
    soundp3.set_volume(100)
    soundp3.play()
def onryo():
    global soundp
    soundp.set_volume(5)
def end1play():
    global sounde1
    sounde1.set_volume(5)
    sounde1.play()
    
def end2play():
    global sounde2
    sounde2.set_volume(5)
    sounde2.play()
    
def end3play():
    global sounde3
    sounde3.set_volume(5)
    sounde3.play()
def onryop2():
    global hayaku, play3, onryo
    pygame.mixer.music.load("imgSS/MusMus-CT-NAVAO-21.wav")#Loading File Into Mixer
    pygame.mixer.music.play()#Playing It In The Whole Device
    pygame.mixer.music.set_volume(0.0)
    pygame.mixer.music.stop()#Loading File Into Mixer
        
def play2():
    global hayaku, play3, onryo
    pygame.mixer.music.load("imgSS/MusMus-CT-NAVAO-21.wav") #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device
    if 0.10 <= hayaku <= 15.00:#0206
        pygame.mixer.music.stop() #Loading File Into Mixer 
        onryo()   
    
root = tk.Tk()
root.title("すばやくしはらいチャレンジゲーム")
root.minsize(1240, 700)#0216
root.option_add("*font", ["メイリオ", 24])
numF = 0
call = " "
num = random.randint(1,1000)
imgSS0 = tk.PhotoImage(file = 'imgSS/siharaidekiru.png', master = root)
mojiC = tk.Label(text = "                                            しはらいできる？                                             ", bg="#FAFAD2", image=imgSS0)#0216
mojiC.pack(anchor='n',expand=1)
mojiA = tk.Text(height=1, width=62, wrap="none")#02161223
mojiA.tag_configure("r", foreground="#000000")
mojiA.tag_configure("g", foreground="#FF0000")
mojiA.tag_configure("b", foreground="#000000")
mojiA.insert("end", "　　　　　　　　　　結果発表ボタンを", 'r')#02161223
mojiA.insert("end", "押して", 'g')
mojiA.insert("end", "次へ行こう!", 'b')
mojiA.configure(state="disabled") # 読取専用に
mojiB = tk.Text(height=1, width=62, wrap="none")#02161223
mojiB.tag_configure("r", foreground="#FF0000")
mojiB.tag_configure("g", foreground="#000000")
mojiB.tag_configure("b", foreground="#000000")
mojiB.insert("end", "          　　　　クリア!", 'r')#02161225　↓　↓　も
mojiB.insert("end", "チャレンジモードが", 'g')#hs
mojiB.insert("end", "できるようになってるよ!", 'b')#hs
mojiB.configure(state="disabled") # 読取専用に
mojiBn = tk.Label(height=1, width=62, text = "どれも2回押しでクリア！", bg="white")#02161223
mojiD = tk.Text(height=1, width=62, wrap="none")#02161223
mojiD.tag_configure("r", foreground="#000000")
mojiD.tag_configure("g", foreground="#000000")
mojiD.tag_configure("b", foreground="#000000")
mojiD.insert("end", "          　　　　　　　　　　　最初", 'r')#02161223
mojiD.insert("end", "から", 'g')
mojiD.insert("end", "やりなおし!", 'b')
mojiD.configure(state="disabled") # 読取専用に
mojiE = tk.Text(height=1, width=62, wrap="none")#02161223
mojiE.tag_configure("r", foreground="#000000")
mojiE.tag_configure("g", foreground="#000000")
mojiE.tag_configure("b", foreground="#000000")
mojiE.insert("end", "           　　　　　　　　　　　　クリア", 'r')#02161223
mojiE.insert("end", "は", 'g')
mojiE.insert("end", "ならず!", 'b')
mojiE.configure(state="disabled") # 読取専用に
mojiF = tk.Label(text = "")
mojiG1 = tk.Label(text = "ザクザクモード",width=12, height=2, foreground='#ff0000', background='lightslategray')
mojiG2 = tk.Label(text = "チャレンジモード",width=12, height=2, foreground='#ff0000', background='lightslategray')
mojiG3 = tk.Label(text = "ザクザクモード",width=12, height=2, foreground='#ff0000', background='lightslategray')
mojiG4 = tk.Label(text = "チャレンジモード",width=12, height=2, foreground='#ff0000', background='lightslategray')
mojiG5 = tk.Label(text = "ザクザクモード",width=12, height=2, foreground='#ff0000', background='lightslategray')
mojiG6 = tk.Label(text = "チャレンジモード",width=12, height=2, foreground='#ff0000', background='lightslategray')
mojiT = tk.Text(height=1, width=62, wrap="none")#02161223
mojiT2 = tk.Text(height=1, width=62, wrap="none")#02161223
mojiTg = tk.Text(height=1, width=62, wrap="none")#02161223
mojiTg.tag_configure("r", foreground="#000000")
mojiTg.tag_configure("g", foreground="#FF0000")
mojiTg.tag_configure("b", foreground="#000000")
mojiTg.insert("end", "トレーに", 'r')
mojiTg.insert("end", str('{:.1f}'.format(num)), 'g')
mojiTg.insert("end", "元分はらって！", 'b')
mojiTg.configure(state="disabled") # 読取専用に
mojiTd = tk.Text(height=1, width=62, wrap="none")#02161223
mojiTd.tag_configure("r", foreground="#000000")
mojiTd.tag_configure("g", foreground="#FF0000")
mojiTd.tag_configure("b", foreground="#000000")
mojiTd.insert("end", "トレーに", 'r')
mojiTd.insert("end", str(num), 'g')
mojiTd.insert("end", "ドンはらって！", 'b')
mojiTd.configure(state="disabled") # 読取専用に
mojiTn = tk.Text(height=1, width=62, wrap="none")#02161223
emojiT = tk.Text(height=1, width=62, wrap="none")#02161223
emojiT.tag_configure("r", foreground="#000000")
emojiT.tag_configure("g", foreground="#FF0000")
emojiT.tag_configure("b", foreground="#000000")
emojiT.insert("end", "2つの商品の", 'r')#hs　1225
emojiT.insert("end", "合計額を", 'g')#hs 1225
emojiT.insert("end", "ピッタリはらって!", 'b')#hs 1225
emojiT.configure(state="disabled")
emojiTn = tk.Text(height=1, width=62, wrap="none")#02161223
mojiN = tk.Label(height=1, width=5, text = "残り秒数", bg="green")
mojiCp = tk.Text(height=1, width=62, wrap="none")#02161222
mojiCp.tag_configure("r", foreground="#000000")
mojiCp.tag_configure("g", foreground="#000000")
mojiCp.tag_configure("b", foreground="#000000")
mojiCp.insert("end", "                                    すばやく", 'r')#02161222
mojiCp.insert("end", "しはらいチャレンジゲーム", 'g')#1225 ひらがなに
mojiCp.insert("end", "!", 'b')
mojiCp.configure(state="disabled") # 読取専用に
mojiZ = tk.Text(height=1, width=62, wrap="none")#02161226
mojiZ.tag_configure("r", foreground="#000000")
mojiZ.tag_configure("g", foreground="#000000")
mojiZ.tag_configure("b", foreground="#000000")
mojiZ.insert("end", "                  ゲーム大好きなあなたに", 'r')#02161226
mojiZ.insert("end", "ザクザクモード解放!", 'g')#02161226
mojiZ.insert("end", "チェックしてね!", 'b')
mojiZ.configure(state="disabled") # 読取専用に
testM = tk.Label(text = "                                しはらいできる？", bg="#FAFAD2")#0125追加
testK = tk.Label(text = "                                しはらいできる？", bg="#FAFAD2")#0125追加
testRM = tk.Label(text = "                               しはらいできる？", bg="#FAFAD2")#0125追加
testF = tk.Label(text = "                                しはらいできる？", bg="#FAFAD2")#0125追加
mojiR = tk.Text(height=1, width=62, wrap="none")#otamesi0125
canvas = tk.Canvas(root, width = 1240, height = 700)#0216
canvas.configure(bg="#FAFAD2")
hantei = 1
imgSS1 = tk.PhotoImage(file = 'imgSS/undou_deadlisft_woman.png', master = root)
imgSS2 = tk.PhotoImage(file = 'imgSS/money_5000.png', master = root)
imgSS3 = tk.PhotoImage(file = 'imgSS/money_500.png', master = root)
imgSS4 = tk.PhotoImage(file = 'imgSS/money_50.png', master = root)
imgSS5 = tk.PhotoImage(file = 'imgSS/money_5.png', master = root)
imgSS6 = tk.PhotoImage(file = 'imgSS/money_10000.png', master = root)
imgSS7 = tk.PhotoImage(file = 'imgSS/money_1000.png', master = root)
imgSS8 = tk.PhotoImage(file = 'imgSS/money_100.png', master = root)
imgSS9 = tk.PhotoImage(file = 'imgSS/money_10.png', master = root)
imgSS10 = tk.PhotoImage(file = 'imgSS/money_1.png', master = root)
imgSS13 = tk.PhotoImage(file = 'imgSS/training_coin.png', master = root)
imgSS11 = tk.PhotoImage(file = 'imgSS/kintore_machine.png', master = root)
imgSS12 = tk.PhotoImage(file = 'imgSS/undou_coinwoman.png', master = root)
imgSS14 = tk.PhotoImage(file = 'imgSS/travel_passport.png', master = root)
imgSS15 = tk.PhotoImage(file = 'imgSS/training.png', master = root)
imgSS17 = tk.PhotoImage(file = 'imgSS/won.png', master = root)
imgSS18 = tk.PhotoImage(file = 'imgSS/woncoin.png', master = root)
imgSS19 = tk.PhotoImage(file = 'imgSS/doncoin.png', master = root)
imgSS20 = tk.PhotoImage(file = 'imgSS/don.png', master = root)
imgSS21 = tk.PhotoImage(file = 'imgSS/gen.png', master = root)
imgSS22 = tk.PhotoImage(file = 'imgSS/gencoin.png', master = root)
imgSS31 = tk.PhotoImage(file = 'imgSS/gen1g.png', master = root)
imgSS28 = tk.PhotoImage(file = 'imgSS/pcgazou.png', master = root)
imgSS29 = tk.PhotoImage(file = 'imgSS/notegazou.png', master = root)
imgSS30 = tk.PhotoImage(file = 'imgSS/lupegazou.png', master = root)
imgSS32 = tk.PhotoImage(file = 'imgSS/haikeis1.png', master = root)
imgSS33 = tk.PhotoImage(file = 'imgSS/haikeib2.png', master = root)
imgSS34 = tk.PhotoImage(file = 'imgSS/haikeih1.png', master = root)
imgSS35 = tk.PhotoImage(file = 'imgSS/kaizoku_takara.png', master = root)
imgSS41 = tk.PhotoImage(file = 'imgSS/10000円札_ミニ.png', master = root)
imgSS42 = tk.PhotoImage(file = 'imgSS/5000円札_ミニ.png', master = root)
imgSS43 = tk.PhotoImage(file = 'imgSS/1000円札_ミニ.png', master = root)
imgSS44 = tk.PhotoImage(file = 'imgSS/500円硬貨_ミニ.png', master = root)
imgSS45 = tk.PhotoImage(file = 'imgSS/100円硬貨_ミニ.png', master = root)
imgSS46 = tk.PhotoImage(file = 'imgSS/50円硬貨_ミニ.png', master = root)
imgSS47 = tk.PhotoImage(file = 'imgSS/10円硬貨_ミニ.png', master = root)
imgSS48 = tk.PhotoImage(file = 'imgSS/5円硬貨_ミニ.png', master = root)
imgSS49 = tk.PhotoImage(file = 'imgSS/1円硬貨_ミニ.png', master = root)
imgSS50 = tk.PhotoImage(file = 'imgSS/たまねぎ_yen.png', master = root)
imgSS51 = tk.PhotoImage(file = 'imgSS/ジャガイモ_yen.png', master = root)
imgSS52 = tk.PhotoImage(file = 'imgSS/にんじん_yen.png', master = root)
imgSS53 = tk.PhotoImage(file = 'imgSS/ペットボトル_yen.png', master = root)
imgSS54 = tk.PhotoImage(file = 'imgSS/レモン_yen.png', master = root)
imgSS55 = tk.PhotoImage(file = 'imgSS/トマト_yen.png', master = root)
imgSS56 = tk.PhotoImage(file = 'imgSS/コーラ_yen.png', master = root)
imgSS57 = tk.PhotoImage(file = 'imgSS/チョコ_yen.png', master = root)
imgSS58 = tk.PhotoImage(file = 'imgSS/カップラーメン_yen.png', master = root)
imgSS59 = tk.PhotoImage(file = 'imgSS/トウモロコシ_yen.png', master = root)
imgSS60 = tk.PhotoImage(file = 'imgSS/ハンバーガー_yen.png', master = root)
imgSS61 = tk.PhotoImage(file = 'imgSS/牛乳_yen.png', master = root)
imgSS62 = tk.PhotoImage(file = 'imgSS/バナナ_yen.png', master = root)
imgSS63 = tk.PhotoImage(file = 'imgSS/タバコ_yen.png', master = root)
imgSS64 = tk.PhotoImage(file = 'imgSS/ビール_yen.png', master = root)
imgSS65 = tk.PhotoImage(file = 'imgSS/フライパン_yen.png', master = root)
imgSS66 = tk.PhotoImage(file = 'imgSS/傘_yen.png', master = root)
imgSS67 = tk.PhotoImage(file = 'imgSS/包丁_yen.png', master = root)
imgSS68 = tk.PhotoImage(file = 'imgSS/メロン_yen.png', master = root)
imgSS69 = tk.PhotoImage(file = 'imgSS/ドライヤー_yen.png', master = root)
imgSS70 = tk.PhotoImage(file = 'imgSS/nitobe1-14.png', master = root)
imgSS71 = tk.PhotoImage(file = 'imgSS/natumekyu1000.png', master = root)
imgSS72 = tk.PhotoImage(file = 'imgSS/money_10000_shibusawa.png', master = root)
imgSS73 = tk.PhotoImage(file = 'imgSS/money_2000.png', master = root)
imgSS74 = tk.PhotoImage(file = 'imgSS/money_1000_kitazato.png', master = root)
imgSS75 = tk.PhotoImage(file = 'imgSS/money_5000_tsuda.png', master = root)
imgSS76 = tk.PhotoImage(file = 'imgSS/eur50.png', master = root)
imgSS77 = tk.PhotoImage(file = 'imgSS/eur5.png', master = root)
imgSS78 = tk.PhotoImage(file = 'imgSS/eur100.png', master = root)
imgSS79 = tk.PhotoImage(file = 'imgSS/eur500.png', master = root)#実は500eurもう使われてないらしい
imgSS80 = tk.PhotoImage(file = 'imgSS/eur10.png', master = root)
imgSS81 = tk.PhotoImage(file = 'imgSS/1eurocent.png', master = root)
imgSS82 = tk.PhotoImage(file = 'imgSS/10eurocent.png', master = root)
imgSS83 = tk.PhotoImage(file = 'imgSS/5eurocent.png', master = root)
imgSS84 = tk.PhotoImage(file = 'imgSS/1eurocoin.png', master = root)
imgSS85 = tk.PhotoImage(file = 'imgSS/50eurocent.png', master = root)
imgSS86 = tk.PhotoImage(file = 'imgSS/money_coin_america_1_reverse.png', master = root)
imgSS87 = tk.PhotoImage(file = 'imgSS/money_coin_america_5_reverse.png', master = root)
imgSS88 = tk.PhotoImage(file = 'imgSS/money_coin_america_10_reverse.png', master = root)
imgSS89 = tk.PhotoImage(file = 'imgSS/money_coin_america_25_reverse.png', master = root)
imgSS90 = tk.PhotoImage(file = 'imgSS/money_dollar1.png', master = root)
imgSS91 = tk.PhotoImage(file = 'imgSS/money_dollar5.png', master = root)
imgSS92 = tk.PhotoImage(file = 'imgSS/money_dollar10.png', master = root)
imgSS93 = tk.PhotoImage(file = 'imgSS/money_dollar50.png', master = root)
imgSS94 = tk.PhotoImage(file = 'imgSS/money_100dollar_new.png', master = root)
imgSS96 = tk.PhotoImage(file = 'imgSS/cachecarton.png', master = root)
imgSS97 = tk.PhotoImage(file = 'imgSS/cachecarton_小.png', master = root)
imgSS98 = tk.PhotoImage(file = 'imgSS/bunbougu_kokuban.png', master = root)
imgSS99 = tk.PhotoImage(file = 'imgSS/morioka4489.png', master = root)
imgSS100 = tk.PhotoImage(file = 'imgSS/nise_2000.png', master = root)
imgSS101 = tk.PhotoImage(file = 'imgSS/鉛筆.png', master = root)
imgSS102 = tk.PhotoImage(file = 'imgSS/鉛筆.png', master = root)
imgSS103 = tk.PhotoImage(file = 'imgSS/鉛筆.png', master = root)
imgSS104 = tk.PhotoImage(file = 'imgSS/鉛筆.png', master = root)
imgSS105 = tk.PhotoImage(file = 'imgSS/鉛筆.png', master = root)
imgSS106 = tk.PhotoImage(file = 'imgSS/マル.png', master = root)
imgSS107 = tk.PhotoImage(file = 'imgSS/バツ.png', master = root)
imgSS108 = tk.PhotoImage(file = 'imgSS/ノーカン.png', master = root)
imgSS109 = tk.PhotoImage(file = 'imgSS/math_plus.png', master = root)
imgSS110 = tk.PhotoImage(file = 'imgSS/傘_プライス.png', master = root)
imgSS111 = tk.PhotoImage(file = 'imgSS/掃除機_プライス.png', master = root)
imgSS112 = tk.PhotoImage(file = 'imgSS/掃除機_yen2.png', master = root)
imgSS113 = tk.PhotoImage(file = 'imgSS/掃除機_gen2.png', master = root)
imgSS114 = tk.PhotoImage(file = 'imgSS/carton_多少大.png', master = root)
imgSS115 = tk.PhotoImage(file = 'imgSS/equal.png', master = root)
imgSS116 = tk.PhotoImage(file = 'imgSS/question.png', master = root)
imgSS117 = tk.PhotoImage(file = 'imgSS/傘_don.png', master = root)
imgSS118 = tk.PhotoImage(file = 'imgSS/教卓.png', master = root)
imgSS119 = tk.PhotoImage(file = 'imgSS/training_coin_santa.png', master = root)
imgSS120 = tk.PhotoImage(file = 'imgSS/travel_passport2.png', master = root)
imgSS121 = None
imgSS122 = None
imgSS123 = None
imgSS124 = None
imgSS125 = None
flag = 1
chohante = 0
chohante2 = 0
chohante3 = 0
mouhante = 0
sttime = 0
stptime = 0
redtime = 0
hayaku = 0
susumu = 0
k3once = 0
numM = 0
numM1 = 0
numM2 = 0
numM3 = 0
numM4 = 0
numM5 = 0
existA = 0
numH = 0
List_A1=[]
List_B1=[]
List_C1=[]
List_D1=[]
Knum = 0
zahyohn = 0
zahyohn2 = 0
zahyohn3 = 0
zahyohn4 = 0
zahyohn5 = 0
tagX = []
tigau = 0
hint = 0
mojiK = tk.Label()
gengo = 0
uketori1 = []
uketori2 = []
uketori3 = []
uketori4 = []
uketori5 = []
carton = []
xi = []
yi = []
gengo2 = 0
imgMA = imgSS50
imgMB = imgSS50
imgMC = imgSS50
imgMD = imgSS50
imgME = imgSS50
imgMF = imgSS50
imgMG = imgSS50
imgMH = imgSS50
imgMI = imgSS50
imgMJ = imgSS50
gengo2 = 0
nedan = []
imgBox = []
mon1A = 0
mon2A = 0
mon3A = 0
mon4A = 0
mon5A = 0
mon1B = 0
mon2B = 0
mon3B = 0
mon4B = 0
mon5B = 0
ret1 = ('a', 'b', 'c')
ret2 = ('d', 'e', 'f')
ret3 = ('g', 'h', 'i')
ret4 = ('j', 'k', 'l')
ret5 = ('m', 'n', 'o')
count = 0
zaq = 0#02161226
chkdel = 0#02161226
img2ID = []
img3ID = []
img4ID = []
img5ID = []
img6ID = []
img7ID = []
img8ID = []
img9ID = []
img1ID = []
imgID = []
migID =[]#0206追加
def realK3():#0125eatarasikutuika muriyari zousetu
    
    global hantei, play4, play5, existA, k3once, Knum, numM1, numM2, numM3, numM4, numM5, zahyohn2, zahyohn3, zahyohn4, zahyohn5, zahyohn, List_A1, List_C1, Knum, num, gengo, gengo2#gengotuketa0128
    
    Knum = 0
    
    for id in canvas.find_all(): # 全オブジェクトを列挙
        tag = canvas.itemcget(id,'tags') # タグ名を取得
        if tag.startswith('img'):
            
            List_A1.append( {tag:canvas.coords(id)}) # .coordsで座標を取得
            List_C1.append( canvas.coords(id)[0])
            List_C1.append( canvas.coords(id)[1])
            if ((List_C1[0] >= 500) and (List_C1[1] >= 0)):#02161223
                if((List_C1[0] <= 825) and (List_C1[1] <= 200)):#02161223
                    xxx = List_A1[0]
                    yyy = xxx.keys()
                    zzz = list(yyy)
                    
                    if zzz[0] == 'img':
                        Knum += 10000
                    #02161226↓
                    elif zzz[0] == 'img1':#02161226
                        Knum += 1000000#02161226
                    elif zzz[0] == 'img2':
                        Knum += 5000
                    elif zzz[0] == 'img3':
                        Knum += 1000
                    elif zzz[0] == 'img4':
                        Knum += 500
                    elif zzz[0] == 'img5':
                        Knum += 100
                    elif zzz[0] == 'img6':
                        Knum += 50
                    elif zzz[0] == 'img7':
                        Knum += 10
                    elif zzz[0] == 'img8':
                        Knum += 5
                    elif zzz[0] == 'img9':
                        Knum += 1
                    else:
                        pass
            
            List_A1 = []
            List_C1 = []
        else:
            List_B1.append( {tag:canvas.coords(id)})
    
def zahyo():
    
    global hantei, play4, play5, existA, k3once, Knum, numM1, numM2, numM3, numM4, numM5, zahyohn2, zahyohn3, zahyohn4, zahyohn5, zahyohn, List_A1, List_C1, Knum, num, chohante, chohante2, chohante3#tuketasi0206
    Knum = 0
    zahyohn = 0
    zahyohn2 = 0
    zahyohn3 = 0
    zahyohn4 = 0
    zahyohn5 = 0
    for id in canvas.find_all(): # 全オブジェクトを列挙
        tag = canvas.itemcget(id,'tags') # タグ名を取得
        if tag.startswith('img'):
            
            
            List_A1.append( {tag:canvas.coords(id)}) # .coordsで座標を取得
            
            List_C1.append( canvas.coords(id)[0])
            List_C1.append( canvas.coords(id)[1])
            
            if ((List_C1[0] >= 500) and (List_C1[1] >= 0)):#判定検知 500, 0, 825, 200
                if((List_C1[0] <= 825) and (List_C1[1] <= 200)):#02161223
                
                    xxx = List_A1[0]
                    yyy = xxx.keys()
                    zzz = list(yyy)
                    
                    
                    if zzz[0] == 'img':
                        Knum += 10000
                    #02161226↓
                    elif zzz[0] == 'img1':#02161226
                        Knum += 1000000#02161226
                    elif zzz[0] == 'img2':
                        Knum += 5000
                    elif zzz[0] == 'img3':
                        Knum += 1000
                    elif zzz[0] == 'img4':
                        Knum += 500
                    elif zzz[0] == 'img5':
                        Knum += 100
                    elif zzz[0] == 'img6':
                        Knum += 50
                    elif zzz[0] == 'img7':
                        Knum += 10
                    elif zzz[0] == 'img8':
                        Knum += 5
                    elif zzz[0] == 'img9':
                        Knum += 1
                    else:
                        pass
                        
            
            List_A1 = []
            List_C1 = []
        else:
            List_B1.append( {tag:canvas.coords(id)})
 
    
    
    if Knum == num:
        zahyohn = 1
        play5()
        
        
    elif Knum == round((numM1), 1):#0125ゲンモードの判定で狂うので雑に小数点以下四捨五入してみる
        zahyohn2 = 1
        play5()
    elif Knum == round((numM2), 1):
        zahyohn3 = 1
        play5()
    elif Knum == round((numM3), 1):
        zahyohn4 = 1
        play5()
    elif Knum == round((numM4), 1):
        zahyohn5 = 1
        play5()
    elif Knum == round((numM5), 1):
        hantei += 2
        zahyohn6 = 1
        play5()#0128 ni kaijo
        
    elif Knum == 0:
        play4()
        zahyohn = 3
    else:
        
        play4()
        
        if k3once == 3:
            zahyohn2 = 2
        elif k3once == 6:
            zahyohn3 = 2
        elif k3once == 9:
            zahyohn4 = 2
        elif k3once == 12:
            zahyohn5 = 2
        elif k3once == 15:
            zahyohn5 = 2
        elif k3once == 18:
            zahyohn5 = 2
        
def challenge(imgM, imgN, numI):
    
    global gengo, gengo2, nedan, imgBox, mon1A, mon2A, mon3A, mon4A, mon5A, mon1B, mon2B, mon3B, mon4B, mon5B, imgSS50, imgSS51, imgSS52, imgSS53, imgSS54, imgSS55, imgSS56, imgSS57, imgSS58, imgSS59, imgSS560, imgSS61, imgSS62, imgSS63, imgSS64, imgSS65, imgSS66, imgSS67, imgSS68, imgSS69, imgSS70, imgSS71, imgSS72, imgSS73, imgSS74, imgSS75, imgSS76, imgSS77, imgSS578, imgSS79, imgSS80, imgSS81, imgSS82, imgSS83, imgSS84, imgSS85, imgSS86
    
    if gengo2 == 2:
        
        imgSS50 = tk.PhotoImage(file = 'imgSS/たまねぎ_gen.png', master = root)
        imgSS51 = tk.PhotoImage(file = 'imgSS/トウモロコシ_gen.png', master = root)
        imgSS52 = tk.PhotoImage(file = 'imgSS/ペットボトル_gen.png', master = root)
        imgSS53 = tk.PhotoImage(file = 'imgSS/ジャガイモ_gen.png', master = root)
        imgSS54 = tk.PhotoImage(file = 'imgSS/カップラーメン_gen.png', master = root)
        imgSS55 = tk.PhotoImage(file = 'imgSS/コーラ_gen.png', master = root)
        imgSS56 = tk.PhotoImage(file = 'imgSS/バナナ_gen.png', master = root)
        imgSS57 = tk.PhotoImage(file = 'imgSS/ビール_gen.png', master = root)
        imgSS58 = tk.PhotoImage(file = 'imgSS/トマト_gen.png', master = root)
        imgSS59 = tk.PhotoImage(file = 'imgSS/牛乳_gen.png', master = root)#02161226
        imgSS60 = tk.PhotoImage(file = 'imgSS/にんじん_gen.png', master = root)#02161226
        imgSS61 = tk.PhotoImage(file = 'imgSS/タバコ_gen.png', master = root)#02161226
        imgSS62 = tk.PhotoImage(file = 'imgSS/レモン_gen.png', master = root)
        imgSS63 = tk.PhotoImage(file = 'imgSS/パン_gen.png', master = root)
        imgSS64 = tk.PhotoImage(file = 'imgSS/チョコ_gen.png', master = root)
        imgSS65 = tk.PhotoImage(file = 'imgSS/ハンバーガー_gen.png', master = root)
        imgSS66 = tk.PhotoImage(file = 'imgSS/メロン_gen.png', master = root)
        imgSS67 = tk.PhotoImage(file = 'imgSS/傘_gen.png', master = root)
        imgSS68 = tk.PhotoImage(file = 'imgSS/包丁_gen.png', master = root)
        imgSS69 = tk.PhotoImage(file = 'imgSS/フライパン_gen.png', master = root)
        imgBox = [imgSS50, imgSS51, imgSS52, imgSS53, imgSS54, imgSS55, imgSS56, imgSS57, imgSS58, imgSS59, imgSS60, imgSS61, imgSS62, imgSS63, imgSS64, imgSS65, imgSS66, imgSS67, imgSS68, imgSS69]
    
    elif gengo2 == 3:
        
        imgSS50 = tk.PhotoImage(file = 'imgSS/にんじん_don.png', master = root)
        imgSS51 = tk.PhotoImage(file = 'imgSS/ペットボトル_don.png', master = root)
        imgSS52 = tk.PhotoImage(file = 'imgSS/トマト_don.png', master = root)
        imgSS53 = tk.PhotoImage(file = 'imgSS/コーラ_don.png', master = root)    
        imgSS54 = tk.PhotoImage(file = 'imgSS/メロン_don.png', master = root)#02161226
        imgSS55 = tk.PhotoImage(file = 'imgSS/バナナ_don.png', master = root)#
        imgSS56 = tk.PhotoImage(file = 'imgSS/カップラーメン_don.png', master = root)
        imgSS57 = tk.PhotoImage(file = 'imgSS/パン_don.png', master = root)#
        imgSS58 = tk.PhotoImage(file = 'imgSS/たまねぎ_don.png', master = root)#
        imgSS59 = tk.PhotoImage(file = 'imgSS/タバコ_don.png', master = root)
        imgSS60 = tk.PhotoImage(file = 'imgSS/ジャガイモ_don.png', master = root)#
        imgSS61 = tk.PhotoImage(file = 'imgSS/レモン_don.png', master = root)#
        imgSS62 = tk.PhotoImage(file = 'imgSS/ビール_don.png', master = root)#02161226
        imgSS63 = tk.PhotoImage(file = 'imgSS/トウモロコシ_don.png', master = root)
        imgSS64 = tk.PhotoImage(file = 'imgSS/フライパン_don.png', master = root)
        imgSS65 = tk.PhotoImage(file = 'imgSS/ハンバーガー_don.png', master = root)
        imgSS66 = tk.PhotoImage(file = 'imgSS/牛乳_don.png', master = root)
        imgSS67 = tk.PhotoImage(file = 'imgSS/包丁_don.png', master = root)
        imgSS68 = tk.PhotoImage(file = 'imgSS/チョコ_don.png', master = root)
        imgSS69 = tk.PhotoImage(file = 'imgSS/傘_don.png', master = root)
        imgBox = [imgSS50, imgSS51, imgSS52, imgSS53, imgSS54, imgSS55, imgSS56, imgSS57, imgSS58, imgSS59, imgSS60, imgSS61, imgSS62, imgSS63, imgSS64, imgSS65, imgSS66, imgSS67, imgSS68, imgSS69]
    
    else:
        
    
        imgSS50 = tk.PhotoImage(file = 'imgSS/たまねぎ_yen.png', master = root)
        imgSS51 = tk.PhotoImage(file = 'imgSS/ジャガイモ_yen.png', master = root)
        imgSS52 = tk.PhotoImage(file = 'imgSS/にんじん_yen.png', master = root)
        imgSS53 = tk.PhotoImage(file = 'imgSS/ペットボトル_yen.png', master = root)
        imgSS54 = tk.PhotoImage(file = 'imgSS/レモン_yen.png', master = root)
        imgSS55 = tk.PhotoImage(file = 'imgSS/トマト_yen.png', master = root)
        imgSS56 = tk.PhotoImage(file = 'imgSS/コーラ_yen.png', master = root)
        imgSS57 = tk.PhotoImage(file = 'imgSS/チョコ_yen.png', master = root)
        imgSS58 = tk.PhotoImage(file = 'imgSS/カップラーメン_yen.png', master = root)
        imgSS59 = tk.PhotoImage(file = 'imgSS/トウモロコシ_yen.png', master = root)
        imgSS60 = tk.PhotoImage(file = 'imgSS/パン_yen.png', master = root)
        imgSS61 = tk.PhotoImage(file = 'imgSS/ハンバーガー_yen.png', master = root)
        imgSS62 = tk.PhotoImage(file = 'imgSS/牛乳_yen.png', master = root)
        imgSS63 = tk.PhotoImage(file = 'imgSS/バナナ_yen.png', master = root)
        imgSS64 = tk.PhotoImage(file = 'imgSS/タバコ_yen.png', master = root)
        imgSS65 = tk.PhotoImage(file = 'imgSS/ビール_yen.png', master = root)
        imgSS66 = tk.PhotoImage(file = 'imgSS/フライパン_yen.png', master = root)
        imgSS67 = tk.PhotoImage(file = 'imgSS/傘_yen.png', master = root)
        imgSS68 = tk.PhotoImage(file = 'imgSS/包丁_yen.png', master = root)
        imgSS69 = tk.PhotoImage(file = 'imgSS/メロン_yen.png', master = root)
        imgBox = [imgSS50, imgSS51, imgSS52, imgSS53, imgSS54, imgSS55, imgSS56, imgSS57, imgSS58, imgSS59, imgSS60, imgSS61, imgSS62, imgSS63, imgSS64, imgSS65, imgSS66, imgSS67, imgSS68, imgSS69]
    
    
    mon1A = random.randint(0,20)
    mon2A = random.randint(0,20)
    mon3A = random.randint(0,20)
    mon4A = random.randint(0,20)
    mon5A = random.randint(0,20)
    
    mon1B = random.randint(0,20)
    mon2B = random.randint(0,20)
    mon3B = random.randint(0,20)
    mon4B = random.randint(0,20)
    mon5B = random.randint(0,20)
    
    
            
    imgM = imgBox[mon1A]
    imgN = imgBox[mon1B]
    
    if gengo2 == 2:
        nedan = [0.6, 1, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 7.5, 8 , 8.5, 12, 15, 20, 36, 49, 69, 70]#02161226
    
    elif gengo2 == 3:
        
        nedan = [28, 34, 77, 90, 100, 110, 119, 120, 129, 130, 134, 140, 150, 155, 200, 250, 260, 300, 390, 600]#02161226
        
    else:
        nedan = [48, 53, 72, 88, 107, 108, 120, 125, 138, 154, 156, 160, 178, 198, 450, 480, 1226, 1542, 2800, 3800]
    
    for u in range(20):
        if imgM == imgBox[u]:
            numI += nedan[u]
        else:
            numI += 0
        
        if imgN == imgBox[u]:
            numI += nedan[u]
        else:
            numI += 0
    
    
    return imgM, imgN, numI
            
    
def kekka_fortune():
    
    global mojiZ, chkdel, zaq, imgSS121, imgSS122, imgSS123, imgSS124, imgSS125, imgSS101, imgSS102, imgSS103, imgSS104, imgSS105, imgSS41, imgSS42, imgSS43, imgSS44, imgSS45, imgSS46, imgSS47, imgSS48, imgSS49, gengo, kaimono1, kaimono2, kaimono3, kaimono4, kaimono5, uketori1, uketori2, uketori3, uketori4, uketori5, mojiK, k3button, tigau, mojiTg, mojiTd, mojiT, mojiTn, hayaku, soundp, play2, sttime, mouhante, chohante, chohante2, chohante3, pressed_x, pressed_y, stptime, item_id, flag, hantei, mojiA, mojiB, mojiC, mojiD, mojiE, mojiF, kaimono
    
    tigau = 0
    sttime = 0
    stptime = 3
    soundp.stop()
    
    
    edbutton.place_forget()
    ed2button.place_forget()
    ed3button.place_forget()
    k3button.place_forget()
    k15button.place_forget()
    hnbutton.place_forget()
    mojiTg.pack_forget()
    mojiTd.pack_forget()
    emojiTn.pack_forget()
    tgbutton.place_forget()
    
    zm1button.place_forget()
    zm2button.place_forget()
    zm3button.place_forget()
    zm4button.place_forget()
    zm5button.place_forget()
    
    if hayaku >= 222.22 and hantei >= 3:#skai0125=240or230 realK3iretarabetunoBUGga...
        #02161226 skai0125=240or230
        chkdel = 1#02161226
    
    if hantei >= 3:
        mojiB.pack(anchor='n',expand=1)
        mojiK = tk.Label(text = "終了時タイム　残り"+str(format(hayaku, '.1f'))+"秒", width=62, height=1, foreground='#000000', background='#FAFAD2')#02161223
    
        mojiK.pack(anchor='n',expand=1)
        hayaku = 18.00
        play2()
        
        
        if mouhante == 1:
            chohante += 1
        if mouhante == 2:
            chohante2 += 1
        if mouhante == 3:
            chohante3 += 1
            
        if zaq == 1:
            flag = 2
            
        if flag == 2 and hantei >=3:
            if chohante >= 1000:
                edbutton.place(x=250, y=550)
                canvas.delete("all")
                stbutton.place_forget()
                stbutton.place(x=50, y=550)
                flag = 1
                hantei = 1
            else:                
                flag = 1
                hantei = 1            
            if chohante2 >= 1000:
                ed2button.place(x=250, y=650)
                canvas.delete("all")
                stbutton.place_forget()
                stbutton.place(x=50, y=550)
                flag = 1
                hantei = 1
            else:                
                flag = 1
                hantei = 1            
            if chohante3 >= 1000:
                ed3button.place(x=250, y=750)
                canvas.delete("all")
                stbutton.place_forget()
                stbutton.place(x=50, y=550)
                flag = 1
                hantei = 1
            else:                
                flag = 1
                hantei = 1
                      
        else:
            flag = 1
            hantei = 1
               
    elif hantei == 1:
        
        mojiD.pack(anchor='n',expand=1)
        mojiK = tk.Label(text = "終了時タイム　"+str(format(hayaku, '.1f'))+"秒", width=62, height=1, foreground='#000000', background='#FAFAD2')#02161223
        
        mojiK.pack(anchor='n',expand=1)
        hayaku = 18.00
        play2()
        flag = 1
        hantei = 1
                 
    else:
        
        mojiE.pack(anchor='n',expand=1)
        mojiK = tk.Label(text = "終了時タイム　"+str(format(hayaku, '.1f'))+"秒", width=62, height=1, foreground='#000000', background='#FAFAD2')#02161223
        
        mojiK.pack(anchor='n',expand=1)
        hayaku = 18.00
        play2()
        
        flag = 1
        hantei = 1
    
    canvas.delete("all")
    button.place_forget()
    mojiA.pack_forget()
    mojiF.pack_forget()
    stbutton.place(x = 550, y = 650)#02161226
    #変更250, 400, image=imgSS11 アマビエ　結果画面でのアマビエの位置を変更
    canvas.create_image(850, 550, image=imgSS11)#02161226
    
    canvas.place(x=100, y=100)
    canvas.pack()
    
    
    if gengo == 2:
        imgSS41 = tk.PhotoImage(file = 'imgSS/100元札_ミニ.png', master = root)
        imgSS42 = tk.PhotoImage(file = 'imgSS/50元札_ミニ.png', master = root)
        imgSS43 = tk.PhotoImage(file = 'imgSS/10元札_ミニ.png', master = root)
        imgSS44 = tk.PhotoImage(file = 'imgSS/5元札_ミニ.png', master = root)
        imgSS45 = tk.PhotoImage(file = 'imgSS/1元札_ミニ.png', master = root)
        imgSS46 = tk.PhotoImage(file = 'imgSS/5角札_ミニ.png', master = root)
        imgSS47 = tk.PhotoImage(file = 'imgSS/1角札_ミニ.png', master = root)
        imgSS48 = None
        imgSS49 = None
    elif gengo == 3:
        imgSS41 = None
        imgSS42 = tk.PhotoImage(file = 'imgSS/50万ドン_ミニ.png', master = root)
        imgSS43 = tk.PhotoImage(file = 'imgSS/10万ドン_ミニ.png', master = root)
        imgSS44 = tk.PhotoImage(file = 'imgSS/5万ドン_ミニ.png', master = root)
        imgSS45 = tk.PhotoImage(file = 'imgSS/1万ドン_ミニ.png', master = root)
        imgSS46 = tk.PhotoImage(file = 'imgSS/5千ドン_ミニ.png', master = root)
        imgSS47 = tk.PhotoImage(file = 'imgSS/千ドン_ミニ.png', master = root)
        imgSS48 = tk.PhotoImage(file = 'imgSS/5百ドン_ミニ.png', master = root)
        imgSS49 = tk.PhotoImage(file = 'imgSS/百ドン_ミニ.png', master = root)        
    else:
        imgSS41 = tk.PhotoImage(file = 'imgSS/10000円札_ミニ.png', master = root)
        imgSS42 = tk.PhotoImage(file = 'imgSS/5000円札_ミニ.png', master = root)
        imgSS43 = tk.PhotoImage(file = 'imgSS/1000円札_ミニ.png', master = root)
        imgSS44 = tk.PhotoImage(file = 'imgSS/500円硬貨_ミニ.png', master = root)
        imgSS45 = tk.PhotoImage(file = 'imgSS/100円硬貨_ミニ.png', master = root)
        imgSS46 = tk.PhotoImage(file = 'imgSS/50円硬貨_ミニ.png', master = root)
        imgSS47 = tk.PhotoImage(file = 'imgSS/10円硬貨_ミニ.png', master = root)
        imgSS48 = tk.PhotoImage(file = 'imgSS/5円硬貨_ミニ.png', master = root)
        imgSS49 = tk.PhotoImage(file = 'imgSS/1円硬貨_ミニ.png', master = root)
        
    kaimono1(uketori1)
    kaimono2(uketori2)
    kaimono3(uketori3)
    kaimono4(uketori4)
    kaimono5(uketori5)
    
    mojiZ.pack_forget()#02161226
    if chkdel == 1:#02161226
        mojiZ.pack(anchor='n',expand=1)
    
def kaimono1(uketori):
    
    global imgSS121, imgSS122, imgSS123, imgSS124, imgSS125, xi, yi, imgSS101, imgSS102, imgSS103, imgSS104, imgSS105
    
    
    canvas.create_image(120, 55, image=imgSS97)#02161223
    #変更50, 30, image=imgSS97結果画面でのトレーの位置を変更する。
    
    canvas.place(x=100, y=100)
    canvas.pack()
    
    canvas.create_image(370, 55, image=imgSS97)#02161223
    #変更150, 30, image=imgSS97
    
    canvas.place(x=100, y=100)
    canvas.pack()
    
    canvas.create_image(620, 55, image=imgSS97)#02161223
    #変更250, 30, image=imgSS97
    
    canvas.place(x=100, y=100)
    canvas.pack()
    
    canvas.create_image(870, 55, image=imgSS97)#02161223    
    #変更350, 30, image=imgSS97
    
    canvas.place(x=100, y=100)
    canvas.pack()
    
    canvas.create_image(1120, 55, image=imgSS97)#02161223
    #変更450, 30, image=imgSS97
    
    canvas.place(x=100, y=100)
    canvas.pack()
    
    canvas.create_image(120, 180, image=imgSS101)#02161223
    #変更50, 180, image=imgSS101 athintの商品画像位置変更
    
    canvas.place(x=100, y=100)
    canvas.pack()
    
    canvas.create_image(370, 180, image=imgSS102)#02161223
    #変更150, 180, image=imgSS102
    
    canvas.place(x=100, y=100)
    canvas.pack()
    
    canvas.create_image(620, 180, image=imgSS103)#02161223
    #変更250, 180, image=imgSS103
    
    canvas.place(x=100, y=100)
    canvas.pack()
    
    canvas.create_image(870, 180, image=imgSS104)#02161223
    #変更350, 180, image=imgSS104
    
    canvas.place(x=100, y=100)
    canvas.pack()
    
    canvas.create_image(1120, 180, image=imgSS105)#02161223
    #変更450, 180, image=imgSS105
    
    canvas.place(x=100, y=100)
    canvas.pack()
    
    canvas.create_image(120, 300, image=imgSS121)#0128解除
    #hs変更#02161223 s0122120, 280, image=imgSS121
    #変更
    
    canvas.place(x=100, y=100)
    canvas.pack()
    
    #変更
    canvas.create_image(370, 300, image=imgSS122)#02161223 s0122
    
    
    canvas.place(x=100, y=100)
    canvas.pack()
    
    #変更
    canvas.create_image(620, 300, image=imgSS123)#02161223 s0122
    
    
    canvas.place(x=100, y=100)
    canvas.pack()
    
    #変更
    canvas.create_image(870, 300, image=imgSS124)#02161223 s0122
    
    canvas.place(x=100, y=100)
    canvas.pack()
    
    #変更
    canvas.create_image(1120, 300, image=imgSS125)#02161223 s0122
    
    canvas.place(x=100, y=100)
    canvas.pack()
    
    
    
    xi = [70, 140, 190]#02161223
    #変更55, 65, 75 x座標のお金の位置を変更 トレーの真ん中へ 起点は紙幣の真ン中
    
    yi = [35, 45, 55, 65, 75, 85, 95]#02161223
    #35, 45, 55, 65, 75, 85, 95
    
    o = 0
    p = 0
    op = 0
    
    for o in range(len(xi)):
        for p in range(len(yi)):
                canvas.create_image(xi[o], yi[p], image=uketori[op])
                canvas.place(x=xi[o], y=yi[p])
                canvas.pack()
                op += 1
    
    
def kaimono2(uketori):    
    global xi, yi    
    
    xi = [320, 390, 440]#02161223
    #変更155, 165, 175 355, 365, 375
    
    yi = [35, 45, 55, 65, 75, 85, 95]#02161223
    #変更35, 45, 55, 65, 75, 85, 95
    
    o = 0
    p = 0
    op = 0    
    for o in range(len(xi)):
        for p in range(len(yi)):
                canvas.create_image(xi[o], yi[p], image=uketori[op])
                canvas.place(x=xi[o], y=yi[p])
                canvas.pack()
                op += 1
    
def kaimono3(uketori):    
    global xi, yi    
    
    xi = [570, 645, 690]#02161223
    #変更255, 265, 275
    
    yi = [35, 45, 55, 65, 75, 85, 95]#02161223 
    
    o = 0
    p = 0
    op = 0    
    for o in range(len(xi)):
        for p in range(len(yi)):
                canvas.create_image(xi[o], yi[p], image=uketori[op])
                canvas.place(x=xi[o], y=yi[p])
                canvas.pack()
                op += 1
                
def kaimono4(uketori):    
    global xi, yi    
    
    
    xi = [820, 890, 940]#02161223
    #変更355, 365, 375
    
    yi = [35, 45, 55, 65, 75, 85, 95]    
    
    o = 0
    p = 0
    op = 0    
    for o in range(len(xi)):
        for p in range(len(yi)):
                canvas.create_image(xi[o], yi[p], image=uketori[op])
                canvas.place(x=xi[o], y=yi[p])
                canvas.pack()
                op += 1
    
def kaimono5(uketori):    
    global xi, yi, uketori1, uketori2, uketori3, uketori4, uketori5   
    
    xi = [1040, 1100, 1160]#02161223
    #変更455, 465, 475
    
    yi = [35, 45, 55, 65, 75, 85, 95]    
    
    o = 0
    p = 0
    op = 0    
    for o in range(len(xi)):
        for p in range(len(yi)):
                canvas.create_image(xi[o], yi[p], image=uketori[op])
                canvas.place(x=xi[o], y=yi[p])
                canvas.pack()
                op += 1
    
def ning():
    
    global mojiZ, imgSS86, imgSS87, imgSS88, imgSS89, imgSS90, imgSS91, imgSS92, imgSS93, imgSS94, zaq, chk, bln, chk2, bln2, flag, mon1A, mon2A, mon3A, mon4A, mon5A, mon1B, mon2B, mon3B, mon4B, mon5B, count, ret, ret2, ret3, ret4, ret5, nedan, imgBox, imgSS121, imgSS122, imgSS123, imgSS124, imgSS125, gengo2, uketori1, uketori2, uketori3, uketori4, uketori5, imgSS41, imgSS42, imgSS43, imgSS44, imgSS45, imgSS46, imgSS47, imgSS48, imgSS49, k3once, gengo, imgSS2, imgSS3, imgSS4, imgSS5, imgSS6, imgSS7, imgSS8, imgSS9, imgSS10, mojiT, mojiT2, mojiTg, mojiTd, existA, k3once, sttime, stptime, mojiA, mojiB, mojiD, mojiE, mojiF, mojiG1, mojiG2, mojiG3, mojiG4, mojiG5, mojiG6, play, chohante, chohante2, chohante3
    
    
    play2()
    canvas.delete("all")
    sttime = 0
    stptime = 3
    
    k3once = 0
    existA = 0
    
    gengo = 0
    
    gengo2 = 0
    
    flag = 1
    
    uketori1 = []
    uketori2 = []
    uketori3 = []
    uketori4 = []
    uketori5 = []
    imgSS121 = None
    imgSS122 = None
    imgSS123 = None
    imgSS124 = None
    imgSS125 = None
    nedan = []
    imgBox = []
    mon1A = 0
    mon2A = 0
    mon3A = 0
    mon4A = 0
    mon5A = 0
    mon1B = 0
    mon2B = 0
    mon3B = 0
    mon4B = 0
    mon5B = 0
    ret = ('a', 'b', 'c')
    ret2 = ('d', 'e', 'f')
    ret3 = ('g', 'h', 'i')
    ret4 = ('j', 'k', 'l')
    ret5 = ('m', 'n', 'o')
    count = 0
    zaq = 0#02161226
    
    stbutton.place_forget()
    edbutton.place_forget()
    ed2button.place_forget()
    ed3button.place_forget()
    mojiB.pack_forget()
    mojiD.pack_forget()
    mojiE.pack_forget()
    mojiA.pack_forget()
    mojiC.pack_forget()
    mojiF.pack_forget()
    mojiG1.pack_forget()
    mojiG2.pack_forget()
    mojiG3.pack_forget()
    mojiG4.pack_forget()
    mojiG5.pack_forget()
    mojiG6.pack_forget()
    #canvas.create_rectangle(0, 0, 500, 600, fill = "white", tag = "back")
    mojiTg.pack_forget()
    mojiTd.pack_forget()
    mojiK.pack_forget()
    mojiT2.pack_forget()
    mojiT.pack_forget()
    
    mojiZ.pack_forget()#02161226
    
    button.place_forget()
    gm1button.place_forget()
    gm2button.place_forget()
    gm3button.place_forget()
    gm4button.place_forget()
    gm5button.place_forget()
    gm6button.place_forget()
    gm7button.place_forget()
    gm8button.place_forget()
    gm9button.place_forget()
    
    er1button.place_forget()
    er2button.place_forget()
    er3button.place_forget()
    
    gobutton.place_forget()
    edbutton.place_forget()
    stbutton.place_forget()
    k3button.place_forget()
    k15button.place_forget()
    rtbutton.place_forget()
    
    chk.place_forget()
    chk2.place_forget()#02161226
    
    
    imgSS2 = tk.PhotoImage(file = 'imgSS/money_5000.png', master = root)
    imgSS3 = tk.PhotoImage(file = 'imgSS/money_500.png', master = root)
    imgSS4 = tk.PhotoImage(file = 'imgSS/money_50.png', master = root)
    imgSS5 = tk.PhotoImage(file = 'imgSS/money_5.png', master = root)
    imgSS6 = tk.PhotoImage(file = 'imgSS/money_10000.png', master = root)
    imgSS7 = tk.PhotoImage(file = 'imgSS/money_1000.png', master = root)
    imgSS8 = tk.PhotoImage(file = 'imgSS/money_100.png', master = root)
    imgSS9 = tk.PhotoImage(file = 'imgSS/money_10.png', master = root)
    imgSS10 = tk.PhotoImage(file = 'imgSS/money_1.png', master = root)
    
    imgSS41 = tk.PhotoImage(file = 'imgSS/10000円札_ミニ.png', master = root)
    imgSS42 = tk.PhotoImage(file = 'imgSS/5000円札_ミニ.png', master = root)
    imgSS43 = tk.PhotoImage(file = 'imgSS/1000円札_ミニ.png', master = root)
    imgSS44 = tk.PhotoImage(file = 'imgSS/500円硬貨_ミニ.png', master = root)
    imgSS45 = tk.PhotoImage(file = 'imgSS/100円硬貨_ミニ.png', master = root)
    imgSS46 = tk.PhotoImage(file = 'imgSS/50円硬貨_ミニ.png', master = root)
    imgSS47 = tk.PhotoImage(file = 'imgSS/10円硬貨_ミニ.png', master = root)
    imgSS48 = tk.PhotoImage(file = 'imgSS/5円硬貨_ミニ.png', master = root)
    imgSS49 = tk.PhotoImage(file = 'imgSS/1円硬貨_ミニ.png', master = root)
    
                        
    imgSS94 = tk.PhotoImage(file = 'imgSS/money_100dollar_new.png', master = root)
    imgSS93 = tk.PhotoImage(file = 'imgSS/money_dollar50.png', master = root)
    imgSS92 = tk.PhotoImage(file = 'imgSS/money_dollar10.png', master = root)
    imgSS91 = tk.PhotoImage(file = 'imgSS/money_dollar5.png', master = root)
    imgSS90 = tk.PhotoImage(file = 'imgSS/money_dollar1.png', master = root)
    imgSS89 = tk.PhotoImage(file = 'imgSS/money_coin_america_25_reverse.png', master = root)
    imgSS88 = tk.PhotoImage(file = 'imgSS/money_coin_america_10_reverse.png', master = root)
    imgSS87 = tk.PhotoImage(file = 'imgSS/money_coin_america_5_reverse.png', master = root)
    imgSS86 = tk.PhotoImage(file = 'imgSS/money_coin_america_1_reverse.png', master = root)
    
    canvas.create_image(250, 300, tag = "open")
    #変更x = 150, y = 550
    gobutton.place(x = 500, y = 700)#02161226
    
    mojiC.pack(anchor='n',expand=1)
    mojiCp.pack(anchor='n',expand=1)
    
    
    canvas.create_image(600, 350, image=imgSS12)#0216
    #変更(280, 200, image=imgSS12) 旅行会社の絵
    
    canvas.place(x=100, y=100)
    canvas.pack()
    
    for us in range(3):
        ichiA = random.randint(100,1100)#0216
        ichiB = random.randint(500,670)#0216
        canvas.create_image(ichiA, ichiB, image=imgSS14, tags = "irasutoya")
        canvas.place(x=100, y=100)
        canvas.pack()          
    hairetsu = []
    ii = random.randint(0, 5)
    iii = random.randint(0, 5)
    iv = random.randint(0, 5)
    v = random.randint(0, 5)
    vi = random.randint(0, 5)
    vii = random.randint(0, 5)
    viii = random.randint(0, 5)
    ix = random.randint(0, 5)
    xi = random.randint(0, 5)
    xii = random.randint(0, 5)
    xiii = random.randint(0, 5)
    xiv = random.randint(0, 5)
    xv = random.randint(0, 5)
    
    hid = [ii, iii, iv, v, vi, vii, viii, ix, xi, xii, xiii, xiv, xv]
    
    for j in range(13):
        hairetsu.append(hid[j])
    for z in range(5):
        for i1 in range(hairetsu[0]):
            a1 = random.randint(100,1050)#0216
        #変更1,400)？
            b1 = random.randint(500,670)#0216
        #変更100,500
            canvas.create_image(a1, b1, image=imgSS2, tags = "img2")
            canvas.place(x=100, y=100)
            canvas.pack()  
        for i2 in range(hairetsu[1]):
            a2 = random.randint(100,1100)#0216
    #変更100,400?
            b2 = random.randint(500,670)#0216
    #変更100,500?
            canvas.create_image(a2, b2, image=imgSS3, tags = "img4")
            canvas.place(x=100, y=100)
            canvas.pack()
        for i3 in range(hairetsu[2]):
            a3 = random.randint(300,400)#0216
            b3 = random.randint(500,670)#0216
        #変更100,500?
            canvas.create_image(a3, b3, image=imgSS4, tags = "img6")
            canvas.place(x=100, y=100)
            canvas.pack()  
        for i4 in range(hairetsu[3]):
            a4 = random.randint(100,1100)#0216
    #変更1,400?
            b4 = random.randint(500,670)#0216
    #変更100,500?
            canvas.create_image(a4, b4, image=imgSS5, tags = "img8")
            canvas.place(x=100, y=100)
            canvas.pack()
        for i5 in range(hairetsu[4]):
            a5 = random.randint(100,1100)#0216
    #変更1,400?
            b5 = random.randint(500,670)#0216
        #変更100,500?
            canvas.create_image(a5, b5, image=imgSS6, tags = "img")
            canvas.place(x=100, y=100)
            canvas.pack()  
        for i6 in range(hairetsu[5]):
            a6 = random.randint(100,1100)#0216
    #変更1,400?
            b6 = random.randint(500,670)#0216
    #変更100,500?
            canvas.create_image(a6, b6, image=imgSS7, tags = "img3")
            canvas.place(x=100, y=100)
            canvas.pack()
        for i7 in range(hairetsu[6]):
            a7 = random.randint(100,1100)#0216
    #変更1,400?
            b7 = random.randint(500,670)#0216
        #変更100,500?
            canvas.create_image(a7, b7, image=imgSS8, tags = "img5")
            canvas.place(x=100, y=100)
            canvas.pack()  
        for i8 in range(hairetsu[7]):
            a8 = random.randint(100,1100)#0216
    #変更1,400?
            b8 = random.randint(500,670)#0216
        #変更1,400?
            canvas.create_image(a8, b8, image=imgSS9, tags = "img7")
            canvas.place(x=100, y=100)
            canvas.pack()
        for i9 in range(hairetsu[8]):
            a9 = random.randint(100,1100)#0216
    #変更1,400?
            b9 = random.randint(500,670)#0216
    #変更100,500?
            canvas.create_image(a9, b9, image=imgSS10, tags = "img9")
            canvas.place(x=100, y=100)
            canvas.pack()   
    
def erabing():
    
    global zaq, chk2, bln2, bln, chk, mojiT, mojiT2, mojiA, mojiT, numH, mojiTg, mojiTd, mojiA, mojiB, mojiD, mojiE, hantei
    
    canvas.delete("all")
    
    gobutton.place_forget()
    mojiB.pack_forget()
    mojiD.pack_forget()
    mojiE.pack_forget()
    mojiG1.pack_forget()
    mojiG2.pack_forget()
    mojiG3.pack_forget()
    mojiG4.pack_forget()
    mojiG5.pack_forget()
    mojiG6.pack_forget()
    mojiT.pack_forget()
    mojiA.pack_forget()
    chk.place_forget()
    chk2.place_forget()    
    mojiT.pack_forget()
    mojiT2.pack_forget()
    mojiCp.pack_forget()
    
    button.place_forget()
    gm1button.place_forget()
    gm2button.place_forget()
    gm3button.place_forget()
    gm4button.place_forget()
    gm5button.place_forget()
    gm6button.place_forget()
    gm7button.place_forget()
    gm8button.place_forget()
    gm9button.place_forget()
    
    er1button.place_forget()
    er2button.place_forget()
    er3button.place_forget()
    
    gobutton.place_forget()
    edbutton.place_forget()
    stbutton.place_forget()
    rtbutton.place_forget()
    
    canvas.create_image(250, 300, tag = "open")
    er1button.place(x = 600, y = 150)#0216
    #変更x = 180, y = 150
    er2button.place(x = 600, y = 350)#0216
    #変更x = 180, y = 250　
    er3button.place(x = 600, y = 550)#0216
    #変更x = 180, y = 350　
    stbutton.place(x = 250, y = 570)#0216
    #変更x = 350, y = 570
    
    
    mojiC.pack(anchor='n',expand=1)
    
    # mojiT.pack()
    mojiT.tag_configure("r", foreground="#FF0000")
    mojiT.tag_configure("g", foreground="#008000")
    mojiT.tag_configure("b", foreground="#0000FF")
    mojiT.tag_configure("t", foreground="#000000")
    mojiT.insert("end", "　　　　                            円・ ", 'r')#0216
    #変更
    mojiT.insert("end", "元・", 'g')
    mojiT.insert("end", "ドン", 'b')
    mojiT.insert("end", "をえらんでね！", 't')
    # mojiT.insert("end", str(num), 'g')
    # mojiT.insert("end", "円分払って！", 'b')
    mojiT.configure(state="disabled") # 読取専用に
    mojiT.pack(anchor='n',expand=1)
    
    numH = random.randint(1,3)
    if numH == 1:
        canvas.create_image(625, 300, image=imgSS32)#0216
        #変更x,y=250背景日本
        canvas.place(x=100, y=100)
        canvas.pack()
    elif numH == 2:
        canvas.create_image(625, 300, image=imgSS33)#0216
        #変更x,y=250背景中国
        canvas.place(x=100, y=100)
        canvas.pack()
    else:
        canvas.create_image(625, 300, image=imgSS34)#0216
        #変更x,y=250背景ベトナム
        canvas.place(x=100, y=100)
        canvas.pack()       
    hantei = 1
    
def opening1():
    
    global chkdel, zaq, mojiT2, mojiT, hint, bln2, chk2, bln, chk, mojiTg, mojiTd, play3, chohante, chohante2, chohante3, mojiA, mojiB, mojiD, mojiE, mojiG1, mojiG2
    
    canvas.delete("all") 
    er1button.place_forget()
    er2button.place_forget()
    er3button.place_forget()
    mojiB.pack_forget()
    mojiD.pack_forget()
    mojiE.pack_forget()
    mojiG1.pack_forget()
    mojiG2.pack_forget()
    mojiG3.pack_forget()
    mojiG4.pack_forget()
    mojiG5.pack_forget()
    mojiG6.pack_forget()
    mojiT.pack_forget()
    mojiT2.pack_forget()
    button.place_forget()
    gm1button.place_forget()
    gm2button.place_forget()
    gm3button.place_forget()
    gm4button.place_forget()
    gm5button.place_forget()
    gm6button.place_forget()
    gm7button.place_forget()
    gm8button.place_forget()
    gm9button.place_forget()
    
    er1button.place_forget()
    er2button.place_forget()
    er3button.place_forget()
    
    gobutton.place_forget()
    edbutton.place_forget()
    ed2button.place_forget()
    ed3button.place_forget()
    stbutton.place_forget() 
    #canvas.create_rectangle(0, 0, 500, 600, fill = "white", tag = "back")
    canvas.create_image(250, 300, tag = "open")
    
    
    gm1button.place(x = 580, y = 150)#0216
    #変更x = 180, y = 150
    gm3button.place(x = 580, y = 350)#0216
    #変更x = 180, y = 150
    stbutton.place(x = 350, y = 570)
    rtbutton.place(x = 100, y = 570)
    
    
    
    mojiC.pack(anchor='n',expand=1)
    
    mojiT2.tag_configure("r", foreground="#FF0000")
    mojiT2.tag_configure("g", foreground="#000000")
    mojiT2.tag_configure("b", foreground="#000000")
    mojiT2.tag_configure("t", foreground="#000000")
    mojiT2.insert("end", "　                                 『かんたん』", 'r')#02161218
    #変更
    mojiT2.insert("end", "から", 'g')
    mojiT2.insert("end", "クリア", 'b')
    mojiT2.insert("end", "しよう！", 't')
    # mojiT.insert("end", str(num), 'g')
    # mojiT.insert("end", "円分払って！", 'b')
    mojiT2.configure(state="disabled") # 読取専用に
    mojiT2.pack(anchor='n',expand=1)
    
    canvas.create_image(800, 550, image=imgSS13)#0216
    #変更250, 250, image=imgSS13
    canvas.place(x=100, y=100)
    canvas.pack()
    
    if chohante != 0:
        gm2button.config(state=tk.NORMAL)
        gm3button.config(state=tk.NORMAL)        
    else:
        gm2button.config(state=tk.DISABLED)
        gm3button.config(state=tk.DISABLED)
        
    bln.set(False)
    chk.place(x=400, y=480)#0216
    #変更chk.place(x=200, y=480)
    
    bln2.set(False)
    if chkdel == 1:
    #     chk2.place(x=200, y=480)
        chk2.place(x=800, y=480)#02161226
    
def opening2():
    
    global chkdel, zaq, imgSS41, imgSS42, imgSS43, imgSS44, imgSS45, imgSS46, imgSS47, imgSS48, imgSS49, bln2, chk2, bln, chk, hint, mojiT2, mojiT, mojiTg, mojiTd, chohante, chohante2, chohante3, mojiA, mojiB, mojiD, mojiE
    
    canvas.delete("all")
    
    edbutton.place_forget()
    ed2button.place_forget()
    ed3button.place_forget()
    er1button.place_forget()
    er2button.place_forget()
    er3button.place_forget()
    mojiB.pack_forget()
    mojiD.pack_forget()
    mojiE.pack_forget()
    mojiG1.pack_forget()
    mojiG2.pack_forget()
    mojiG3.pack_forget()
    mojiG4.pack_forget()
    mojiG5.pack_forget()
    mojiG6.pack_forget()
    mojiT.pack_forget()
    mojiT2.pack_forget()
    #canvas.create_rectangle(0, 0, 500, 600, fill = "white", tag = "back")
    canvas.create_image(250, 300, tag = "open")
    
    gm4button.place(x = 580, y = 150)#0216
    #変更x = 180, y = 150
    gm6button.place(x = 580, y = 350)#0216
    #変更x = 180, y = 150
    stbutton.place(x = 350, y = 570)
    rtbutton.place(x = 100, y = 570)
    
    
    mojiC.pack(anchor='n',expand=1)
    mojiT2.tag_configure("r", foreground="#FF0000")
    mojiT2.tag_configure("g", foreground="#000000")
    mojiT2.tag_configure("b", foreground="#000000")
    mojiT2.tag_configure("t", foreground="#000000")
    mojiT2.insert("end", "　                                 『かんたん』", 'r')#02161218
    #変更
    mojiT2.insert("end", "から", 'g')
    mojiT2.insert("end", "クリア", 'b')
    mojiT2.insert("end", "しよう！", 't')
    # mojiT.insert("end", str(num), 'g')
    # mojiT.insert("end", "円分払って！", 'b')
    mojiT2.configure(state="disabled") # 読取専用に
    mojiT2.pack(anchor='n',expand=1)
    
    
    canvas.create_image(800, 550, image=imgSS13)#02161218
    #変更250, 250, image=imgSS13, tag = "img"
    canvas.place(x=100, y=100)
    canvas.pack()
    
    
    if chohante2 != 0:
        gm5button.config(state=tk.NORMAL)
        gm6button.config(state=tk.NORMAL)
                
    else:
        gm5button.config(state=tk.DISABLED)
        gm6button.config(state=tk.DISABLED)
             
    bln.set(False)
    chk.place(x=400, y=480)#0216
    #変更chk.place(x=200, y=480)
    
    bln2.set(False)
    if chkdel == 1:#02161226
    #     chk2.place(x=200, y=480)
        chk2.place(x=800, y=480)#02161226
    
    
    imgSS41 = tk.PhotoImage(file = 'imgSS/100元札_ミニ.png', master = root)
    imgSS42 = tk.PhotoImage(file = 'imgSS/50元札_ミニ.png', master = root)
    imgSS43 = tk.PhotoImage(file = 'imgSS/10元札_ミニ.png', master = root)
    imgSS44 = tk.PhotoImage(file = 'imgSS/5元札_ミニ.png', master = root)
    imgSS45 = tk.PhotoImage(file = 'imgSS/1元札_ミニ.png', master = root)
    imgSS46 = tk.PhotoImage(file = 'imgSS/5角札_ミニ.png', master = root)
    imgSS47 = tk.PhotoImage(file = 'imgSS/1角札_ミニ.png', master = root)
    imgSS48 = tk.PhotoImage(file = 'imgSS/5角硬貨_ミニ.png', master = root)
    imgSS49 = tk.PhotoImage(file = 'imgSS/1角硬貨_ミニ.png', master = root)
    
    
def opening3():
    
    global chkdel, zaq, imgSS41, imgSS42, imgSS43, imgSS44, imgSS45, imgSS46, imgSS47, imgSS48, imgSS49, bln2, chk2, bln, chk, hint, mojiT2, mojiT, mojiTg, mojiTd, chohante, chohante2, chohante3, mojiA, mojiB, mojiD, mojiE
    
    canvas.delete("all")
    
    er1button.place_forget()
    er2button.place_forget()
    er3button.place_forget()
    mojiB.pack_forget()
    mojiD.pack_forget()
    mojiE.pack_forget()
    mojiG1.pack_forget()
    mojiG2.pack_forget()
    mojiG3.pack_forget()
    mojiG4.pack_forget()
    mojiG5.pack_forget()
    mojiG6.pack_forget()
    mojiT.pack_forget()
    #canvas.create_rectangle(0, 0, 500, 600, fill = "white", tag = "back")
    canvas.create_image(250, 300, tag = "open")
    gm7button.place(x = 580, y = 150)#02161218
    #変更x = 180, y = 150
    gm9button.place(x = 580, y = 350)#02161218
    #変更x = 180, y = 350
    stbutton.place(x = 350, y = 570)
    rtbutton.place(x = 100, y = 570)
    
    
    mojiC.pack(anchor='n',expand=1)
    mojiT2.tag_configure("r", foreground="#FF0000")
    mojiT2.tag_configure("g", foreground="#000000")
    mojiT2.tag_configure("b", foreground="#000000")
    mojiT2.tag_configure("t", foreground="#000000")
    mojiT2.insert("end", "　                                 『かんたん』", 'r')#02161218
    #変更
    mojiT2.insert("end", "から", 'g')
    mojiT2.insert("end", "クリア", 'b')
    mojiT2.insert("end", "しよう！", 't')
    # mojiT.insert("end", str(num), 'g')
    # mojiT.insert("end", "円分払って！", 'b')
    mojiT2.configure(state="disabled") # 読取専用に
    mojiT2.pack(anchor='n',expand=1)
    
    canvas.create_image(800, 550, image=imgSS13)#02161218
    #変更250, 250, image=imgSS13, tag = "img" 筋トレ女性の絵 tag img は下手につけてはだめ
    canvas.place(x=100, y=100)
    canvas.pack()
    
    
    if chohante3 != 0:
        gm8button.config(state=tk.NORMAL)
        gm9button.config(state=tk.NORMAL)
        
    else:
        gm8button.config(state=tk.DISABLED)
        gm9button.config(state=tk.DISABLED)
    
        
    bln.set(False)
    chk.place(x=400, y=480)#02161218
    #変更x=200, y=480
    
    bln2.set(False)
    if chkdel == 1:
    #     chk2.place(x=200, y=480)
        chk2.place(x=800, y=480)#02161226
    
    
    
    imgSS41 = None
    imgSS42 = tk.PhotoImage(file = 'imgSS/50万ドン_ミニ.png', master = root)
    imgSS43 = tk.PhotoImage(file = 'imgSS/10万ドン_ミニ.png', master = root)
    imgSS44 = tk.PhotoImage(file = 'imgSS/5万ドン_ミニ.png', master = root)
    imgSS45 = tk.PhotoImage(file = 'imgSS/1万ドン_ミニ.png', master = root)
    imgSS46 = tk.PhotoImage(file = 'imgSS/5千ドン_ミニ.png', master = root)
    imgSS47 = tk.PhotoImage(file = 'imgSS/千ドン_ミニ.png', master = root)
    imgSS48 = tk.PhotoImage(file = 'imgSS/5百ドン_ミニ.png', master = root)
    imgSS49 = tk.PhotoImage(file = 'imgSS/百ドン_ミニ.png', master = root)
    
def gaming1():
    
    global zaq, chk, bln, chk2, bln2, gengo, imgSS41, imgSS42, imgSS43, imgSS44, imgSS45, imgSS46, imgSS47, imgSS48, imgSS49, atohint1, atohint2, atohint3, atohint4, atohint5, mojiT, mojiT2, k3once, bln, hint, k3, mojiTg, mojiTd, mojiT, numM1, numM2, numM3, numM4, numM5, play3, ima, sttime, stptime, mouhante, mojiA, mojiB, mojiC, mojiD, mojiF, mojiG1, mojiG2, numF, stptime, yoidon, imgSS101, imgSS102, imgSS103, imgSS104, imgSS105, k15, chohante, chohante2, chohante3#0128kaijoグローバル付け足し
    ima = time.time()
    stptime = 0
    sttime = 3
    play3()    
    imgSS41 = tk.PhotoImage(file = 'imgSS/10000円札_ミニ.png', master = root)
    imgSS42 = tk.PhotoImage(file = 'imgSS/5000円札_ミニ.png', master = root)
    imgSS43 = tk.PhotoImage(file = 'imgSS/1000円札_ミニ.png', master = root)
    imgSS44 = tk.PhotoImage(file = 'imgSS/500円硬貨_ミニ.png', master = root)
    imgSS45 = tk.PhotoImage(file = 'imgSS/100円硬貨_ミニ.png', master = root)
    imgSS46 = tk.PhotoImage(file = 'imgSS/50円硬貨_ミニ.png', master = root)
    imgSS47 = tk.PhotoImage(file = 'imgSS/10円硬貨_ミニ.png', master = root)
    imgSS48 = tk.PhotoImage(file = 'imgSS/5円硬貨_ミニ.png', master = root)
    imgSS49 = tk.PhotoImage(file = 'imgSS/1円硬貨_ミニ.png', master = root)
    
    num = random.randint(1,1000)
    numM1 = random.randint(99,11000)
    atohint1(numM1)
    numM2 = random.randint(99,11000)
    atohint2(numM2)
    numM3 = random.randint(99,11000)
    atohint3(numM3)
    numM4 = random.randint(99,11000)
    atohint4(numM4)
    numM5 = random.randint(99,11000)
    atohint5(numM5)
    
    imgSS101 = None#作ってもらったはずなのに自分で再作成0128kaijo　5行　gaming4や7にも増殖
    imgSS102 = None
    imgSS103 = None
    imgSS104 = None
    imgSS105 = None
    
    
    gm1button.place_forget()
    gm2button.place_forget()
    gm3button.place_forget()
    gm4button.place_forget()
    gm5button.place_forget()
    gm6button.place_forget()
    gm7button.place_forget()
    gm8button.place_forget()
    gm9button.place_forget()
    stbutton.place_forget()
    mojiD.pack_forget()
    mojiA.pack_forget()
    mojiB.pack_forget()
    mojiG1.pack_forget()
    mojiG2.pack_forget()
    mojiG3.pack_forget()
    mojiG4.pack_forget()
    mojiG5.pack_forget()
    mojiG6.pack_forget()
    chk.place_forget()
    chk2.place_forget()
    mojiT.pack_forget()
    mojiT2.pack_forget()
    
    stbutton.place_forget()
    rtbutton.place_forget()
    
    canvas.delete("all")
    
    canvas.create_image(570, 570, image=imgSS98)#02161218
    #変更1000, 1000, image=imgSS98
    canvas.place(x=400, y=400)
    canvas.pack()
    
   
    
    #自分が追加した箇所        
    k3button.place(x=1090, y=110)
    #変更x=390, y=110
    k15button.place(x=1090, y=760)
        
    a1man = random.randint(1,400)
    b1man = random.randint(100,500)
    canvas.create_image(a1man, b1man, image=imgSS6, tags = "img")
    canvas.place(x=100, y=100)
    canvas.pack()
    
    a5000 = random.randint(1,400)
    b5000 = random.randint(100,500)
    canvas.create_image(a5000, b5000, image=imgSS2, tags = "img2")
    canvas.place(x=100, y=100)
    canvas.pack()
        
        
    for i in range(4):
        a1000 = random.randint(1,400)
        b1000 = random.randint(100,500)
        canvas.create_image(a1000, b1000, image=imgSS7, tags = "img3")
        canvas.place(x=100, y=100)
        canvas.pack()
        
    a500 = random.randint(1,400)
    b500 = random.randint(100,500)
    canvas.create_image(a500, b500, image=imgSS3, tags = "img4")
    canvas.place(x=100, y=100)
    canvas.pack()
     
    for i in range(4):
        a100 = random.randint(1,400)
        b100 = random.randint(100,500)
        canvas.create_image(a100, b100, image=imgSS8, tags = "img5")
        canvas.place(x=100, y=100)
        canvas.pack()
        
    a50 = random.randint(1,400)
    b50 = random.randint(100,500)
    canvas.create_image(a50, b50, image=imgSS4, tags = "img6")
    canvas.place(x=100, y=100)
    canvas.pack()
        
    for i in range(4):
        a10 = random.randint(1,400)
        b10 = random.randint(100,500)
        canvas.create_image(a10, b10, image=imgSS9, tags = "img7")
        canvas.place(x=100, y=100)
        canvas.pack()
        
    a5en = random.randint(1,400)
    b5en = random.randint(100,500)
    canvas.create_image(a5en, b5en, image=imgSS5, tags = "img8")
    canvas.place(x=100, y=100)
    canvas.pack()
        
    for i in range(4):
        a1en = random.randint(1,400)
        b1en = random.randint(100,500)
        canvas.create_image(a1en, b1en, image=imgSS10, tags = "img9")
        canvas.place(x=100, y=100)
        canvas.pack()
        
    mouhante = 1
    
    numF = random.randint(1,1000)
    mojiF = tk.Label(text = "                                                    トレーに"+str(numF)+"円分払って")#02161218
    #変更
    # チェックされているか？
    if bln.get():
        hint = 1
    else:
        hint = 0
    # チェック2されているか？
    if bln2.get():
        zaq = 1
    else:
        zaq = 0
    
    
    
    zm1button.place(x=860,y=100)#s0122 0128kaijo
    gengo = 1
    k3once = 3
 
    
    
def gaming2():
    
    global zaq, chk, bln, chk2, bln2, chk, bln, hint, chk, mojiT, mojiT2, mojiTg, mojiTd, numM1, numM2, numM3, numM4, numM5, mojiT, play3, mojiA, mojiB, mojiC, mojiD, mojiF, sttime, stptime, ima, chohante, chohante2, chohante3    
    ima = time.time()
    stptime = 0
    sttime = 3
    chohante += 1000
    play3()    
    numM1 = random.randint(99,11000)
    numM2 = random.randint(99,11000)
    numM3 = random.randint(99,11000)
    numM4 = random.randint(99,11000)
    numM5 = random.randint(99,11000)
    
    gm1button.place_forget()
    gm2button.place_forget()
    gm3button.place_forget()
    gm4button.place_forget()
    gm5button.place_forget()
    gm6button.place_forget()
    gm7button.place_forget()
    gm8button.place_forget()
    gm9button.place_forget()
    
    stbutton.place_forget()
    mojiD.pack_forget()
    mojiA.pack_forget()
    mojiB.pack_forget()
    mojiG1.pack_forget()
    mojiG2.pack_forget()
    mojiG3.pack_forget()
    mojiG4.pack_forget()
    mojiG5.pack_forget()
    mojiG6.pack_forget()
    
    chk.place_forget()
    chk2.place_forget()
    mojiT.pack_forget()
    mojiT2.pack_forget()
    
    stbutton.place_forget()
    rtbutton.place_forget()
    
    
    canvas.delete("all")
    
    
    
    numF = random.randint(1,1000)
    mojiF = tk.Label(text = "トレーに"+str(numF)+"円分払って！")
    
    mojiT.pack(anchor='n',expand=1)
   
    
    #自分が追加した箇所        
    k3button.place(x=390, y=110)
    
    
    
    hairetsu = []
    ii = random.randint(0, 5)
    iii = random.randint(0, 5)
    iv = random.randint(0, 5)
    v = random.randint(0, 5)
    vi = random.randint(0, 5)
    vii = random.randint(0, 5)
    viii = random.randint(1, 5)
    
    
    hid = [ii, iii, iv, v, vi, vii, viii]
    
    for k in range(7):
        hairetsu.append(hid[k])
    
    
    for z in range(hairetsu[6]*5):
        for w1 in range(hairetsu[0]):
            a1 = random.randint(1,400)
            b1 = random.randint(100,500)
            canvas.create_image(a1, b1, image=imgSS17, tags = "img")
            canvas.place(x=100, y=100)
            canvas.pack()  
        for w2 in range(hairetsu[1]):
            a2 = random.randint(1,400)
            b2 = random.randint(100,500)
            canvas.create_image(a2, b2, image=imgSS18, tags = "img")
            canvas.place(x=100, y=100)
            canvas.pack()
        for d1 in range(hairetsu[2]):
            a3 = random.randint(1,400)
            b3 = random.randint(100,500)
            canvas.create_image(a3, b3, image=imgSS19, tags = "img")
            canvas.place(x=100, y=100)
            canvas.pack()  
        for d2 in range(hairetsu[3]):
            a4 = random.randint(1,400)
            b4 = random.randint(100,500)
            canvas.create_image(a4, b4, image=imgSS20, tags = "img")
            canvas.place(x=100, y=100)
            canvas.pack()
        for g1 in range(hairetsu[4]):
            a3 = random.randint(1,400)
            b3 = random.randint(100,500)
            canvas.create_image(a3, b3, image=imgSS21, tags = "img")
            canvas.place(x=100, y=100)
            canvas.pack()  
        for g2 in range(hairetsu[5]):
            a4 = random.randint(1,400)
            b4 = random.randint(100,500)
            canvas.create_image(a4, b4, image=imgSS22, tags = "img")
            canvas.place(x=100, y=100)
            canvas.pack()
            
            
    # チェックされているか？
    if bln.get():
        hint = 1
    else:
        hint = 0
        
    # [結果] チェックされています
    # チェック2されているか？
    if bln2.get():
        zaq = 1
    else:
        zaq = 0
    
def gaming3():
    
    global zaq, chk, bln, chk2, bln2, gengo, emojiTn, gengo, gengo2, k3once, imgSS121, imgSS122, imgSS123, imgSS124, imgSS125, imgSS101, imgSS102, imgSS103, imgSS104, imgSS105, atohint1, atohint2, atohint3, atohint4, atohint5, imgMA, imgMB, imgMC, imgMD, imgME, imgMF, imgMG, imgMH, imgMI, imgMJ, count, ret1, ret2, ret3, ret4, ret5, challenge, imgSS50, chk, bln, hint, mojiT, mojiT2, chk, mojiTg, mojiTd, emojiT, numM1, numM2, numM3, numM4, numM5, mojiT, play3, mojiA, mojiB, mojiC, mojiD, mojiF, flag, stptime, sttime, ima, chohante, chohante2, chohante3    
    ima = time.time()
    stptime = 0
    sttime = 3
    chohante += 1000
    play3()
    numM1 = 0
    imgMA = imgSS50
    imgMB = imgSS50    
    ret1 = challenge(imgMA, imgMB, numM1)
    count = 0
    for v in ret1:
        count += 1
        if count == 1:
            imgMA = v
        elif count == 2:
            imgMB = v
        else:
            numM1 = v
            
    atohint1(numM1)
    
    numM2 = 0
    imgMC = imgSS50
    imgMD = imgSS50
    ret2 = challenge(imgMC, imgMD, numM2)
    count = 0
    for vw in ret2:
        count += 1
        if count == 1:
            imgMC = vw
        elif count == 2:
            imgMD = vw
        else:
            numM2 = vw
            
    atohint2(numM2)
    
    numM3 = 0
    imgME = imgSS50
    imgMF = imgSS50
    ret3 = challenge(imgME, imgMF, numM3)
    
    count = 0
    for vwx in ret3:
        count += 1
        if count == 1:
            imgME = vwx
        elif count == 2:
            imgMF = vwx
        else:
            numM3 = vwx
            
    atohint3(numM3)
    
    
    numM4 = 0
    imgMG = imgSS50
    imgMH = imgSS50
    ret4 = challenge(imgMG, imgMH, numM4)
    
    count = 0
    for vwxy in ret4:
        count += 1
        if count == 1:
            imgMG = vwxy
        elif count == 2:
            imgMH = vwxy
        else:
            numM4 = vwxy
            
    atohint4(numM4)
    numM5 = 0
    imgMI = imgSS50
    imgMJ = imgSS50
    ret5 = challenge(imgMI, imgMJ, numM5)
    
    count = 0
    for vwxyz in ret5:
        count += 1
        if count == 1:
            imgMI = vwxyz
        elif count == 2:
            imgMJ = vwxyz
        else:
            numM5 = vwxyz
            
    atohint5(numM5)
    
    imgSS101 = imgMA
    imgSS102 = imgMC
    imgSS103 = imgME
    imgSS104 = imgMG
    imgSS105 = imgMI
    imgSS121 = imgMB
    imgSS122 = imgMD
    imgSS123 = imgMF
    imgSS124 = imgMH
    imgSS125 = imgMJ
    
    
    gm1button.place_forget()
    gm2button.place_forget()
    gm3button.place_forget()
    gm4button.place_forget()
    gm5button.place_forget()
    gm6button.place_forget()
    gm7button.place_forget()
    gm8button.place_forget()
    gm9button.place_forget()
    
    stbutton.place_forget()
    mojiD.pack_forget()
    mojiA.pack_forget()
    mojiB.pack_forget()
    mojiG1.pack_forget()
    mojiG2.pack_forget()
    mojiG3.pack_forget()
    mojiG4.pack_forget()
    mojiG5.pack_forget()
    mojiG6.pack_forget()
    
    
    chk.place_forget()
    chk2.place_forget()
    
    mojiT.pack_forget()
    mojiT2.pack_forget()
    
    stbutton.place_forget()
    rtbutton.place_forget()
    
    canvas.delete("all")
    
    
    numF = random.randint(1,1000)
    mojiF = tk.Label(text = "トレーに"+str(numF)+"円分払って")
    
    
    
    canvas.create_image(250, 150, image=imgSS96)
    canvas.place(x=150, y=150)
    canvas.pack()
    emojiT.pack(anchor='n',expand=1)
   
    
    #自分が追加した箇所        
    k3button.place(x=1090, y=110)#02161218
    k15button.place(x=1090, y=760)
    canvas.create_image(50, 50, image=imgMA)
    canvas.place(x=100, y=100)
    canvas.pack()
    
    canvas.create_image(210, 50, image=imgMB)
    canvas.place(x=100, y=100)
    canvas.pack()
    
    canvas.create_image(130, 50, image=imgSS109, tags = "mig")#02160125
    canvas.place(x=100, y=100)
    canvas.pack()
    canvas.create_image(290, 50, image=imgSS115, tags = "mig")#02160125)
    canvas.place(x=100, y=100)
    canvas.pack()
    canvas.create_image(370, 53, image=imgSS116)
    canvas.place(x=100, y=100)
    canvas.pack()
                        
    a1man = random.randint(1,400)
    b1man = random.randint(100,500)
    canvas.create_image(a1man, b1man, image=imgSS6, tags = "img")
    canvas.place(x=100, y=100)
    canvas.pack()
    
    a5000 = random.randint(1,400)
    b5000 = random.randint(100,500)
    canvas.create_image(a5000, b5000, image=imgSS2, tags = "img2")
    canvas.place(x=100, y=100)
    canvas.pack()
        
        
    for i in range(4):
        a1000 = random.randint(1,400)
        b1000 = random.randint(100,500)
        canvas.create_image(a1000, b1000, image=imgSS7, tags = "img3")
        canvas.place(x=100, y=100)
        canvas.pack()
        
    a500 = random.randint(1,400)
    b500 = random.randint(100,500)
    canvas.create_image(a500, b500, image=imgSS3, tags = "img4")
    canvas.place(x=100, y=100)
    canvas.pack()
     
    for i in range(4):
        a100 = random.randint(1,400)
        b100 = random.randint(100,500)
        canvas.create_image(a100, b100, image=imgSS8, tags = "img5")
        canvas.place(x=100, y=100)
        canvas.pack()
        
    a50 = random.randint(1,400)
    b50 = random.randint(100,500)
    canvas.create_image(a50, b50, image=imgSS4, tags = "img6")
    canvas.place(x=100, y=100)
    canvas.pack()
        
    for i in range(4):
        a10 = random.randint(1,400)
        b10 = random.randint(100,500)
        canvas.create_image(a10, b10, image=imgSS9, tags = "img7")
        canvas.place(x=100, y=100)
        canvas.pack()
        
    a5en = random.randint(1,400)
    b5en = random.randint(100,500)
    canvas.create_image(a5en, b5en, image=imgSS5, tags = "img8")
    canvas.place(x=100, y=100)
    canvas.pack()
        
    for i in range(4):
        a1en = random.randint(1,400)
        b1en = random.randint(100,500)
        canvas.create_image(a1en, b1en, image=imgSS10, tags = "img9")
        canvas.place(x=100, y=100)
        canvas.pack()
    
    
    
    # チェックされているか？
    if bln.get():
        hint = 1
    else:
        hint = 0
        
    # [結果] チェックされています
    # チェック2されているか？
    if bln2.get():
        zaq = 1
    else:
        zaq = 0
    
    zm1button.place(x=860,y=100)#s0122 0128kaijo
    
    
    gengo = -1
    k3once = 3
    
def gaming4():
    
    global zaq, chk, bln, chk2, bln2, gengo2, imgSS41, imgSS42, imgSS43, imgSS44, imgSS45, imgSS46, imgSS47, imgSS48, imgSS49, atohint5, atohint4, atohint3, atohint2, atohint1, chk, bln, hint, gengo, k3once, mojiT, mojiTn, mojiT2, mojiTg, mojiTd, emojiT, emojiTn, mojiTg, mojiTd, numM1, numM2, numM3, numM4, numM5, mojiT, play3, mouhante, mojiA, mojiB, mojiC, mojiD, mojiF, stptime, sttime, ima, imgSS101, imgSS102, imgSS103, imgSS104, imgSS105, chohante, chohante2, chohante3#0128kaijoグローバル付け足し
    ima = time.time()
    stptime = 0
    sttime = 3
    play3()    
    imgSS41 = tk.PhotoImage(file = 'imgSS/100元札_ミニ.png', master = root)
    imgSS42 = tk.PhotoImage(file = 'imgSS/50元札_ミニ.png', master = root)
    imgSS43 = tk.PhotoImage(file = 'imgSS/10元札_ミニ.png', master = root)
    imgSS44 = tk.PhotoImage(file = 'imgSS/5元札_ミニ.png', master = root)
    imgSS45 = tk.PhotoImage(file = 'imgSS/1元札_ミニ.png', master = root)
    imgSS46 = tk.PhotoImage(file = 'imgSS/5角札_ミニ.png', master = root)
    imgSS47 = tk.PhotoImage(file = 'imgSS/1角札_ミニ.png', master = root)
    imgSS48 = None
    imgSS49 = None
    
    gengo2 = 2
    
    numM1 = 100*(random.randint(1,110)+round(random.random(), 1))
    atohint1(numM1)
    numM2 = 100*(random.randint(1,110)+round(random.random(), 1))
    atohint2(numM2)
    numM3 = 100*(random.randint(1,110)+round(random.random(), 1))
    atohint3(numM3)
    numM4 = 100*(random.randint(1,110)+round(random.random(), 1))
    atohint4(numM4)
    numM5 = 100*(random.randint(1,110)+round(random.random(), 1))
    atohint5(numM5)
    
    imgSS101 = None#作ってもらったはずなのに自分で再作成0128kaijo　5行　gaming4や7にも増殖
    imgSS102 = None
    imgSS103 = None
    imgSS104 = None
    imgSS105 = None
    
    
    
    gm1button.place_forget()
    gm2button.place_forget()
    gm3button.place_forget()
    gm4button.place_forget()
    gm5button.place_forget()
    gm6button.place_forget()
    gm7button.place_forget()
    gm8button.place_forget()
    gm9button.place_forget()
    
    stbutton.place_forget()
    mojiD.pack_forget()
    mojiA.pack_forget()
    mojiB.pack_forget()
    mojiG1.pack_forget()
    mojiG2.pack_forget()
    mojiG3.pack_forget()
    mojiG4.pack_forget()
    mojiG5.pack_forget()
    mojiG6.pack_forget()
    emojiT.pack_forget()
    emojiTn.pack_forget()
    mojiT.pack_forget()
    mojiT2.pack_forget()
    mojiTd.pack_forget()
    mojiTg.pack_forget()
    mojiTn.pack_forget()
    
    chk.place_forget()
    chk2.place_forget()
    
    rtbutton.place_forget()
    
    canvas.delete("all")
    
    
    numF = random.randint(1,1000)
    mojiF = tk.Label(text = "トレーに"+str(numF)+"ウォン分払って")
    
    #変更150, 100, 350, 0, fill='cornflowerblue'
   
    
    #自分が追加した箇所        
    k3button.place(x=1090, y=110)#02161218
    #変更x=390, y=110
    k15button.place(x=1090, y=760)
    
    for i in range(5):
        a = random.randint(1,400)
        b = random.randint(100,500)
        canvas.create_image(a, b, image=imgSS21, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
        canvas.create_image(a+200, b+200, image=imgSS22, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
        canvas.create_image(a+200, b+200, image=imgSS31, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
        
        
        
    mouhante = 2
    
    # チェックされているか？
    if bln.get():
        hint = 1
    else:
        hint = 0
        
    # [結果] チェックされています
    # チェック2されているか？
    if bln2.get():
        zaq = 1
    else:
        zaq = 0
    
    zm1button.place(x=860,y=100)#s0122 0128kaijo
    
    
    gengo = 2
    k3once = 3
    
def gaming5():
    
    global zaq, chk, bln, chk2, bln2, gengo2, chk, bln, hint, gengo, mojiT, mojiTn, mojiT2, mojiTg, mojiTd, emojiT, emojiTn, mojiTg, mojiTd, mojiTg, mojiTd, numM1, numM2, numM3, numM4, numM5, mojiT, play3, mojiA, mojiB, mojiC, mojiD, mojiF, stptime, sttime, ima, chohante, chohante2, chohante3    
    ima = time.time()
    stptime = 0
    sttime = 3
    chohante2 += 1000
    play3()    
    gengo2 = 2
    
    numM1 = random.randint(1,110)+round(random.random(), 1)
    numM2 = random.randint(1,110)+round(random.random(), 1)
    numM3 = random.randint(1,110)+round(random.random(), 1)
    numM4 = random.randint(1,110)+round(random.random(), 1)
    numM5 = random.randint(1,110)+round(random.random(), 1)
    
    gm1button.place_forget()
    gm2button.place_forget()
    gm3button.place_forget()
    gm4button.place_forget()
    gm5button.place_forget()
    gm6button.place_forget()
    gm7button.place_forget()
    gm8button.place_forget()
    gm9button.place_forget()
    
    stbutton.place_forget()
    mojiD.pack_forget()
    mojiA.pack_forget()
    mojiB.pack_forget()
    mojiG1.pack_forget()
    mojiG2.pack_forget()
    mojiG3.pack_forget()
    mojiG4.pack_forget()
    mojiG5.pack_forget()
    mojiG6.pack_forget()
    emojiT.pack_forget()
    emojiTn.pack_forget()
    mojiT.pack_forget()
    mojiT2.pack_forget()
    mojiTd.pack_forget()
    mojiTg.pack_forget()
    
    chk.place_forget()
    chk2.place_forget()
    
    rtbutton.place_forget()
    
    canvas.delete("all")
    
    
    numF = random.randint(1,1000)
    mojiF = tk.Label(text = "トレーに"+str(numF)+"ウォン分払って")
    
    #変更150, 100, 350, 0, fill='cornflowerblue'
   
    
    #自分が追加した箇所        
    k3button.place(x=1090, y=110)
    k15button.place(x=1090, y=760)
    
    for i in range(5):
        a = random.randint(1,400)
        b = random.randint(100,500)
        canvas.create_image(a, b, image=imgSS17, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
        canvas.create_image(a+200, b+200, image=imgSS18, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
    
    hairetsu = []
    ii = random.randint(0, 5)
    iii = random.randint(0, 5)
    iv = random.randint(0, 5)
    v = random.randint(0, 5)
    vi = random.randint(0, 5)
    vii = random.randint(0, 5)
    viii = random.randint(0, 5)
    ix = random.randint(0, 5)
    xi = random.randint(0, 5)
    xii = random.randint(0, 5)
    xiii = random.randint(0, 5)
    xiv = random.randint(0, 5)
    xv = random.randint(0, 5)
    xvi = random.randint(0, 5)
    xvii = random.randint(0, 5)
    xviii = random.randint(0, 5)
    xix = random.randint(0, 5)
    xx = random.randint(0, 5)
    
    hid = [ii, iii, iv, v, vi, vii, viii, ix, xi, xii, xiii, xiv, xv, xvi, xvii, xviii, xix, xx]
    
    for l in range(18):
        hairetsu.append(hid[l])
    
    for i1 in range(hairetsu[0]):
        a1 = random.randint(1,400)
        b1 = random.randint(100,500)
        canvas.create_image(a1, b1, image=imgSS2, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()  
    for i2 in range(hairetsu[1]):
        a2 = random.randint(1,400)
        b2 = random.randint(100,500)
        canvas.create_image(a2, b2, image=imgSS3, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
    for i3 in range(hairetsu[2]):
        a3 = random.randint(1,400)
        b3 = random.randint(100,500)
        canvas.create_image(a3, b3, image=imgSS4, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()  
    for i4 in range(hairetsu[3]):
        a4 = random.randint(1,400)
        b4 = random.randint(100,500)
        canvas.create_image(a4, b4, image=imgSS5, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
    for i5 in range(hairetsu[4]):
        a5 = random.randint(1,400)
        b5 = random.randint(100,500)
        canvas.create_image(a5, b5, image=imgSS6, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()  
    for i6 in range(hairetsu[5]):
        a6 = random.randint(1,400)
        b6 = random.randint(100,500)
        canvas.create_image(a6, b6, image=imgSS7, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
    for i7 in range(hairetsu[6]):
        a7 = random.randint(1,400)
        b7 = random.randint(100,500)
        canvas.create_image(a7, b7, image=imgSS8, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()  
    for i8 in range(hairetsu[7]):
        a8 = random.randint(1,400)
        b8 = random.randint(100,500)
        canvas.create_image(a8, b8, image=imgSS9, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
    for i9 in range(hairetsu[8]):
        a9 = random.randint(1,400)
        b9 = random.randint(100,500)
        canvas.create_image(a9, b9, image=imgSS10, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()  
    # チェックされているか？
    if bln.get():
        hint = 1
    else:
        hint = 0
        
    # [結果] チェックされています
    # チェック2されているか？
    if bln2.get():
        zaq = 1
    else:
        zaq = 0
    
    gengo = 2
      
def gaming6():
    
    global zaq, chk, bln, chk2, bln2, gengo2, imgSS41, imgSS42, imgSS43, imgSS44, imgSS45, imgSS46, imgSS47, imgSS48, imgSS49, atohint5, atohint4, atohint3, atohint2, atohint1, gengo, emojiTn, gengo, gengo2, k3once, imgSS121, imgSS122, imgSS123, imgSS124, imgSS125, imgSS101, imgSS102, imgSS103, imgSS104, imgSS105, atohint1, atohint2, atohint3, atohint4, atohint5, imgMA, imgMB, imgMC, imgMD, imgME, imgMF, imgMG, imgMH, imgMI, imgMJ, count, ret1, ret2, ret3, ret4, ret5, challenge, imgSS50, gengo2, chk, bln, hint, gengo, mojiT, mojiTn, mojiT2, mojiTg, mojiTd, emojiT, emojiTn, mojiTg, mojiTd, mojiTg, mojiTd, numM1, numM2, numM3, numM4, numM5, mojiT, play3, mojiA, mojiB, mojiC, mojiD, mojiF, flag, stptime, sttime, ima, chohante, chohante2, chohante3
    ima = time.time()
    stptime = 0
    sttime = 3
    chohante2 += 1000
    play3()    
    imgSS41 = tk.PhotoImage(file = 'imgSS/100元札_ミニ.png', master = root)
    imgSS42 = tk.PhotoImage(file = 'imgSS/50元札_ミニ.png', master = root)
    imgSS43 = tk.PhotoImage(file = 'imgSS/10元札_ミニ.png', master = root)
    imgSS44 = tk.PhotoImage(file = 'imgSS/5元札_ミニ.png', master = root)
    imgSS45 = tk.PhotoImage(file = 'imgSS/1元札_ミニ.png', master = root)
    imgSS46 = tk.PhotoImage(file = 'imgSS/5角札_ミニ.png', master = root)
    imgSS47 = tk.PhotoImage(file = 'imgSS/1角札_ミニ.png', master = root)
    imgSS48 = None
    imgSS49 = None
    
    gengo2 = 2
    
 
    numM1 = 0
    imgMA = imgSS50
    imgMB = imgSS50    
    ret1 = challenge(imgMA, imgMB, numM1)
    count = 0
    for v in ret1:
        count += 1
        if count == 1:
            imgMA = v
        elif count == 2:
            imgMB = v
        else:
            numM1 = v
            
    numM1 *= 100
    atohint1(numM1)
        
    
    
    numM2 = 0
    imgMC = imgSS50
    imgMD = imgSS50
    ret2 = challenge(imgMC, imgMD, numM2)
    count = 0
    for vw in ret2:
        count += 1
        if count == 1:
            imgMC = vw
        elif count == 2:
            imgMD = vw
        else:
            numM2 = vw
            
    numM2 *= 100
    atohint2(numM2)
    
    numM3 = 0
    imgME = imgSS50
    imgMF = imgSS50
    ret3 = challenge(imgME, imgMF, numM3)
    
    count = 0
    for vwx in ret3:
        count += 1
        if count == 1:
            imgME = vwx
        elif count == 2:
            imgMF = vwx
        else:
            numM3 = vwx
            
    numM3 *= 100
    atohint3(numM3)
    
    
    numM4 = 0
    imgMG = imgSS50
    imgMH = imgSS50
    ret4 = challenge(imgMG, imgMH, numM4)
    
    count = 0
    for vwxy in ret4:
        count += 1
        if count == 1:
            imgMG = vwxy
        elif count == 2:
            imgMH = vwxy
        else:
            numM4 = vwxy
            
    numM4 *= 100
    atohint4(numM4)
    numM5 = 0
    imgMI = imgSS50
    imgMJ = imgSS50
    ret5 = challenge(imgMI, imgMJ, numM5)
    
    count = 0
    for vwxyz in ret5:
        count += 1
        if count == 1:
            imgMI = vwxyz
        elif count == 2:
            imgMJ = vwxyz
        else:
            numM5 = vwxyz
            
    numM5 *= 100
    atohint5(numM5)
    
    imgSS101 = imgMA
    imgSS102 = imgMC
    imgSS103 = imgME
    imgSS104 = imgMG
    imgSS105 = imgMI
    imgSS121 = imgMB
    imgSS122 = imgMD
    imgSS123 = imgMF
    imgSS124 = imgMH
    imgSS125 = imgMJ
    
    
    gm1button.place_forget()
    gm2button.place_forget()
    gm3button.place_forget()
    gm4button.place_forget()
    gm5button.place_forget()
    gm6button.place_forget()
    gm7button.place_forget()
    gm8button.place_forget()
    gm9button.place_forget()
    
    stbutton.place_forget()
    mojiD.pack_forget()
    mojiA.pack_forget()
    mojiB.pack_forget()
    mojiG1.pack_forget()
    mojiG2.pack_forget()
    mojiG3.pack_forget()
    mojiG4.pack_forget()
    mojiG5.pack_forget()
    mojiG6.pack_forget()
    emojiT.pack_forget()
    emojiTn.pack_forget()
    mojiT.pack_forget()
    mojiT2.pack_forget()
    mojiTd.pack_forget()
    mojiTg.pack_forget()
    mojiTn.pack_forget()
    
    chk.place_forget()
    chk2.place_forget()
    
    rtbutton.place_forget()
    canvas.delete("all")
    
    
    numF = random.randint(1,1000)
    mojiF = tk.Label(text = "トレーに"+str(numF)+"ウォン分払って")
    
    #変更150, 100, 350, 0, fill='cornflowerblue'
    canvas.create_image(250, 150, image=imgSS96)
    canvas.place(x=150, y=150)
    canvas.pack()
    emojiT.pack(anchor='n',expand=1)
   
    
    #自分が追加した箇所        
    k3button.place(x=1090, y=110)#02161218
    #変更x=390, y=110
    k15button.place(x=1090, y=760)
    
    canvas.create_image(50, 50, image=imgMA)
    canvas.place(x=100, y=100)
    canvas.pack()
    
    canvas.create_image(210, 50, image=imgMB)
    canvas.place(x=100, y=100)
    canvas.pack()
    
    canvas.create_image(130, 50, image=imgSS109, tags = "mig")#02160125)
    canvas.place(x=100, y=100)
    canvas.pack()
    canvas.create_image(290, 50, image=imgSS115, tags = "mig")#02160125)    
    canvas.place(x=100, y=100)
    canvas.pack()
    canvas.create_image(370, 53, image=imgSS116)
    canvas.place(x=100, y=100)
    canvas.pack()
    
    for i in range(5):
        a = random.randint(1,400)
        b = random.randint(100,500)
        canvas.create_image(a, b, image=imgSS17, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
        canvas.create_image(a+200, b+200, image=imgSS18, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
        
        
        
    emojiT.pack(anchor='n',expand=1)
    
    
    # チェックされているか？
    if bln.get():
        hint = 1
    else:
        hint = 0
        
    # [結果] チェックされています
    
    # チェック2されているか？
    if bln2.get():
        zaq = 1
    else:
        zaq = 0
    
    
    zm1button.place(x=860,y=100)#s0122 0128kaijo
    
    gengo = 5
    k3once = 3
    
        
def gaming7():
    
    global zaq, chk, bln, chk2, bln2, gengo2, imgSS41, imgSS42, imgSS43, imgSS44, imgSS45, imgSS46, imgSS47, imgSS48, imgSS49, atohint5, atohint4, atohint3, atohint2, atohint1, chk, bln, hint, k3once, gengo, mojiT, mojiTn, mojiT2, mojiTg, mojiTd, emojiT, emojiTn, mojiTg, mojiTd, mojiTg, mojiTd, numM1, numM2, numM3, numM4, numM5, mojiT, play3, mouhante, mojiA, mojiB, mojiC, mojiD, mojiF, flag, stptime, sttime, ima, imgSS101, imgSS102, imgSS103, imgSS104, imgSS105, chohante, chohante2, chohante3#0128kaijoグローバル付け足し
    ima = time.time()
    stptime = 0
    sttime = 3
    play3()                      
    imgSS41 = None
    imgSS42 = tk.PhotoImage(file = 'imgSS/50万ドン_ミニ.png', master = root)
    imgSS43 = tk.PhotoImage(file = 'imgSS/10万ドン_ミニ.png', master = root)
    imgSS44 = tk.PhotoImage(file = 'imgSS/5万ドン_ミニ.png', master = root)
    imgSS45 = tk.PhotoImage(file = 'imgSS/1万ドン_ミニ.png', master = root)
    imgSS46 = tk.PhotoImage(file = 'imgSS/5千ドン_ミニ.png', master = root)
    imgSS47 = tk.PhotoImage(file = 'imgSS/千ドン_ミニ.png', master = root)
    imgSS48 = tk.PhotoImage(file = 'imgSS/5百ドン_ミニ.png', master = root)
    imgSS49 = tk.PhotoImage(file = 'imgSS/百ドン_ミニ.png', master = root)
    
    gengo2 = 3
  
    numM1 = random.randint(99,5050)
    atohint1(numM1)
    numM2 = random.randint(99,5050)
    atohint2(numM2)
    numM3 = random.randint(99,5050)
    atohint3(numM3)
    numM4 = random.randint(99,5050)
    atohint4(numM4)
    numM5 = random.randint(99,5050)
    atohint5(numM5)
    
    
    imgSS101 = None#作ってもらったはずなのに自分で再作成0128kaijo　5行　gaming4や7にも増殖
    imgSS102 = None
    imgSS103 = None
    imgSS104 = None
    imgSS105 = None
    
    
    gm1button.place_forget()
    gm2button.place_forget()
    gm3button.place_forget()
    gm4button.place_forget()
    gm5button.place_forget()
    gm6button.place_forget()
    gm7button.place_forget()
    gm8button.place_forget()
    gm9button.place_forget()
    
    stbutton.place_forget()
    mojiD.pack_forget()
    mojiA.pack_forget()
    mojiB.pack_forget()
    mojiG1.pack_forget()
    mojiG2.pack_forget()
    mojiG3.pack_forget()
    mojiG4.pack_forget()
    mojiG5.pack_forget()
    mojiG6.pack_forget()
    emojiT.pack_forget()
    emojiTn.pack_forget()
    mojiT.pack_forget()
    mojiT2.pack_forget()
    mojiTd.pack_forget()
    mojiTg.pack_forget()
    mojiTn.pack_forget()
    
    chk.place_forget()
    chk2.place_forget()
    
    rtbutton.place_forget()
    canvas.delete("all")
    
    
    numF = random.randint(1,1000)
    mojiF = tk.Label(text = "トレーに"+str(numF)+"ドン分払って")
    
    #変更150, 100, 350, 0, fill='cornflowerblue'
   
    
    #自分が追加した箇所        
    k3button.place(x=1090, y=110)#02161221
    #変更x=390, y=110
    k15button.place(x=1090, y=760)    
    
    for i in range(5):
        a = random.randint(1,400)
        b = random.randint(100,500)
        canvas.create_image(a, b, image=imgSS19, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
        canvas.create_image(a+200, b+200, image=imgSS20, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
    
    mouhante = 3
     
    # チェックされているか？
    if bln.get():
        hint = 1
    else:
        hint = 0
        
    # [結果] チェックされています
    
    # チェック2されているか？
    if bln2.get():
        zaq = 1
    else:
        zaq = 0
    
    
    zm1button.place(x=860,y=100)#s0122 0128kaijo
    
    gengo = 3
    k3once = 3
        
def gaming8():
    
    global zaq, chk, bln, chk2, bln2, gengo2, chk, bln, hint, gengo, k3once, mojiT, mojiTn, mojiT2, mojiTg, mojiTd, emojiT, emojiTn, mojiTg, mojiTd, mojiTg, mojiTd, numM1, numM2, numM3, numM4, numM5, mojiT, play3, mojiA, mojiB, mojiC, mojiD, mojiF, flag, stptime, sttime, ima, chohante, chohante2, chohante3
    ima = time.time()
    stptime = 0
    sttime = 3
    chohante3 += 1000
        
    play3()    
    gengo2 = 3
    
    numM1 = random.randint(99,5050)
    numM2 = random.randint(99,5050)
    numM3 = random.randint(99,5050)
    numM4 = random.randint(99,5050)
    numM5 = random.randint(99,5050)
    
    gm1button.place_forget()
    gm2button.place_forget()
    gm3button.place_forget()
    gm4button.place_forget()
    gm5button.place_forget()
    gm6button.place_forget()
    gm7button.place_forget()
    gm8button.place_forget()
    gm9button.place_forget()
    
    stbutton.place_forget()
    mojiD.pack_forget()
    mojiA.pack_forget()
    mojiB.pack_forget()
    mojiG1.pack_forget()
    mojiG2.pack_forget()
    mojiG3.pack_forget()
    mojiG4.pack_forget()
    mojiG5.pack_forget()
    mojiG6.pack_forget()
    emojiT.pack_forget()
    emojiTn.pack_forget()
    mojiT.pack_forget()
    mojiT2.pack_forget()
    mojiTd.pack_forget()
    mojiTg.pack_forget()
    mojiTn.pack_forget()
    
    chk.place_forget()
    chk2.place_forget()#02161226
    
    rtbutton.place_forget()
    canvas.delete("all")
    
    
    numF = random.randint(1,1000)
    mojiF = tk.Label(text = "トレーに"+str(numF)+"ドン分払って")
    
    #変更150, 100, 350, 0, fill='cornflowerblue'
   
    
    #自分が追加した箇所        
    k3button.place(x=1090, y=110)#02161221
    k15button.place(x=1090, y=760)    
    
    for i in range(5):
        a = random.randint(1,400)
        b = random.randint(100,500)
        canvas.create_image(a, b, image=imgSS19, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
        canvas.create_image(a+200, b+200, image=imgSS20, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
        
        
    hairetsu = []
    ii = random.randint(0, 5)
    iii = random.randint(0, 5)
    iv = random.randint(0, 5)
    v = random.randint(0, 5)
    vi = random.randint(0, 5)
    vii = random.randint(0, 5)
    viii = random.randint(0, 5)
    ix = random.randint(0, 5)
    xi = random.randint(0, 5)
    xii = random.randint(0, 5)
    xiii = random.randint(0, 5)
    xiv = random.randint(0, 5)
    xv = random.randint(0, 5)
    xvi = random.randint(0, 5)
    xvii = random.randint(0, 5)
    xviii = random.randint(0, 5)
    xix = random.randint(0, 5)
    xx = random.randint(0, 5)
    
    hid = [ii, iii, iv, v, vi, vii, viii, ix, xi, xii, xiii, xiv, xv, xvi, xvii, xviii, xix, xx]
    
    for l in range(18):
        hairetsu.append(hid[l])
    
    for i1 in range(hairetsu[0]):
        a1 = random.randint(1,400)
        b1 = random.randint(100,500)
        canvas.create_image(a1, b1, image=imgSS2, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()  
    for i2 in range(hairetsu[1]):
        a2 = random.randint(1,400)
        b2 = random.randint(100,500)
        canvas.create_image(a2, b2, image=imgSS3, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
    for i3 in range(hairetsu[2]):
        a3 = random.randint(1,400)
        b3 = random.randint(100,500)
        canvas.create_image(a3, b3, image=imgSS4, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()  
    for i4 in range(hairetsu[3]):
        a4 = random.randint(1,400)
        b4 = random.randint(100,500)
        canvas.create_image(a4, b4, image=imgSS5, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
    for i5 in range(hairetsu[4]):
        a5 = random.randint(1,400)
        b5 = random.randint(100,500)
        canvas.create_image(a5, b5, image=imgSS6, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()  
    for i6 in range(hairetsu[5]):
        a6 = random.randint(1,400)
        b6 = random.randint(100,500)
        canvas.create_image(a6, b6, image=imgSS7, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
    for i7 in range(hairetsu[6]):
        a7 = random.randint(1,400)
        b7 = random.randint(100,500)
        canvas.create_image(a7, b7, image=imgSS8, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()  
    for i8 in range(hairetsu[7]):
        a8 = random.randint(1,400)
        b8 = random.randint(100,500)
        canvas.create_image(a8, b8, image=imgSS9, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
    for i9 in range(hairetsu[8]):
        a9 = random.randint(1,400)
        b9 = random.randint(100,500)
        canvas.create_image(a9, b9, image=imgSS10, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()  
    
    # チェックされているか？
    if bln.get():
        hint = 1
    else:
        hint = 0
    # チェック2されているか？
    if bln2.get():
        zaq = 1
    else:
        zaq = 0
    
    gengo = 3
    k3once = 3
    
    
def gaming9():
    
    global zaq, chk, bln, chk2, bln2, gengo2, imgSS41, imgSS42, imgSS43, imgSS44, imgSS45, imgSS46, imgSS47, imgSS48, imgSS49, atohint5, atohint4, atohint3, atohint2, atohint1, gengo, emojiTn, gengo, gengo2, k3once, imgSS121, imgSS122, imgSS123, imgSS124, imgSS125, imgSS101, imgSS102, imgSS103, imgSS104, imgSS105, atohint1, atohint2, atohint3, atohint4, atohint5, imgMA, imgMB, imgMC, imgMD, imgME, imgMF, imgMG, imgMH, imgMI, imgMJ, count, ret1, ret2, ret3, ret4, ret5, challenge, imgSS50, gengo2, imgSS41, imgSS42, imgSS43, imgSS44, imgSS45, imgSS46, imgSS47, imgSS48, imgSS49, atohint5, atohint4, atohint3, atohint2, atohint1, gengo2, chk, bln, hint, gengo, k3once, mojiT, mojiTn, mojiT2, mojiTg, mojiTd, emojiT, emojiTn, mojiTg, mojiTd, mojiTg, mojiTd, numM1, numM2, numM3, numM4, numM5, mojiT, play3, mojiA, mojiB, mojiC, mojiD, mojiF, flag, stptime, sttime, ima, chohante, chohante2, chohante3
    ima = time.time()
    stptime = 0
    sttime = 3
    chohante3 += 1000    
    play3()    
    imgSS41 = None
    imgSS42 = tk.PhotoImage(file = 'imgSS/50万ドン_ミニ.png', master = root)
    imgSS43 = tk.PhotoImage(file = 'imgSS/10万ドン_ミニ.png', master = root)
    imgSS44 = tk.PhotoImage(file = 'imgSS/5万ドン_ミニ.png', master = root)
    imgSS45 = tk.PhotoImage(file = 'imgSS/1万ドン_ミニ.png', master = root)
    imgSS46 = tk.PhotoImage(file = 'imgSS/5千ドン_ミニ.png', master = root)
    imgSS47 = tk.PhotoImage(file = 'imgSS/千ドン_ミニ.png', master = root)
    imgSS48 = tk.PhotoImage(file = 'imgSS/5百ドン_ミニ.png', master = root)
    imgSS49 = tk.PhotoImage(file = 'imgSS/百ドン_ミニ.png', master = root)
    
    gengo2 = 3
  
    numM1 = 0
    imgMA = imgSS50
    imgMB = imgSS50    
    ret1 = challenge(imgMA, imgMB, numM1)
    count = 0
    for v in ret1:
        count += 1
        if count == 1:
            imgMA = v
        elif count == 2:
            imgMB = v
        else:
            numM1 = v
            
    atohint1(numM1)
        
    
    
    numM2 = 0
    imgMC = imgSS50
    imgMD = imgSS50
    ret2 = challenge(imgMC, imgMD, numM2)
    count = 0
    for vw in ret2:
        count += 1
        if count == 1:
            imgMC = vw
        elif count == 2:
            imgMD = vw
        else:
            numM2 = vw
            
    atohint2(numM2)
    
    
    numM3 = 0
    imgME = imgSS50
    imgMF = imgSS50
    ret3 = challenge(imgME, imgMF, numM3)
    
    count = 0
    for vwx in ret3:
        count += 1
        if count == 1:
            imgME = vwx
        elif count == 2:
            imgMF = vwx
        else:
            numM3 = vwx
            
    atohint3(numM3)
    
    
    numM4 = 0
    imgMG = imgSS50
    imgMH = imgSS50
    ret4 = challenge(imgMG, imgMH, numM4)
    
    count = 0
    for vwxy in ret4:
        count += 1
        if count == 1:
            imgMG = vwxy
        elif count == 2:
            imgMH = vwxy
        else:
            numM4 = vwxy
            
    atohint4(numM4)
    numM5 = 0
    imgMI = imgSS50
    imgMJ = imgSS50
    ret5 = challenge(imgMI, imgMJ, numM5)
    
    count = 0
    for vwxyz in ret5:
        count += 1
        if count == 1:
            imgMI = vwxyz
        elif count == 2:
            imgMJ = vwxyz
        else:
            numM5 = vwxyz
            
    atohint5(numM5)
    
    imgSS101 = imgMA
    imgSS102 = imgMC
    imgSS103 = imgME
    imgSS104 = imgMG
    imgSS105 = imgMI
    imgSS121 = imgMB
    imgSS122 = imgMD
    imgSS123 = imgMF
    imgSS124 = imgMH
    imgSS125 = imgMJ
    
    
    
    gm1button.place_forget()
    gm2button.place_forget()
    gm3button.place_forget()
    gm4button.place_forget()
    gm5button.place_forget()
    gm6button.place_forget()
    gm7button.place_forget()
    gm8button.place_forget()
    gm9button.place_forget()
    
    stbutton.place_forget()
    mojiD.pack_forget()
    mojiA.pack_forget()
    mojiB.pack_forget()
    mojiG1.pack_forget()
    mojiG2.pack_forget()
    mojiG3.pack_forget()
    mojiG4.pack_forget()
    mojiG5.pack_forget()
    mojiG6.pack_forget()
    emojiT.pack_forget()
    emojiTn.pack_forget()
    mojiT.pack_forget()
    mojiT2.pack_forget()
    mojiTd.pack_forget()
    mojiTg.pack_forget()
    mojiTn.pack_forget()
    
    chk.place_forget()
    chk2.place_forget()#02161226
    
    rtbutton.place_forget()
    canvas.delete("all")
    
    
    numF = random.randint(1,1000)
    mojiF = tk.Label(text = "トレーに"+str(numF)+"ドン分払って")
    
       
    k3button.place(x=1090, y=110)#0216
    #変更x=390, y=110
    k15button.place(x=1090, y=760)    
    
    for i in range(5):
        a = random.randint(1,400)
        b = random.randint(100,500)
        canvas.create_image(a, b, image=imgSS19, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
        canvas.create_image(a+200, b+200, image=imgSS20, tags = "img")
        canvas.place(x=100, y=100)
        canvas.pack()
    emojiT.pack(anchor='n',expand=1)
    
    
    # チェックされているか？
    if bln.get():
        hint = 1
    else:
        hint = 0
        
    # [結果] チェックされています
    # チェック2されているか？
    if bln2.get():
        zaq = 1
    else:
        zaq = 0
    
    zm1button.place(x=860,y=100)#s0122 0128kaijo
    
    
    gengo = 3
    
    gengo = 6
    
    k3once = 3
def ending():
    
    global onryop2, end1play, sounde1, mojiA, mojiB, mojiC, mojiD, mojiF, flag, Timer
    
    edbutton.place_forget()
    ed2button.place_forget()
    ed3button.place_forget()
    gm1button.place_forget()
    gm2button.place_forget()
    gm3button.place_forget()
    gm4button.place_forget()
    gm5button.place_forget()
    gm6button.place_forget()
    gm7button.place_forget()
    gm8button.place_forget()
    gm9button.place_forget()
    
    stbutton.place_forget()
    mojiD.pack_forget()
    mojiA.pack_forget()
    mojiB.pack_forget()
    mojiF.pack_forget()
    mojiC.pack_forget()
    canvas.delete("all")
   
    stbutton.place(x = 550, y = 550)#02161226
    
    onryop2()
    end1play()
    cap = cv2.VideoCapture('imgSS/日本へようこそ.mp4')
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # Our operations on the frame come here
        # Display the resulting frame
    
        cv2.imshow('welcome2Japan!', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    
    
def ending2():
    
    global onryop2, end2play, sounde2, mojiA, mojiB, mojiC, mojiD, mojiF, flag, Timer
    
    edbutton.place_forget()
    ed2button.place_forget()
    ed3button.place_forget()
    gm1button.place_forget()
    gm2button.place_forget()
    gm3button.place_forget()
    gm4button.place_forget()
    gm5button.place_forget()
    gm6button.place_forget()
    gm7button.place_forget()
    gm8button.place_forget()
    gm9button.place_forget()
    
    stbutton.place_forget()
    mojiD.pack_forget()
    mojiA.pack_forget()
    mojiB.pack_forget()
    mojiF.pack_forget()
    mojiC.pack_forget()
    canvas.delete("all")
    stbutton.place(x = 550, y = 550)#02161226
    
   
    onryop2()
    end2play()
    cap = cv2.VideoCapture('imgSS/中国へようこそ.mp4')
    
    
    
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # Our operations on the frame come here
        # Display the resulting frame
        cv2.imshow('welcome2China!', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    
    
def ending3():
    
    global onryop2, end3play, sounde3, mojiA, mojiB, mojiC, mojiD, mojiF, flag, Timer
    
    edbutton.place_forget()
    ed2button.place_forget()
    ed3button.place_forget()
    gm1button.place_forget()
    gm2button.place_forget()
    gm3button.place_forget()
    gm4button.place_forget()
    gm5button.place_forget()
    gm6button.place_forget()
    gm7button.place_forget()
    gm8button.place_forget()
    gm9button.place_forget()
    
    stbutton.place_forget()
    mojiD.pack_forget()
    mojiA.pack_forget()
    mojiB.pack_forget()
    mojiF.pack_forget()
    mojiC.pack_forget()
    canvas.delete("all")
    stbutton.place(x = 550, y = 550)#02161226
  
    
    onryop2()
    end3play()
    
    cap = cv2.VideoCapture('imgSS/ベトナムへようこそ.mp4')
    
    
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # Our operations on the frame come here
        # Display the resulting frame
        cv2.imshow('welcome2Vietnam!', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()    
def released():
    global img2ID, img3ID, img4ID, img5ID, img6ID, img7ID, img8ID, img9ID, img1ID, imgID, migID#blackbox0204
    
        
    for idmiru in canvas.find_all():#全オブジェクトを列挙
        tagmiru = canvas.itemcget(idmiru,'tags')#タグ名を取得
        if tagmiru.endswith('current'):
            pass
        else:
            if tagmiru.startswith('img2'):
                img2ID.append(idmiru)
            elif tagmiru.startswith('img3'):
                img3ID.append(idmiru)
            elif tagmiru.startswith('img4'):
                img4ID.append(idmiru)
            elif tagmiru.startswith('img5'):
                img5ID.append(idmiru)
            elif tagmiru.startswith('img6'):
                img6ID.append(idmiru)
            elif tagmiru.startswith('img7'):
                img7ID.append(idmiru)
            elif tagmiru.startswith('img8'):
                img8ID.append(idmiru)
            elif tagmiru.startswith('img9'):
                img9ID.append(idmiru)
            elif tagmiru.startswith('img1'):
                img1ID.append(idmiru)
            elif tagmiru.startswith('img'):
                imgID.append(idmiru)
                
            elif tagmiru.startswith('mig'):#0206追加
                migID.append(idmiru)
    
    for idmiru in canvas.find_all():#全オブジェクトを列挙
        tagmiru = canvas.itemcget(idmiru,'tags')#タグ名を取得
        
        if tagmiru.endswith('current'):
            pass
        else:
            if idmiru in img2ID:
                canvas.itemconfigure(idmiru, tags='img2')
            elif idmiru in img3ID:
                canvas.itemconfigure(idmiru, tags='img3')
            elif idmiru in img4ID:
                canvas.itemconfigure(idmiru, tags='img4')
            elif idmiru in img5ID:
                canvas.itemconfigure(idmiru, tags='img5')
            elif idmiru in img6ID:
                canvas.itemconfigure(idmiru, tags='img6')
            elif idmiru in img7ID:
                canvas.itemconfigure(idmiru, tags='img7')
            elif idmiru in img8ID:
                canvas.itemconfigure(idmiru, tags='img8')
            elif idmiru in img9ID:
                canvas.itemconfigure(idmiru, tags='img9')
            elif idmiru in img1ID:
                canvas.itemconfigure(idmiru, tags='img1')
            elif idmiru in imgID:
                canvas.itemconfigure(idmiru, tags='img')
                
            elif idmiru in migID:#0206追加
                canvas.itemconfigure(idmiru, tags='mig')
    
    
    
def clicked():
    # マウスカーソルを移動
    root.event_generate('<Motion>', warp=True, x=600, y=300)
def dropped(event):
    global pressed_x, pressed_y, item_id, img2ID, img3ID, img4ID, img5ID, img6ID, img7ID, img8ID, img9ID, img1ID, imgID, migID, clicked#blackbox0204
    item_id = canvas.find_closest(event.x, event.y)
            
    
    for idmiru in canvas.find_all():#全オブジェクトを列挙
        tagmiru = canvas.itemcget(idmiru,'tags')#タグ名を取得
        
        if tagmiru.endswith('current'):
            canvas.lift(idmiru)
        else:
            if idmiru in img2ID:
                canvas.itemconfigure(idmiru, tags='img2')
            elif idmiru in img3ID:
                canvas.itemconfigure(idmiru, tags='img3')
            elif idmiru in img4ID:
                canvas.itemconfigure(idmiru, tags='img4')
            elif idmiru in img5ID:
                canvas.itemconfigure(idmiru, tags='img5')
            elif idmiru in img6ID:
                canvas.itemconfigure(idmiru, tags='img6')
            elif idmiru in img7ID:
                canvas.itemconfigure(idmiru, tags='img7')
            elif idmiru in img8ID:
                canvas.itemconfigure(idmiru, tags='img8')
            elif idmiru in img9ID:
                canvas.itemconfigure(idmiru, tags='img9')
            elif idmiru in img1ID:
                canvas.itemconfigure(idmiru, tags='img1')
            elif idmiru in imgID:
                canvas.itemconfigure(idmiru, tags='img')
            
            elif idmiru in migID:#0206追加
                canvas.itemconfigure(idmiru, tags='mig')
    img2ID = []
    img3ID = []
    img4ID = []
    img5ID = []
    img6ID = []
    img7ID = []
    img8ID = []
    img9ID = []
    img1ID = []
    imgID = []
    
    migID = []#0206追加
    
    tag = canvas.itemcget(item_id,'tags') # タグ名を取得
    List_C1.append( canvas.coords(item_id)[0])
    List_C1.append( canvas.coords(item_id)[1])
    if ((List_C1[0] >= 500) and (List_C1[1] >= 0)):#判定 canvas.create_rectangle(500, 0, 825, 200)
        if((List_C1[0] <= 825) and (List_C1[1] <= 200)):
            clicked()
        
def pressed(event):
    global flag, pressed_x, pressed_y, item_id, hantei, play, call, mojiF, numF, tagX, tigau, img2ID, img3ID, img4ID, img5ID, img6ID, img7ID, img8ID, img9ID, img1ID, imgID, migID, chkdel#blackbox0204
    play()
    
    try:
        item_id = canvas.find_closest(event.x, event.y)
        tag = canvas.gettags(item_id[0])[0]
        item = canvas.type(tag)
        #0128kaijo
        if tag.startswith('irasutoya'):
            chkdel = 1
        tigau = 0
        for i in range(len(tagX)):
            if tag == tagX[i]:
                tigau = 1    
        pressed_x = event.x
        pressed_y = event.y
        for idmiru in canvas.find_all():#全オブジェクトを列挙
            tagmiru = canvas.itemcget(idmiru,'tags')#タグ名を取得
            if tagmiru.endswith('current'):
                canvas.lift(idmiru)
            else:
    #             canvas.lower(idmiru)#あまり変わらなかった?
                pass    
    except:
        pass
        
    
def dragged(event):
    global flag, pressed_x, pressed_y, item_id, hantei, play, call, mojiF, numF, tagX, tigau, pressed_x, pressed_y, item_id, img2ID, img3ID, img4ID, img5ID, img6ID, img7ID, img8ID, img9ID, img1ID, imgID, migID#blackbox0204
    
    try:
        item_id = canvas.find_closest(event.x, event.y)
        tag = canvas.gettags(item_id[0])[0]
        item = canvas.type(tag) # rectangle image
        delta_x = event.x - pressed_x
        delta_y = event.y - pressed_y
        if item == "rectangle":
            x0, y0, x1, y1 = canvas.coords(item_id)
            canvas.coords(item_id, x0+delta_x, y0+delta_y, x1+delta_x, y1+delta_y)
        else:
            x, y = canvas.coords(item_id)
            canvas.coords(item_id, x+delta_x, y+delta_y)
        pressed_x = event.x
        pressed_y = event.y
        for idmiru in canvas.find_all():#全オブジェクトを列挙
            tagmiru = canvas.itemcget(idmiru,'tags')#タグ名を取得
            if tagmiru.endswith('current'):
                canvas.lift(idmiru)
                
        for idmiru in canvas.find_all():#全オブジェクトを列挙
            tagmiru = canvas.itemcget(idmiru,'tags')#タグ名を取得
            if tagmiru.endswith('current'):
                canvas.lift(idmiru)
    #             blackbox = idmiru
            else:
                if tagmiru.startswith('img2'):
                    img2ID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                elif tagmiru.startswith('img3'):
                    img3ID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                elif tagmiru.startswith('img4'):
                    img4ID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                elif tagmiru.startswith('img5'):
                    img5ID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                elif tagmiru.startswith('img6'):
                    img6ID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                elif tagmiru.startswith('img7'):
                    img7ID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                elif tagmiru.startswith('img8'):
                    img8ID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                elif tagmiru.startswith('img9'):
                    img9ID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                elif tagmiru.startswith('img1'):
                    img1ID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                elif tagmiru.startswith('img'):
                    imgID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                    
                elif tagmiru.startswith('mig'):#0206追加
                    migID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                
    except:
        for idmiru in canvas.find_all():#全オブジェクトを列挙
            tagmiru = canvas.itemcget(idmiru,'tags')#タグ名を取得
            if tagmiru.endswith('current'):
                canvas.lift(idmiru)
    #             blackbox = idmiru
            else:
                if tagmiru.startswith('img2'):
                    img2ID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                elif tagmiru.startswith('img3'):
                    img3ID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                elif tagmiru.startswith('img4'):
                    img4ID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                elif tagmiru.startswith('img5'):
                    img5ID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                elif tagmiru.startswith('img6'):
                    img6ID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                elif tagmiru.startswith('img7'):
                    img7ID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                elif tagmiru.startswith('img8'):
                    img8ID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                elif tagmiru.startswith('img9'):
                    img9ID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                elif tagmiru.startswith('img1'):
                    img1ID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                elif tagmiru.startswith('img'):
                    imgID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
                    
                elif tagmiru.startswith('mig'):#0206追加
                    migID.append(idmiru)
                    canvas.itemconfigure(idmiru, tags='')
        
               
def k3():
    global k3once
    zahyo()
    k3once += 3
def k15():
    global existA, zahyo
    zahyo()
    existA = 100000
    
class App(tk.Tk):
    def __init__(self, *args, **kwargs):#呪文
        tk.Tk.__init__(self, *args, **kwargs)#呪文
        
    
canvas.tag_bind("rect", "<ButtonPress-1>", pressed)
canvas.tag_bind("img", "<ButtonPress-1>", pressed)
canvas.tag_bind("img2", "<ButtonPress-1>", pressed)
canvas.tag_bind("img3", "<ButtonPress-1>", pressed)
canvas.tag_bind("img4", "<ButtonPress-1>", pressed)
canvas.tag_bind("img5", "<ButtonPress-1>", pressed)
canvas.tag_bind("img6", "<ButtonPress-1>", pressed)
canvas.tag_bind("img7", "<ButtonPress-1>", pressed)
canvas.tag_bind("img8", "<ButtonPress-1>", pressed)
canvas.tag_bind("img9", "<ButtonPress-1>", pressed)
canvas.tag_bind("img1", "<ButtonPress-1>", pressed)#02161226 de tuketasi
canvas.tag_bind("irasutoya", "<ButtonPress-1>", pressed)#0206
canvas.tag_bind("rect", "<B1-Motion>", dragged)
canvas.tag_bind("img", "<B1-Motion>", dragged)
canvas.tag_bind("img2", "<B1-Motion>", dragged)
canvas.tag_bind("img3", "<B1-Motion>", dragged)
canvas.tag_bind("img4", "<B1-Motion>", dragged)
canvas.tag_bind("img5", "<B1-Motion>", dragged)
canvas.tag_bind("img6", "<B1-Motion>", dragged)
canvas.tag_bind("img7", "<B1-Motion>", dragged)
canvas.tag_bind("img8", "<B1-Motion>", dragged)
canvas.tag_bind("img9", "<B1-Motion>", dragged)
canvas.tag_bind("img1", "<B1-Motion>", dragged)#02161226 de tuketasi
canvas.tag_bind("irasutoya", "<B1-Motion>", dragged)#02161226 de tuketasi
canvas.tag_bind("rect", "<ButtonRelease-1>", dropped)#0204直接追加か
canvas.tag_bind("img", "<ButtonRelease-1>", dropped)
canvas.tag_bind("img2", "<ButtonRelease-1>", dropped)
canvas.tag_bind("img3", "<ButtonRelease-1>", dropped)
canvas.tag_bind("img4", "<ButtonRelease-1>", dropped)
canvas.tag_bind("img5", "<ButtonRelease-1>", dropped)
canvas.tag_bind("img6", "<ButtonRelease-1>", dropped)
canvas.tag_bind("img7", "<ButtonRelease-1>", dropped)
canvas.tag_bind("img8", "<ButtonRelease-1>", dropped)
canvas.tag_bind("img9", "<ButtonRelease-1>", dropped)
canvas.tag_bind("img1", "<ButtonRelease-1>", dropped)
canvas.tag_bind("irasutoya", "<ButtonRelease-1>", dropped)
    
def atohint1(numM):
    global gengo2, gengo, imgSS101, uketori1, uketori2, uketori3, uketori4, uketori5, imgSS41, imgSS42, imgSS43, imgSS44, imgSS45, imgSS46, imgSS47, imgSS48, imgSS49, imgSS1, imgSS2, imgSS3, imgSS4, imgSS5, imgSS6, imgSS7, imgSS8, imgSS9, imgSS10, imgSS11, gengo, play5, play4, k3once, existA, hint, tigau, tagX, zahyohn, zahyohn2, zahyohn3, zahyohn4, zahyohn5, stptime, sttime, hayaku, susumu, mojiT, mojiTn, existA, mojiA, numM1, numM2, numM3, numM4, numM5, numF, mojiF, hantei, kekka_fortune, play2, hayaku, imgSS1, imgSS2, imgSS3, imgSS4, imgSS5, imgSS6, imgSS7, imgSS8, imgSS9, imgSS10, imgSS11, gengo, mojiN, mojiT, mojiTn, canvas, ima, mojiT, mojiTn, existA, nojiA, numM1, numM2, numM3, numM4, numM5, numF, mojiF, hantei, kekka_fortune, play2, hayaku, uketori1
    
    
    a = numM/10000
    if a >= 1:
        numM1_a = numM - 10000
        kaikei1 = imgSS41
    else:
        numM1_a = numM
        kaikei1 = None
    b = numM1_a/5000
    if b >= 1:
        numM1_ab = numM1_a - 5000        
        kaikei2 = imgSS42
    else:
        numM1_ab = numM1_a
        kaikei2 = None
    c1 = numM1_ab/1000
    if c1 >= 1:
        numM1_abc1 = numM1_ab - 1000
        kaikei3 = imgSS43
    else:
        numM1_abc1 = numM1_ab        
        kaikei3 = None
    c2 = numM1_abc1/1000
    if c2 >= 1:
        numM1_abc1c2 = numM1_abc1 - 1000
        kaikei4 = imgSS43
    else:
        numM1_abc1c2 = numM1_abc1        
        kaikei4 = None
    c3 = numM1_abc1c2/1000
    if c3 >= 1:
        numM1_abc1c2c3 = numM1_abc1c2 - 1000
        kaikei5 = imgSS43
    else:
        numM1_abc1c2c3 = numM1_abc1c2        
        kaikei5 = None
    c4 = numM1_abc1c2c3/1000
    if c4 >= 1:
        numM1_abc1c2c3c4 = numM1_abc1c2c3 - 1000
        kaikei6 = imgSS43
    else:
        numM1_abc1c2c3c4 = numM1_abc1c2c3        
        kaikei6 = None
    d = numM1_abc1c2c3c4/500
    if d >= 1:
        numM1_abc1c2c3c4d = numM1_abc1c2c3c4 - 500
        kaikei7 = imgSS44
    else:
        numM1_abc1c2c3c4d = numM1_abc1c2c3c4
        kaikei7 = None
    e1 = numM1_abc1c2c3c4d/100
    if e1 >= 1:
        numM1_abc1c2c3c4de1 = numM1_abc1c2c3c4d - 100
        kaikei8 = imgSS45
    else:
        numM1_abc1c2c3c4de1 = numM1_abc1c2c3c4d        
        kaikei8 = None
    e2 = numM1_abc1c2c3c4de1/100
    if e2 >= 1:
        numM1_abc1c2c3c4de1e2 = numM1_abc1c2c3c4de1 - 100
        kaikei9 = imgSS45
    else:
        numM1_abc1c2c3c4de1e2 = numM1_abc1c2c3c4de1       
        kaikei9 = None
    e3 = numM1_abc1c2c3c4de1e2/100
    if e3 >= 1:
        numM1_abc1c2c3c4de1e2e3 = numM1_abc1c2c3c4de1e2 - 100
        kaikei10 = imgSS45
    else:
        numM1_abc1c2c3c4de1e2e3 = numM1_abc1c2c3c4de1e2       
        kaikei10 = None
    e4 = numM1_abc1c2c3c4de1e2e3/100
    if e4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4 = numM1_abc1c2c3c4de1e2e3 - 100
        kaikei11 = imgSS45
    else:
        numM1_abc1c2c3c4de1e2e3e4 = numM1_abc1c2c3c4de1e2e3        
        kaikei11 = None
    f = numM1_abc1c2c3c4de1e2e3e4/50
    if f >= 1:
        numM1_abc1c2c3c4de1e2e3e4f = numM1_abc1c2c3c4de1e2e3e4 - 50
        kaikei12 = imgSS46
    else:
        numM1_abc1c2c3c4de1e2e3e4f = numM1_abc1c2c3c4de1e2e3e4
        kaikei12 = None
    g1 = numM1_abc1c2c3c4de1e2e3e4f/10
    if g1 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1 = numM1_abc1c2c3c4de1e2e3e4f - 10
        kaikei13 = imgSS47
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1 = numM1_abc1c2c3c4de1e2e3e4f        
        kaikei13 = None
    g2 = numM1_abc1c2c3c4de1e2e3e4fg1/10
    if g2 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2 = numM1_abc1c2c3c4de1e2e3e4fg1 - 10
        kaikei14 = imgSS47
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2 = numM1_abc1c2c3c4de1e2e3e4fg1       
        kaikei14 = None
    g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2/10
    if g3 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2 - 10
        kaikei15 = imgSS47
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2        
        kaikei15 = None
    g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3/10
    if g4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3 - 10
        kaikei16 = imgSS47
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3      
        kaikei16 = None
    h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4/5
    if h >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 - 5
        kaikei17 = imgSS48
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4
        kaikei17 = None
    i1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h/1
    if i1 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h - 1
        kaikei18 = imgSS49
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h
        kaikei18 = None
    i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1/1
    if i2 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 - 1
        kaikei19 = imgSS49
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1        
        kaikei19 = None
    i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2/1
    if i3 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 - 1
        kaikei20 = imgSS49
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2        
        kaikei20 = None
    i4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3/1
    if i4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3i4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 - 1
        kaikei21 = imgSS49
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3
        kaikei21 = None               
    
    q = [kaikei1, kaikei2, kaikei3, kaikei4, kaikei5, kaikei6, kaikei7, kaikei8, kaikei9, kaikei10, kaikei11, kaikei12, kaikei13, kaikei14, kaikei15, kaikei16, kaikei17, kaikei18, kaikei19, kaikei20, kaikei21] 
    for r in range(21):
        uketori1.append(q[r])
        
        
    if gengo2 == 2:
        
        if 0 <= numM < 100:
            imgSS101 = tk.PhotoImage(file = 'imgSS/たまねぎ_gen.png', master = root)
        elif 100 <= numM < 200:
            imgSS101 = tk.PhotoImage(file = 'imgSS/トウモロコシ_gen.png', master = root)
        elif 200 <= numM < 300:
            imgSS101 = tk.PhotoImage(file = 'imgSS/ペットボトル_gen.png', master = root)
        elif 300 <= numM < 301:
            imgSS101 = tk.PhotoImage(file = 'imgSS/カップラーメン_gen.png', master = root)
        elif 301 <= numM < 350:
            imgSS101 = tk.PhotoImage(file = 'imgSS/ジャガイモ_gen.png', master = root)
        elif 350 <= numM < 400:
            imgSS101 = tk.PhotoImage(file = 'imgSS/コーラ_gen.png', master = root)
        elif 400 <= numM < 500:
            imgSS101 = tk.PhotoImage(file = 'imgSS/バナナ_gen.png', master = root)
        elif 500 <= numM < 600:
            imgSS101 = tk.PhotoImage(file = 'imgSS/ビール_gen.png', master = root)        
        elif 600 <= numM < 700:
            imgSS101 = tk.PhotoImage(file = 'imgSS/トマト_gen.png', master = root)
        elif 700 <= numM < 701:
            imgSS101 = tk.PhotoImage(file = 'imgSS/にんじん_gen.png', master = root)    
        elif 701 <= numM < 800:
            imgSS101 = tk.PhotoImage(file = 'imgSS/牛乳_gen.png', master = root)    
        elif 800 <= numM < 801:
            imgSS101 = tk.PhotoImage(file = 'imgSS/タバコ_gen.png', master = root)    
        elif 801 <= numM < 1200:
            imgSS101 = tk.PhotoImage(file = 'imgSS/レモン_gen.png', master = root)    
        elif 1200 <= numM < 1500:
            imgSS101 = tk.PhotoImage(file = 'imgSS/パン_gen.png', master = root)
        elif 1500 <= numM < 2000:
            imgSS101 = tk.PhotoImage(file = 'imgSS/チョコ_gen.png', master = root)
        elif 2000 <= numM < 3600:
            imgSS101 = tk.PhotoImage(file = 'imgSS/ハンバーガー_gen.png', master = root)
        elif 3600 <= numM < 4900:
            imgSS101 = tk.PhotoImage(file = 'imgSS/メロン_gen.png', master = root)    
        elif 4900 <= numM < 7000:
            imgSS101 = tk.PhotoImage(file = 'imgSS/傘_gen.png', master = root)        
        elif 7000 <= numM < 7001:
            imgSS101 = tk.PhotoImage(file = 'imgSS/フライパン_gen.png', master = root)         
        elif 7001 <= numM < 10000:#25000でドライヤーがあったが・・・
            imgSS101 = tk.PhotoImage(file = 'imgSS/包丁_gen.png', master = root)       
        else:
            imgSS101 = tk.PhotoImage(file = 'imgSS/syohinken.png', master = root)
        
    elif gengo2 == 3:
        
        
        if 0 <= numM < 34:
            imgSS101 = tk.PhotoImage(file = 'imgSS/にんじん_don.png', master = root)
        elif 34 <= numM < 77:
            imgSS101 = tk.PhotoImage(file = 'imgSS/ペットボトル_don.png', master = root)
        elif 77 <= numM < 90:
            imgSS101 = tk.PhotoImage(file = 'imgSS/トマト_don.png', master = root)
        elif 90 <= numM < 100:
            imgSS101 = tk.PhotoImage(file = 'imgSS/コーラ_don.png', master = root)
        elif 100 <= numM < 101:
            imgSS101 = tk.PhotoImage(file = 'imgSS/メロン_don.png', master = root)
        elif 101 <= numM < 119:
            imgSS101 = tk.PhotoImage(file = 'imgSS/パン_don.png', master = root)
        elif 119 <= numM < 120:
            imgSS101 = tk.PhotoImage(file = 'imgSS/カップラーメン_don.png', master = root)
        elif 120 <= numM < 121:
            imgSS101 = tk.PhotoImage(file = 'imgSS/バナナ_don.png', master = root)        
        elif 121 <= numM < 122:
            imgSS101 = tk.PhotoImage(file = 'imgSS/ジャガイモ_don.png', master = root)
        elif 122 <= numM < 129:
            imgSS101 = tk.PhotoImage(file = 'imgSS/タバコ_don.png', master = root)    
        elif 129 <= numM < 150:
            imgSS101 = tk.PhotoImage(file = 'imgSS/たまねぎ_don.png', master = root)    
        elif 150 <= numM < 151:
            imgSS101 = tk.PhotoImage(file = 'imgSS/ビール_don.png', master = root)    
        elif 151 <= numM < 155:
            imgSS101 = tk.PhotoImage(file = 'imgSS/レモン_don.png', master = root)    
        elif 155 <= numM < 200:
            imgSS101 = tk.PhotoImage(file = 'imgSS/トウモロコシ_don.png', master = root)
        elif 200 <= numM < 250:
            imgSS101 = tk.PhotoImage(file = 'imgSS/フライパン_don.png', master = root)
        elif 250 <= numM < 300:
            imgSS101 = tk.PhotoImage(file = 'imgSS/ハンバーガー_don.png', master = root)
        elif 300 <= numM < 301:
            imgSS101 = tk.PhotoImage(file = 'imgSS/牛乳_don.png', master = root)    
        elif 301 <= numM < 390:
            imgSS101 = tk.PhotoImage(file = 'imgSS/包丁_don.png', master = root)        
        elif 390 <= numM < 600:
            imgSS101 = tk.PhotoImage(file = 'imgSS/チョコ_don.png', master = root)         
        elif 600 <= numM < 1250:
            imgSS101 = tk.PhotoImage(file = 'imgSS/傘_don.png', master = root)       
        elif 1250 <= numM < 6999:
            imgSS101 = tk.PhotoImage(file = 'imgSS/ドライヤー_don.png', master = root)       
        else:
            imgSS101 = tk.PhotoImage(file = 'imgSS/syohinken.png', master = root)
    else:
        
            
        if 0 <= numM < 53:
            imgSS101 = tk.PhotoImage(file = 'imgSS/たまねぎ_yen.png', master = root)
        elif 53 <= numM < 72:
            imgSS101 = tk.PhotoImage(file = 'imgSS/ジャガイモ_yen.png', master = root)
        elif 72 <= numM < 88:
            imgSS101 = tk.PhotoImage(file = 'imgSS/にんじん_yen.png', master = root)
        elif 88 <= numM < 107:
            imgSS101 = tk.PhotoImage(file = 'imgSS/ペットボトル_yen.png', master = root)
        elif 107 <= numM < 108:
            imgSS101 = tk.PhotoImage(file = 'imgSS/レモン_yen.png', master = root)
        elif 108 <= numM < 120:
            imgSS101 = tk.PhotoImage(file = 'imgSS/トマト_yen.png', master = root)
        elif 120 <= numM < 125:
            imgSS101 = tk.PhotoImage(file = 'imgSS/コーラ_yen.png', master = root)
        elif 125 <= numM < 138:
            imgSS101 = tk.PhotoImage(file = 'imgSS/チョコ_yen.png', master = root)
        elif 138 <= numM < 154:
            imgSS101 = tk.PhotoImage(file = 'imgSS/カップラーメン_yen.png', master = root)        
        elif 154 <= numM < 156:
            imgSS101 = tk.PhotoImage(file = 'imgSS/トウモロコシ_yen.png', master = root)
        elif 156 <= numM < 160:
            imgSS101 = tk.PhotoImage(file = 'imgSS/パン_yen.png', master = root)    
        elif 160 <= numM < 178:
            imgSS101 = tk.PhotoImage(file = 'imgSS/ハンバーガー_yen.png', master = root)    
        elif 178 <= numM < 198:
            imgSS101 = tk.PhotoImage(file = 'imgSS/牛乳_yen.png', master = root)    
        elif 198 <= numM < 450:
            imgSS101 = tk.PhotoImage(file = 'imgSS/バナナ_yen.png', master = root)    
        elif 450 <= numM < 480:
            imgSS101 = tk.PhotoImage(file = 'imgSS/タバコ_yen.png', master = root)
        elif 480 <= numM < 1226:
            imgSS101 = tk.PhotoImage(file = 'imgSS/ビール_yen.png', master = root)
        elif 1226 <= numM < 1542:
            imgSS101 = tk.PhotoImage(file = 'imgSS/フライパン_yen.png', master = root)
        elif 1542 <= numM < 2800:
            imgSS101 = tk.PhotoImage(file = 'imgSS/傘_yen.png', master = root)    
        elif 2800 <= numM < 3800:
            imgSS101 = tk.PhotoImage(file = 'imgSS/包丁_yen.png', master = root)        
        elif 3800 <= numM < 7603:
            imgSS101 = tk.PhotoImage(file = 'imgSS/メロン_yen.png', master = root)         
        elif 7603 <= numM < 10980:
            imgSS101 = tk.PhotoImage(file = 'imgSS/ドライヤー_yen.png', master = root)       
        else:
            imgSS101 = tk.PhotoImage(file = 'imgSS/syohinken.png', master = root)
        
def atohint2(numM):
    global gengo2, imgSS102, uketori1, uketori2, uketori3, uketori4, uketori5, imgSS41, imgSS42, imgSS43, imgSS44, imgSS45, imgSS46, imgSS47, imgSS48, imgSS49, imgSS1, imgSS2, imgSS3, imgSS4, imgSS5, imgSS6, imgSS7, imgSS8, imgSS9, imgSS10, imgSS11, gengo, play5, play4, k3once, existA, hint, tigau, tagX, zahyohn, zahyohn2, zahyohn3, zahyohn4, zahyohn5, stptime, sttime, hayaku, susumu, mojiT, mojiTn, existA, mojiA, numM1, numM2, numM3, numM4, numM5, numF, mojiF, hantei, kekka_fortune, play2, hayaku, imgSS1, imgSS2, imgSS3, imgSS4, imgSS5, imgSS6, imgSS7, imgSS8, imgSS9, imgSS10, imgSS11, gengo, mojiN, mojiT, mojiTn, canvas, ima, mojiT, mojiTn, existA, nojiA, numM1, numM2, numM3, numM4, numM5, numF, mojiF, hantei, kekka_fortune, play2, hayaku, uketori2
    
    
    a = numM/10000
    if a >= 1:
        numM1_a = numM - 10000
        kaikei1 = imgSS41
    else:
        numM1_a = numM
        kaikei1 = None
    b = numM1_a/5000
    if b >= 1:
        numM1_ab = numM1_a - 5000        
        kaikei2 = imgSS42
    else:
        numM1_ab = numM1_a
        kaikei2 = None
    c1 = numM1_ab/1000
    if c1 >= 1:
        numM1_abc1 = numM1_ab - 1000
        kaikei3 = imgSS43
    else:
        numM1_abc1 = numM1_ab        
        kaikei3 = None
    c2 = numM1_abc1/1000
    if c2 >= 1:
        numM1_abc1c2 = numM1_abc1 - 1000
        kaikei4 = imgSS43
    else:
        numM1_abc1c2 = numM1_abc1        
        kaikei4 = None
    c3 = numM1_abc1c2/1000
    if c3 >= 1:
        numM1_abc1c2c3 = numM1_abc1c2 - 1000
        kaikei5 = imgSS43
    else:
        numM1_abc1c2c3 = numM1_abc1c2        
        kaikei5 = None
    c4 = numM1_abc1c2c3/1000
    if c4 >= 1:
        numM1_abc1c2c3c4 = numM1_abc1c2c3 - 1000
        kaikei6 = imgSS43
    else:
        numM1_abc1c2c3c4 = numM1_abc1c2c3        
        kaikei6 = None
    d = numM1_abc1c2c3c4/500
    if d >= 1:
        numM1_abc1c2c3c4d = numM1_abc1c2c3c4 - 500
        kaikei7 = imgSS44
    else:
        numM1_abc1c2c3c4d = numM1_abc1c2c3c4
        kaikei7 = None
    e1 = numM1_abc1c2c3c4d/100
    if e1 >= 1:
        numM1_abc1c2c3c4de1 = numM1_abc1c2c3c4d - 100
        kaikei8 = imgSS45
    else:
        numM1_abc1c2c3c4de1 = numM1_abc1c2c3c4d        
        kaikei8 = None
    e2 = numM1_abc1c2c3c4de1/100
    if e2 >= 1:
        numM1_abc1c2c3c4de1e2 = numM1_abc1c2c3c4de1 - 100
        kaikei9 = imgSS45
    else:
        numM1_abc1c2c3c4de1e2 = numM1_abc1c2c3c4de1       
        kaikei9 = None
    e3 = numM1_abc1c2c3c4de1e2/100
    if e3 >= 1:
        numM1_abc1c2c3c4de1e2e3 = numM1_abc1c2c3c4de1e2 - 100
        kaikei10 = imgSS45
    else:
        numM1_abc1c2c3c4de1e2e3 = numM1_abc1c2c3c4de1e2       
        kaikei10 = None
    e4 = numM1_abc1c2c3c4de1e2e3/100
    if e4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4 = numM1_abc1c2c3c4de1e2e3 - 100
        kaikei11 = imgSS45
    else:
        numM1_abc1c2c3c4de1e2e3e4 = numM1_abc1c2c3c4de1e2e3        
        kaikei11 = None
    f = numM1_abc1c2c3c4de1e2e3e4/50
    if f >= 1:
        numM1_abc1c2c3c4de1e2e3e4f = numM1_abc1c2c3c4de1e2e3e4 - 50
        kaikei12 = imgSS46
    else:
        numM1_abc1c2c3c4de1e2e3e4f = numM1_abc1c2c3c4de1e2e3e4
        kaikei12 = None
    g1 = numM1_abc1c2c3c4de1e2e3e4f/10
    if g1 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1 = numM1_abc1c2c3c4de1e2e3e4f - 10
        kaikei13 = imgSS47
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1 = numM1_abc1c2c3c4de1e2e3e4f        
        kaikei13 = None
    g2 = numM1_abc1c2c3c4de1e2e3e4fg1/10
    if g2 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2 = numM1_abc1c2c3c4de1e2e3e4fg1 - 10
        kaikei14 = imgSS47
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2 = numM1_abc1c2c3c4de1e2e3e4fg1       
        kaikei14 = None
    g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2/10
    if g3 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2 - 10
        kaikei15 = imgSS47
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2        
        kaikei15 = None
    g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3/10
    if g4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3 - 10
        kaikei16 = imgSS47
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3      
        kaikei16 = None
    h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4/5
    if h >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 - 5
        kaikei17 = imgSS48
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4
        kaikei17 = None
    i1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h/1
    if i1 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h - 1
        kaikei18 = imgSS49
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h
        kaikei18 = None
    i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1/1
    if i2 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 - 1
        kaikei19 = imgSS49
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1        
        kaikei19 = None
    i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2/1
    if i3 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 - 1
        kaikei20 = imgSS49
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2        
        kaikei20 = None
    i4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3/1
    if i4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3i4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 - 1
        kaikei21 = imgSS49
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3
        kaikei21 = None               
    
    q = [kaikei1, kaikei2, kaikei3, kaikei4, kaikei5, kaikei6, kaikei7, kaikei8, kaikei9, kaikei10, kaikei11, kaikei12, kaikei13, kaikei14, kaikei15, kaikei16, kaikei17, kaikei18, kaikei19, kaikei20, kaikei21] 
    for r in range(21):
        uketori2.append(q[r])
        
        
    if gengo2 == 2:
        
        if 0 <= numM < 100:
            imgSS102 = tk.PhotoImage(file = 'imgSS/たまねぎ_gen.png', master = root)
        elif 100 <= numM < 200:
            imgSS102 = tk.PhotoImage(file = 'imgSS/トウモロコシ_gen.png', master = root)
        elif 200 <= numM < 300:
            imgSS102 = tk.PhotoImage(file = 'imgSS/ペットボトル_gen.png', master = root)
        elif 300 <= numM < 301:
            imgSS102 = tk.PhotoImage(file = 'imgSS/カップラーメン_gen.png', master = root)
        elif 301 <= numM < 350:
            imgSS102 = tk.PhotoImage(file = 'imgSS/ジャガイモ_gen.png', master = root)
        elif 350 <= numM < 400:
            imgSS102 = tk.PhotoImage(file = 'imgSS/コーラ_gen.png', master = root)
        elif 400 <= numM < 500:
            imgSS102 = tk.PhotoImage(file = 'imgSS/バナナ_gen.png', master = root)
        elif 500 <= numM < 600:
            imgSS102 = tk.PhotoImage(file = 'imgSS/ビール_gen.png', master = root)        
        elif 600 <= numM < 700:
            imgSS102 = tk.PhotoImage(file = 'imgSS/トマト_gen.png', master = root)
        elif 700 <= numM < 701:
            imgSS102 = tk.PhotoImage(file = 'imgSS/にんじん_gen.png', master = root)    
        elif 701 <= numM < 800:
            imgSS102 = tk.PhotoImage(file = 'imgSS/牛乳_gen.png', master = root)    
        elif 800 <= numM < 801:
            imgSS102 = tk.PhotoImage(file = 'imgSS/タバコ_gen.png', master = root)    
        elif 801 <= numM < 1200:
            imgSS102 = tk.PhotoImage(file = 'imgSS/レモン_gen.png', master = root)    
        elif 1200 <= numM < 1500:
            imgSS102 = tk.PhotoImage(file = 'imgSS/パン_gen.png', master = root)
        elif 1500 <= numM < 2000:
            imgSS102 = tk.PhotoImage(file = 'imgSS/チョコ_gen.png', master = root)
        elif 2000 <= numM < 3600:
            imgSS102 = tk.PhotoImage(file = 'imgSS/ハンバーガー_gen.png', master = root)
        elif 3600 <= numM < 4900:
            imgSS102 = tk.PhotoImage(file = 'imgSS/メロン_gen.png', master = root)    
        elif 4900 <= numM < 7000:
            imgSS102 = tk.PhotoImage(file = 'imgSS/傘_gen.png', master = root)        
        elif 7000 <= numM < 7001:
            imgSS102 = tk.PhotoImage(file = 'imgSS/フライパン_gen.png', master = root)         
        elif 7001 <= numM < 10000:#25000でドライヤーがあったが・・・
            imgSS102 = tk.PhotoImage(file = 'imgSS/包丁_gen.png', master = root)       
        else:
            imgSS102 = tk.PhotoImage(file = 'imgSS/syohinken.png', master = root)
    elif gengo2 == 3:#02161226
   
        if 0 <= numM < 34:
            imgSS102 = tk.PhotoImage(file = 'imgSS/にんじん_don.png', master = root)
        elif 34 <= numM < 77:
            imgSS102 = tk.PhotoImage(file = 'imgSS/ペットボトル_don.png', master = root)
        elif 77 <= numM < 90:
            imgSS102 = tk.PhotoImage(file = 'imgSS/トマト_don.png', master = root)
        elif 90 <= numM < 100:
            imgSS102 = tk.PhotoImage(file = 'imgSS/コーラ_don.png', master = root)
        elif 100 <= numM < 101:
            imgSS102 = tk.PhotoImage(file = 'imgSS/メロン_don.png', master = root)
        elif 101 <= numM < 119:
            imgSS102 = tk.PhotoImage(file = 'imgSS/パン_don.png', master = root)
        elif 119 <= numM < 120:
            imgSS102 = tk.PhotoImage(file = 'imgSS/カップラーメン_don.png', master = root)
        elif 120 <= numM < 121:
            imgSS102 = tk.PhotoImage(file = 'imgSS/バナナ_don.png', master = root)        
        elif 121 <= numM < 122:
            imgSS102 = tk.PhotoImage(file = 'imgSS/ジャガイモ_don.png', master = root)
        elif 122 <= numM < 129:
            imgSS102 = tk.PhotoImage(file = 'imgSS/タバコ_don.png', master = root)    
        elif 129 <= numM < 150:
            imgSS102 = tk.PhotoImage(file = 'imgSS/たまねぎ_don.png', master = root)    
        elif 150 <= numM < 151:
            imgSS102 = tk.PhotoImage(file = 'imgSS/ビール_don.png', master = root)    
        elif 151 <= numM < 155:
            imgSS102 = tk.PhotoImage(file = 'imgSS/レモン_don.png', master = root)    
        elif 155 <= numM < 200:
            imgSS102 = tk.PhotoImage(file = 'imgSS/トウモロコシ_don.png', master = root)
        elif 200 <= numM < 250:
            imgSS102 = tk.PhotoImage(file = 'imgSS/フライパン_don.png', master = root)
        elif 250 <= numM < 300:
            imgSS102 = tk.PhotoImage(file = 'imgSS/ハンバーガー_don.png', master = root)
        elif 300 <= numM < 301:
            imgSS102 = tk.PhotoImage(file = 'imgSS/牛乳_don.png', master = root)    
        elif 301 <= numM < 390:
            imgSS102 = tk.PhotoImage(file = 'imgSS/包丁_don.png', master = root)        
        elif 390 <= numM < 600:
            imgSS102 = tk.PhotoImage(file = 'imgSS/チョコ_don.png', master = root)         
        elif 600 <= numM < 1250:
            imgSS102 = tk.PhotoImage(file = 'imgSS/傘_don.png', master = root)       
        elif 1250 <= numM < 6999:
            imgSS102 = tk.PhotoImage(file = 'imgSS/ドライヤー_don.png', master = root)       
        else:
            imgSS102 = tk.PhotoImage(file = 'imgSS/syohinken.png', master = root)
    else:
        
        if 0 <= numM < 53:
            imgSS102 = tk.PhotoImage(file = 'imgSS/たまねぎ_yen.png', master = root)
        elif 53 <= numM < 72:
            imgSS102 = tk.PhotoImage(file = 'imgSS/ジャガイモ_yen.png', master = root)
        elif 72 <= numM < 107:
            imgSS102 = tk.PhotoImage(file = 'imgSS/にんじん_yen.png', master = root)
        elif 107 <= numM < 108:
            imgSS102 = tk.PhotoImage(file = 'imgSS/レモン_yen.png', master = root)
        elif 108 <= numM < 120:
            imgSS102 = tk.PhotoImage(file = 'imgSS/トマト_yen.png', master = root)
        elif 120 <= numM < 125:
            imgSS102 = tk.PhotoImage(file = 'imgSS/コーラ_yen.png', master = root)
        elif 125 <= numM < 138:
            imgSS102 = tk.PhotoImage(file = 'imgSS/チョコ_yen.png', master = root)
        elif 138 <= numM < 154:
            imgSS102 = tk.PhotoImage(file = 'imgSS/カップラーメン_yen.png', master = root)        
        elif 154 <= numM < 156:
            imgSS102 = tk.PhotoImage(file = 'imgSS/トウモロコシ_yen.png', master = root)
        elif 156 <= numM < 160:
            imgSS102 = tk.PhotoImage(file = 'imgSS/パン_yen.png', master = root)    
        elif 160 <= numM < 178:
            imgSS102 = tk.PhotoImage(file = 'imgSS/ハンバーガー_yen.png', master = root)    
        elif 178 <= numM < 198:
            imgSS102 = tk.PhotoImage(file = 'imgSS/牛乳_yen.png', master = root)    
        elif 198 <= numM < 450:
            imgSS102 = tk.PhotoImage(file = 'imgSS/バナナ_yen.png', master = root)    
        elif 450 <= numM < 480:
            imgSS102 = tk.PhotoImage(file = 'imgSS/タバコ_yen.png', master = root)
        elif 480 <= numM < 1226:
            imgSS102 = tk.PhotoImage(file = 'imgSS/ビール_yen.png', master = root)
        elif 1226 <= numM < 1542:
            imgSS102 = tk.PhotoImage(file = 'imgSS/フライパン_yen.png', master = root)
        elif 1542 <= numM < 2800:
            imgSS102 = tk.PhotoImage(file = 'imgSS/傘_yen.png', master = root)    
        elif 2800 <= numM < 3800:
            imgSS102 = tk.PhotoImage(file = 'imgSS/包丁_yen.png', master = root)        
        elif 3800 <= numM < 7603:
            imgSS102 = tk.PhotoImage(file = 'imgSS/メロン_yen.png', master = root)         
        elif 7603 <= numM < 10980:
            imgSS102 = tk.PhotoImage(file = 'imgSS/ドライヤー_yen.png', master = root)       
        else:
            imgSS102 = tk.PhotoImage(file = 'imgSS/syohinken.png', master = root)
def atohint3(numM):
    global gengo2, imgSS103, uketori1, uketori2, uketori3, uketori4, uketori5, imgSS41, imgSS42, imgSS43, imgSS44, imgSS45, imgSS46, imgSS47, imgSS48, imgSS49, imgSS1, imgSS2, imgSS3, imgSS4, imgSS5, imgSS6, imgSS7, imgSS8, imgSS9, imgSS10, imgSS11, gengo, play5, play4, k3once, existA, hint, tigau, tagX, zahyohn, zahyohn2, zahyohn3, zahyohn4, zahyohn5, stptime, sttime, hayaku, susumu, mojiT, mojiTn, existA, mojiA, numM1, numM2, numM3, numM4, numM5, numF, mojiF, hantei, kekka_fortune, play2, hayaku, imgSS1, imgSS2, imgSS3, imgSS4, imgSS5, imgSS6, imgSS7, imgSS8, imgSS9, imgSS10, imgSS11, gengo, mojiN, mojiT, mojiTn, canvas, ima, mojiT, mojiTn, existA, nojiA, numM1, numM2, numM3, numM4, numM5, numF, mojiF, hantei, kekka_fortune, play2, hayaku, uketori3
    
    
    a = numM/10000
    if a >= 1:
        numM1_a = numM - 10000
        kaikei1 = imgSS41
    else:
        numM1_a = numM
        kaikei1 = None
    b = numM1_a/5000
    if b >= 1:
        numM1_ab = numM1_a - 5000        
        kaikei2 = imgSS42
    else:
        numM1_ab = numM1_a
        kaikei2 = None
    c1 = numM1_ab/1000
    if c1 >= 1:
        numM1_abc1 = numM1_ab - 1000
        kaikei3 = imgSS43
    else:
        numM1_abc1 = numM1_ab        
        kaikei3 = None
    c2 = numM1_abc1/1000
    if c2 >= 1:
        numM1_abc1c2 = numM1_abc1 - 1000
        kaikei4 = imgSS43
    else:
        numM1_abc1c2 = numM1_abc1        
        kaikei4 = None
    c3 = numM1_abc1c2/1000
    if c3 >= 1:
        numM1_abc1c2c3 = numM1_abc1c2 - 1000
        kaikei5 = imgSS43
    else:
        numM1_abc1c2c3 = numM1_abc1c2        
        kaikei5 = None
    c4 = numM1_abc1c2c3/1000
    if c4 >= 1:
        numM1_abc1c2c3c4 = numM1_abc1c2c3 - 1000
        kaikei6 = imgSS43
    else:
        numM1_abc1c2c3c4 = numM1_abc1c2c3        
        kaikei6 = None
    d = numM1_abc1c2c3c4/500
    if d >= 1:
        numM1_abc1c2c3c4d = numM1_abc1c2c3c4 - 500
        kaikei7 = imgSS44
    else:
        numM1_abc1c2c3c4d = numM1_abc1c2c3c4
        kaikei7 = None
    e1 = numM1_abc1c2c3c4d/100
    if e1 >= 1:
        numM1_abc1c2c3c4de1 = numM1_abc1c2c3c4d - 100
        kaikei8 = imgSS45
    else:
        numM1_abc1c2c3c4de1 = numM1_abc1c2c3c4d        
        kaikei8 = None
    e2 = numM1_abc1c2c3c4de1/100
    if e2 >= 1:
        numM1_abc1c2c3c4de1e2 = numM1_abc1c2c3c4de1 - 100
        kaikei9 = imgSS45
    else:
        numM1_abc1c2c3c4de1e2 = numM1_abc1c2c3c4de1       
        kaikei9 = None
    e3 = numM1_abc1c2c3c4de1e2/100
    if e3 >= 1:
        numM1_abc1c2c3c4de1e2e3 = numM1_abc1c2c3c4de1e2 - 100
        kaikei10 = imgSS45
    else:
        numM1_abc1c2c3c4de1e2e3 = numM1_abc1c2c3c4de1e2       
        kaikei10 = None
    e4 = numM1_abc1c2c3c4de1e2e3/100
    if e4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4 = numM1_abc1c2c3c4de1e2e3 - 100
        kaikei11 = imgSS45
    else:
        numM1_abc1c2c3c4de1e2e3e4 = numM1_abc1c2c3c4de1e2e3        
        kaikei11 = None
    f = numM1_abc1c2c3c4de1e2e3e4/50
    if f >= 1:
        numM1_abc1c2c3c4de1e2e3e4f = numM1_abc1c2c3c4de1e2e3e4 - 50
        kaikei12 = imgSS46
    else:
        numM1_abc1c2c3c4de1e2e3e4f = numM1_abc1c2c3c4de1e2e3e4
        kaikei12 = None
    g1 = numM1_abc1c2c3c4de1e2e3e4f/10
    if g1 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1 = numM1_abc1c2c3c4de1e2e3e4f - 10
        kaikei13 = imgSS47
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1 = numM1_abc1c2c3c4de1e2e3e4f        
        kaikei13 = None
    g2 = numM1_abc1c2c3c4de1e2e3e4fg1/10
    if g2 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2 = numM1_abc1c2c3c4de1e2e3e4fg1 - 10
        kaikei14 = imgSS47
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2 = numM1_abc1c2c3c4de1e2e3e4fg1       
        kaikei14 = None
    g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2/10
    if g3 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2 - 10
        kaikei15 = imgSS47
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2        
        kaikei15 = None
    g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3/10
    if g4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3 - 10
        kaikei16 = imgSS47
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3      
        kaikei16 = None
    h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4/5
    if h >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 - 5
        kaikei17 = imgSS48
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4
        kaikei17 = None
    i1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h/1
    if i1 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h - 1
        kaikei18 = imgSS49
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h
        kaikei18 = None
    i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1/1
    if i2 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 - 1
        kaikei19 = imgSS49
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1        
        kaikei19 = None
    i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2/1
    if i3 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 - 1
        kaikei20 = imgSS49
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2        
        kaikei20 = None
    i4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3/1
    if i4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3i4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 - 1
        kaikei21 = imgSS49
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3
        kaikei21 = None               
    
    q = [kaikei1, kaikei2, kaikei3, kaikei4, kaikei5, kaikei6, kaikei7, kaikei8, kaikei9, kaikei10, kaikei11, kaikei12, kaikei13, kaikei14, kaikei15, kaikei16, kaikei17, kaikei18, kaikei19, kaikei20, kaikei21] 
    for r in range(21):
        uketori3.append(q[r])
        
        
        
    if gengo2 == 2:
        
        if 0 <= numM < 100:
            imgSS103 = tk.PhotoImage(file = 'imgSS/たまねぎ_gen.png', master = root)
        elif 100 <= numM < 200:
            imgSS103 = tk.PhotoImage(file = 'imgSS/トウモロコシ_gen.png', master = root)
        elif 200 <= numM < 300:
            imgSS103 = tk.PhotoImage(file = 'imgSS/ペットボトル_gen.png', master = root)
        elif 300 <= numM < 301:
            imgSS103 = tk.PhotoImage(file = 'imgSS/カップラーメン_gen.png', master = root)
        elif 301 <= numM < 350:
            imgSS103 = tk.PhotoImage(file = 'imgSS/ジャガイモ_gen.png', master = root)
        elif 350 <= numM < 400:
            imgSS103 = tk.PhotoImage(file = 'imgSS/コーラ_gen.png', master = root)
        elif 400 <= numM < 500:
            imgSS103 = tk.PhotoImage(file = 'imgSS/バナナ_gen.png', master = root)
        elif 500 <= numM < 600:
            imgSS103 = tk.PhotoImage(file = 'imgSS/ビール_gen.png', master = root)        
        elif 600 <= numM < 700:
            imgSS103 = tk.PhotoImage(file = 'imgSS/トマト_gen.png', master = root)
        elif 700 <= numM < 701:
            imgSS103 = tk.PhotoImage(file = 'imgSS/にんじん_gen.png', master = root)    
        elif 701 <= numM < 800:
            imgSS103 = tk.PhotoImage(file = 'imgSS/牛乳_gen.png', master = root)    
        elif 800 <= numM < 801:
            imgSS103 = tk.PhotoImage(file = 'imgSS/タバコ_gen.png', master = root)    
        elif 801 <= numM < 1200:
            imgSS103 = tk.PhotoImage(file = 'imgSS/レモン_gen.png', master = root)    
        elif 1200 <= numM < 1500:
            imgSS103 = tk.PhotoImage(file = 'imgSS/パン_gen.png', master = root)
        elif 1500 <= numM < 2000:
            imgSS103 = tk.PhotoImage(file = 'imgSS/チョコ_gen.png', master = root)
        elif 2000 <= numM < 3600:
            imgSS103 = tk.PhotoImage(file = 'imgSS/ハンバーガー_gen.png', master = root)
        elif 3600 <= numM < 4900:
            imgSS103 = tk.PhotoImage(file = 'imgSS/メロン_gen.png', master = root)    
        elif 4900 <= numM < 7000:
            imgSS103 = tk.PhotoImage(file = 'imgSS/傘_gen.png', master = root)        
        elif 7000 <= numM < 7001:
            imgSS103 = tk.PhotoImage(file = 'imgSS/フライパン_gen.png', master = root)         
        elif 7001 <= numM < 10000:#25000でドライヤーがあったが・・・
            imgSS103 = tk.PhotoImage(file = 'imgSS/包丁_gen.png', master = root)       
        else:
            imgSS103 = tk.PhotoImage(file = 'imgSS/syohinken.png', master = root)
        
    elif gengo2 == 3:
        
        if 0 <= numM < 34:
            imgSS103 = tk.PhotoImage(file = 'imgSS/にんじん_don.png', master = root)
        elif 34 <= numM < 77:
            imgSS103 = tk.PhotoImage(file = 'imgSS/ペットボトル_don.png', master = root)
        elif 77 <= numM < 90:
            imgSS103 = tk.PhotoImage(file = 'imgSS/トマト_don.png', master = root)
        elif 90 <= numM < 100:
            imgSS103 = tk.PhotoImage(file = 'imgSS/コーラ_don.png', master = root)
        elif 100 <= numM < 101:
            imgSS103 = tk.PhotoImage(file = 'imgSS/メロン_don.png', master = root)
        elif 101 <= numM < 119:
            imgSS103 = tk.PhotoImage(file = 'imgSS/パン_don.png', master = root)
        elif 119 <= numM < 120:
            imgSS103 = tk.PhotoImage(file = 'imgSS/カップラーメン_don.png', master = root)
        elif 120 <= numM < 121:
            imgSS103 = tk.PhotoImage(file = 'imgSS/バナナ_don.png', master = root)        
        elif 121 <= numM < 122:
            imgSS103 = tk.PhotoImage(file = 'imgSS/ジャガイモ_don.png', master = root)
        elif 122 <= numM < 129:
            imgSS103 = tk.PhotoImage(file = 'imgSS/タバコ_don.png', master = root)    
        elif 129 <= numM < 150:
            imgSS103 = tk.PhotoImage(file = 'imgSS/たまねぎ_don.png', master = root)    
        elif 150 <= numM < 151:
            imgSS103 = tk.PhotoImage(file = 'imgSS/ビール_don.png', master = root)    
        elif 151 <= numM < 155:
            imgSS103 = tk.PhotoImage(file = 'imgSS/レモン_don.png', master = root)    
        elif 155 <= numM < 200:
            imgSS103 = tk.PhotoImage(file = 'imgSS/トウモロコシ_don.png', master = root)
        elif 200 <= numM < 250:
            imgSS103 = tk.PhotoImage(file = 'imgSS/フライパン_don.png', master = root)
        elif 250 <= numM < 300:
            imgSS103 = tk.PhotoImage(file = 'imgSS/ハンバーガー_don.png', master = root)
        elif 300 <= numM < 301:
            imgSS103 = tk.PhotoImage(file = 'imgSS/牛乳_don.png', master = root)    
        elif 301 <= numM < 390:
            imgSS103 = tk.PhotoImage(file = 'imgSS/包丁_don.png', master = root)        
        elif 390 <= numM < 600:
            imgSS103 = tk.PhotoImage(file = 'imgSS/チョコ_don.png', master = root)         
        elif 600 <= numM < 1250:
            imgSS103 = tk.PhotoImage(file = 'imgSS/傘_don.png', master = root)       
        elif 1250 <= numM < 6999:
            imgSS103 = tk.PhotoImage(file = 'imgSS/ドライヤー_don.png', master = root)       
        else:
            imgSS103 = tk.PhotoImage(file = 'imgSS/syohinken.png', master = root)
    else:
        
        if 0 <= numM < 53:
            imgSS103 = tk.PhotoImage(file = 'imgSS/たまねぎ_yen.png', master = root)
        elif 53 <= numM < 72:
            imgSS103 = tk.PhotoImage(file = 'imgSS/ジャガイモ_yen.png', master = root)
        elif 72 <= numM < 107:
            imgSS103 = tk.PhotoImage(file = 'imgSS/にんじん_yen.png', master = root)
        elif 107 <= numM < 108:
            imgSS103 = tk.PhotoImage(file = 'imgSS/レモン_yen.png', master = root)
        elif 108 <= numM < 120:
            imgSS103 = tk.PhotoImage(file = 'imgSS/トマト_yen.png', master = root)
        elif 120 <= numM < 125:
            imgSS103 = tk.PhotoImage(file = 'imgSS/コーラ_yen.png', master = root)
        elif 125 <= numM < 138:
            imgSS103 = tk.PhotoImage(file = 'imgSS/チョコ_yen.png', master = root)
        elif 138 <= numM < 154:
            imgSS103 = tk.PhotoImage(file = 'imgSS/カップラーメン_yen.png', master = root)        
        elif 154 <= numM < 156:
            imgSS103 = tk.PhotoImage(file = 'imgSS/トウモロコシ_yen.png', master = root)
        elif 156 <= numM < 160:
            imgSS103 = tk.PhotoImage(file = 'imgSS/パン_yen.png', master = root)    
        elif 160 <= numM < 178:
            imgSS103 = tk.PhotoImage(file = 'imgSS/ハンバーガー_yen.png', master = root)    
        elif 178 <= numM < 198:
            imgSS103 = tk.PhotoImage(file = 'imgSS/牛乳_yen.png', master = root)    
        elif 198 <= numM < 450:
            imgSS103 = tk.PhotoImage(file = 'imgSS/バナナ_yen.png', master = root)    
        elif 450 <= numM < 480:
            imgSS103 = tk.PhotoImage(file = 'imgSS/タバコ_yen.png', master = root)
        elif 480 <= numM < 1226:
            imgSS103 = tk.PhotoImage(file = 'imgSS/ビール_yen.png', master = root)
        elif 1226 <= numM < 1542:
            imgSS103 = tk.PhotoImage(file = 'imgSS/フライパン_yen.png', master = root)
        elif 1542 <= numM < 2800:
            imgSS103 = tk.PhotoImage(file = 'imgSS/傘_yen.png', master = root)    
        elif 2800 <= numM < 3800:
            imgSS103 = tk.PhotoImage(file = 'imgSS/包丁_yen.png', master = root)        
        elif 3800 <= numM < 7603:
            imgSS103 = tk.PhotoImage(file = 'imgSS/メロン_yen.png', master = root)         
        elif 7603 <= numM < 10980:
            imgSS103 = tk.PhotoImage(file = 'imgSS/ドライヤー_yen.png', master = root)       
        else:
            imgSS103 = tk.PhotoImage(file = 'imgSS/syohinken.png', master = root)
def atohint4(numM):
    global gengo2, imgSS104, uketori1, uketori2, uketori3, uketori4, uketori5, imgSS41, imgSS42, imgSS43, imgSS44, imgSS45, imgSS46, imgSS47, imgSS48, imgSS49, imgSS1, imgSS2, imgSS3, imgSS4, imgSS5, imgSS6, imgSS7, imgSS8, imgSS9, imgSS10, imgSS11, gengo, play5, play4, k3once, existA, hint, tigau, tagX, zahyohn, zahyohn2, zahyohn3, zahyohn4, zahyohn5, stptime, sttime, hayaku, susumu, mojiT, mojiTn, existA, mojiA, numM1, numM2, numM3, numM4, numM5, numF, mojiF, hantei, kekka_fortune, play2, hayaku, imgSS1, imgSS2, imgSS3, imgSS4, imgSS5, imgSS6, imgSS7, imgSS8, imgSS9, imgSS10, imgSS11, gengo, mojiN, mojiT, mojiTn, canvas, ima, mojiT, mojiTn, existA, nojiA, numM1, numM2, numM3, numM4, numM5, numF, mojiF, hantei, kekka_fortune, play2, hayaku, uketori4
    
    
    a = numM/10000
    if a >= 1:
        numM1_a = numM - 10000
        kaikei1 = imgSS41
    else:
        numM1_a = numM
        kaikei1 = None
    b = numM1_a/5000
    if b >= 1:
        numM1_ab = numM1_a - 5000        
        kaikei2 = imgSS42
    else:
        numM1_ab = numM1_a
        kaikei2 = None
    c1 = numM1_ab/1000
    if c1 >= 1:
        numM1_abc1 = numM1_ab - 1000
        kaikei3 = imgSS43
    else:
        numM1_abc1 = numM1_ab        
        kaikei3 = None
    c2 = numM1_abc1/1000
    if c2 >= 1:
        numM1_abc1c2 = numM1_abc1 - 1000
        kaikei4 = imgSS43
    else:
        numM1_abc1c2 = numM1_abc1        
        kaikei4 = None
    c3 = numM1_abc1c2/1000
    if c3 >= 1:
        numM1_abc1c2c3 = numM1_abc1c2 - 1000
        kaikei5 = imgSS43
    else:
        numM1_abc1c2c3 = numM1_abc1c2        
        kaikei5 = None
    c4 = numM1_abc1c2c3/1000
    if c4 >= 1:
        numM1_abc1c2c3c4 = numM1_abc1c2c3 - 1000
        kaikei6 = imgSS43
    else:
        numM1_abc1c2c3c4 = numM1_abc1c2c3        
        kaikei6 = None
    d = numM1_abc1c2c3c4/500
    if d >= 1:
        numM1_abc1c2c3c4d = numM1_abc1c2c3c4 - 500
        kaikei7 = imgSS44
    else:
        numM1_abc1c2c3c4d = numM1_abc1c2c3c4
        kaikei7 = None
    e1 = numM1_abc1c2c3c4d/100
    if e1 >= 1:
        numM1_abc1c2c3c4de1 = numM1_abc1c2c3c4d - 100
        kaikei8 = imgSS45
    else:
        numM1_abc1c2c3c4de1 = numM1_abc1c2c3c4d        
        kaikei8 = None
    e2 = numM1_abc1c2c3c4de1/100
    if e2 >= 1:
        numM1_abc1c2c3c4de1e2 = numM1_abc1c2c3c4de1 - 100
        kaikei9 = imgSS45
    else:
        numM1_abc1c2c3c4de1e2 = numM1_abc1c2c3c4de1       
        kaikei9 = None
    e3 = numM1_abc1c2c3c4de1e2/100
    if e3 >= 1:
        numM1_abc1c2c3c4de1e2e3 = numM1_abc1c2c3c4de1e2 - 100
        kaikei10 = imgSS45
    else:
        numM1_abc1c2c3c4de1e2e3 = numM1_abc1c2c3c4de1e2       
        kaikei10 = None
    e4 = numM1_abc1c2c3c4de1e2e3/100
    if e4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4 = numM1_abc1c2c3c4de1e2e3 - 100
        kaikei11 = imgSS45
    else:
        numM1_abc1c2c3c4de1e2e3e4 = numM1_abc1c2c3c4de1e2e3        
        kaikei11 = None
    f = numM1_abc1c2c3c4de1e2e3e4/50
    if f >= 1:
        numM1_abc1c2c3c4de1e2e3e4f = numM1_abc1c2c3c4de1e2e3e4 - 50
        kaikei12 = imgSS46
    else:
        numM1_abc1c2c3c4de1e2e3e4f = numM1_abc1c2c3c4de1e2e3e4
        kaikei12 = None
    g1 = numM1_abc1c2c3c4de1e2e3e4f/10
    if g1 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1 = numM1_abc1c2c3c4de1e2e3e4f - 10
        kaikei13 = imgSS47
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1 = numM1_abc1c2c3c4de1e2e3e4f        
        kaikei13 = None
    g2 = numM1_abc1c2c3c4de1e2e3e4fg1/10
    if g2 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2 = numM1_abc1c2c3c4de1e2e3e4fg1 - 10
        kaikei14 = imgSS47
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2 = numM1_abc1c2c3c4de1e2e3e4fg1       
        kaikei14 = None
    g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2/10
    if g3 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2 - 10
        kaikei15 = imgSS47
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2        
        kaikei15 = None
    g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3/10
    if g4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3 - 10
        kaikei16 = imgSS47
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3      
        kaikei16 = None
    h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4/5
    if h >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 - 5
        kaikei17 = imgSS48
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4
        kaikei17 = None
    i1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h/1
    if i1 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h - 1
        kaikei18 = imgSS49
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h
        kaikei18 = None
    i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1/1
    if i2 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 - 1
        kaikei19 = imgSS49
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1        
        kaikei19 = None
    i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2/1
    if i3 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 - 1
        kaikei20 = imgSS49
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2        
        kaikei20 = None
    i4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3/1
    if i4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3i4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 - 1
        kaikei21 = imgSS49
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3
        kaikei21 = None               
    
    q = [kaikei1, kaikei2, kaikei3, kaikei4, kaikei5, kaikei6, kaikei7, kaikei8, kaikei9, kaikei10, kaikei11, kaikei12, kaikei13, kaikei14, kaikei15, kaikei16, kaikei17, kaikei18, kaikei19, kaikei20, kaikei21] 
    for r in range(21):
        uketori4.append(q[r])
        
    
    if gengo2 == 2:
        
        if 0 <= numM < 100:
            imgSS104 = tk.PhotoImage(file = 'imgSS/たまねぎ_gen.png', master = root)
        elif 100 <= numM < 200:
            imgSS104 = tk.PhotoImage(file = 'imgSS/トウモロコシ_gen.png', master = root)
        elif 200 <= numM < 300:
            imgSS104 = tk.PhotoImage(file = 'imgSS/ペットボトル_gen.png', master = root)
        elif 300 <= numM < 301:
            imgSS104 = tk.PhotoImage(file = 'imgSS/カップラーメン_gen.png', master = root)
        elif 301 <= numM < 350:
            imgSS104 = tk.PhotoImage(file = 'imgSS/ジャガイモ_gen.png', master = root)
        elif 350 <= numM < 400:
            imgSS104 = tk.PhotoImage(file = 'imgSS/コーラ_gen.png', master = root)
        elif 400 <= numM < 500:
            imgSS104 = tk.PhotoImage(file = 'imgSS/バナナ_gen.png', master = root)
        elif 500 <= numM < 600:
            imgSS104 = tk.PhotoImage(file = 'imgSS/ビール_gen.png', master = root)        
        elif 600 <= numM < 700:
            imgSS104 = tk.PhotoImage(file = 'imgSS/トマト_gen.png', master = root)
        elif 700 <= numM < 701:
            imgSS104 = tk.PhotoImage(file = 'imgSS/にんじん_gen.png', master = root)    
        elif 701 <= numM < 800:
            imgSS104 = tk.PhotoImage(file = 'imgSS/牛乳_gen.png', master = root)    
        elif 800 <= numM < 801:
            imgSS104 = tk.PhotoImage(file = 'imgSS/タバコ_gen.png', master = root)    
        elif 801 <= numM < 1200:
            imgSS104 = tk.PhotoImage(file = 'imgSS/レモン_gen.png', master = root)    
        elif 1200 <= numM < 1500:
            imgSS104 = tk.PhotoImage(file = 'imgSS/パン_gen.png', master = root)
        elif 1500 <= numM < 2000:
            imgSS104 = tk.PhotoImage(file = 'imgSS/チョコ_gen.png', master = root)
        elif 2000 <= numM < 3600:
            imgSS104 = tk.PhotoImage(file = 'imgSS/ハンバーガー_gen.png', master = root)
        elif 3600 <= numM < 4900:
            imgSS104 = tk.PhotoImage(file = 'imgSS/メロン_gen.png', master = root)    
        elif 4900 <= numM < 7000:
            imgSS104 = tk.PhotoImage(file = 'imgSS/傘_gen.png', master = root)        
        elif 7000 <= numM < 7001:
            imgSS104 = tk.PhotoImage(file = 'imgSS/フライパン_gen.png', master = root)         
        elif 7001 <= numM < 10000:#25000でドライヤーがあったが・・・
            imgSS104 = tk.PhotoImage(file = 'imgSS/包丁_gen.png', master = root)       
        else:
            imgSS104 = tk.PhotoImage(file = 'imgSS/syohinken.png', master = root)
    elif gengo2 == 3:
        
        if 0 <= numM < 34:
            imgSS104 = tk.PhotoImage(file = 'imgSS/にんじん_don.png', master = root)
        elif 34 <= numM < 77:
            imgSS104 = tk.PhotoImage(file = 'imgSS/ペットボトル_don.png', master = root)
        elif 77 <= numM < 90:
            imgSS104 = tk.PhotoImage(file = 'imgSS/トマト_don.png', master = root)
        elif 90 <= numM < 100:
            imgSS104 = tk.PhotoImage(file = 'imgSS/コーラ_don.png', master = root)
        elif 100 <= numM < 101:
            imgSS104 = tk.PhotoImage(file = 'imgSS/メロン_don.png', master = root)
        elif 101 <= numM < 119:
            imgSS104 = tk.PhotoImage(file = 'imgSS/パン_don.png', master = root)
        elif 119 <= numM < 120:
            imgSS104 = tk.PhotoImage(file = 'imgSS/カップラーメン_don.png', master = root)
        elif 120 <= numM < 121:
            imgSS104 = tk.PhotoImage(file = 'imgSS/バナナ_don.png', master = root)        
        elif 121 <= numM < 122:
            imgSS104 = tk.PhotoImage(file = 'imgSS/ジャガイモ_don.png', master = root)
        elif 122 <= numM < 129:
            imgSS104 = tk.PhotoImage(file = 'imgSS/タバコ_don.png', master = root)    
        elif 129 <= numM < 150:
            imgSS104 = tk.PhotoImage(file = 'imgSS/たまねぎ_don.png', master = root)    
        elif 150 <= numM < 151:
            imgSS104 = tk.PhotoImage(file = 'imgSS/ビール_don.png', master = root)    
        elif 151 <= numM < 155:
            imgSS104 = tk.PhotoImage(file = 'imgSS/レモン_don.png', master = root)    
        elif 155 <= numM < 200:
            imgSS104 = tk.PhotoImage(file = 'imgSS/トウモロコシ_don.png', master = root)
        elif 200 <= numM < 250:
            imgSS104 = tk.PhotoImage(file = 'imgSS/フライパン_don.png', master = root)
        elif 250 <= numM < 300:
            imgSS104 = tk.PhotoImage(file = 'imgSS/ハンバーガー_don.png', master = root)
        elif 300 <= numM < 301:
            imgSS104 = tk.PhotoImage(file = 'imgSS/牛乳_don.png', master = root)    
        elif 301 <= numM < 390:
            imgSS104 = tk.PhotoImage(file = 'imgSS/包丁_don.png', master = root)        
        elif 390 <= numM < 600:
            imgSS104 = tk.PhotoImage(file = 'imgSS/チョコ_don.png', master = root)         
        elif 600 <= numM < 1250:
            imgSS104 = tk.PhotoImage(file = 'imgSS/傘_don.png', master = root)       
        elif 1250 <= numM < 6999:
            imgSS104 = tk.PhotoImage(file = 'imgSS/ドライヤー_don.png', master = root)       
        else:
            imgSS104 = tk.PhotoImage(file = 'imgSS/syohinken.png', master = root)
    else:
        
        if 0 <= numM < 53:
            imgSS104 = tk.PhotoImage(file = 'imgSS/たまねぎ_yen.png', master = root)
        elif 53 <= numM < 72:
            imgSS104 = tk.PhotoImage(file = 'imgSS/ジャガイモ_yen.png', master = root)
        elif 72 <= numM < 107:
            imgSS104 = tk.PhotoImage(file = 'imgSS/にんじん_yen.png', master = root)
        elif 107 <= numM < 108:
            imgSS104 = tk.PhotoImage(file = 'imgSS/レモン_yen.png', master = root)
        elif 108 <= numM < 120:
            imgSS104 = tk.PhotoImage(file = 'imgSS/トマト_yen.png', master = root)
        elif 120 <= numM < 125:
            imgSS104 = tk.PhotoImage(file = 'imgSS/コーラ_yen.png', master = root)
        elif 125 <= numM < 138:
            imgSS104 = tk.PhotoImage(file = 'imgSS/チョコ_yen.png', master = root)
        elif 138 <= numM < 154:
            imgSS104 = tk.PhotoImage(file = 'imgSS/カップラーメン_yen.png', master = root)        
        elif 154 <= numM < 156:
            imgSS104 = tk.PhotoImage(file = 'imgSS/トウモロコシ_yen.png', master = root)
        elif 156 <= numM < 160:
            imgSS104 = tk.PhotoImage(file = 'imgSS/パン_yen.png', master = root)    
        elif 160 <= numM < 178:
            imgSS104 = tk.PhotoImage(file = 'imgSS/ハンバーガー_yen.png', master = root)    
        elif 178 <= numM < 198:
            imgSS104 = tk.PhotoImage(file = 'imgSS/牛乳_yen.png', master = root)    
        elif 198 <= numM < 450:
            imgSS104 = tk.PhotoImage(file = 'imgSS/バナナ_yen.png', master = root)    
        elif 450 <= numM < 480:
            imgSS104 = tk.PhotoImage(file = 'imgSS/タバコ_yen.png', master = root)
        elif 480 <= numM < 1226:
            imgSS104 = tk.PhotoImage(file = 'imgSS/ビール_yen.png', master = root)
        elif 1226 <= numM < 1542:
            imgSS104 = tk.PhotoImage(file = 'imgSS/フライパン_yen.png', master = root)
        elif 1542 <= numM < 2800:
            imgSS104 = tk.PhotoImage(file = 'imgSS/傘_yen.png', master = root)    
        elif 2800 <= numM < 3800:
            imgSS104 = tk.PhotoImage(file = 'imgSS/包丁_yen.png', master = root)        
        elif 3800 <= numM < 7603:
            imgSS104 = tk.PhotoImage(file = 'imgSS/メロン_yen.png', master = root)         
        elif 7603 <= numM < 10980:
            imgSS104 = tk.PhotoImage(file = 'imgSS/ドライヤー_yen.png', master = root)       
        else:
            imgSS104 = tk.PhotoImage(file = 'imgSS/syohinken.png', master = root)
def atohint5(numM):
    global gengo2, imgSS105, uketori1, uketori2, uketori3, uketori4, uketori5, imgSS41, imgSS42, imgSS43, imgSS44, imgSS45, imgSS46, imgSS47, imgSS48, imgSS49, imgSS1, imgSS2, imgSS3, imgSS4, imgSS5, imgSS6, imgSS7, imgSS8, imgSS9, imgSS10, imgSS11, gengo, play5, play4, k3once, existA, hint, tigau, tagX, zahyohn, zahyohn2, zahyohn3, zahyohn4, zahyohn5, stptime, sttime, hayaku, susumu, mojiT, mojiTn, existA, mojiA, numM1, numM2, numM3, numM4, numM5, numF, mojiF, hantei, kekka_fortune, play2, hayaku, imgSS1, imgSS2, imgSS3, imgSS4, imgSS5, imgSS6, imgSS7, imgSS8, imgSS9, imgSS10, imgSS11, gengo, mojiN, mojiT, mojiTn, canvas, ima, mojiT, mojiTn, existA, nojiA, numM1, numM2, numM3, numM4, numM5, numF, mojiF, hantei, kekka_fortune, play2, hayaku, uketori5
    
    
    a = numM/10000
    if a >= 1:
        numM1_a = numM - 10000
        kaikei1 = imgSS41
    else:
        numM1_a = numM
        kaikei1 = None
    b = numM1_a/5000
    if b >= 1:
        numM1_ab = numM1_a - 5000        
        kaikei2 = imgSS42
    else:
        numM1_ab = numM1_a
        kaikei2 = None
    c1 = numM1_ab/1000
    if c1 >= 1:
        numM1_abc1 = numM1_ab - 1000
        kaikei3 = imgSS43
    else:
        numM1_abc1 = numM1_ab        
        kaikei3 = None
    c2 = numM1_abc1/1000
    if c2 >= 1:
        numM1_abc1c2 = numM1_abc1 - 1000
        kaikei4 = imgSS43
    else:
        numM1_abc1c2 = numM1_abc1        
        kaikei4 = None
    c3 = numM1_abc1c2/1000
    if c3 >= 1:
        numM1_abc1c2c3 = numM1_abc1c2 - 1000
        kaikei5 = imgSS43
    else:
        numM1_abc1c2c3 = numM1_abc1c2        
        kaikei5 = None
    c4 = numM1_abc1c2c3/1000
    if c4 >= 1:
        numM1_abc1c2c3c4 = numM1_abc1c2c3 - 1000
        kaikei6 = imgSS43
    else:
        numM1_abc1c2c3c4 = numM1_abc1c2c3        
        kaikei6 = None
    d = numM1_abc1c2c3c4/500
    if d >= 1:
        numM1_abc1c2c3c4d = numM1_abc1c2c3c4 - 500
        kaikei7 = imgSS44
    else:
        numM1_abc1c2c3c4d = numM1_abc1c2c3c4
        kaikei7 = None
    e1 = numM1_abc1c2c3c4d/100
    if e1 >= 1:
        numM1_abc1c2c3c4de1 = numM1_abc1c2c3c4d - 100
        kaikei8 = imgSS45
    else:
        numM1_abc1c2c3c4de1 = numM1_abc1c2c3c4d        
        kaikei8 = None
    e2 = numM1_abc1c2c3c4de1/100
    if e2 >= 1:
        numM1_abc1c2c3c4de1e2 = numM1_abc1c2c3c4de1 - 100
        kaikei9 = imgSS45
    else:
        numM1_abc1c2c3c4de1e2 = numM1_abc1c2c3c4de1       
        kaikei9 = None
    e3 = numM1_abc1c2c3c4de1e2/100
    if e3 >= 1:
        numM1_abc1c2c3c4de1e2e3 = numM1_abc1c2c3c4de1e2 - 100
        kaikei10 = imgSS45
    else:
        numM1_abc1c2c3c4de1e2e3 = numM1_abc1c2c3c4de1e2       
        kaikei10 = None
    e4 = numM1_abc1c2c3c4de1e2e3/100
    if e4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4 = numM1_abc1c2c3c4de1e2e3 - 100
        kaikei11 = imgSS45
    else:
        numM1_abc1c2c3c4de1e2e3e4 = numM1_abc1c2c3c4de1e2e3        
        kaikei11 = None
    f = numM1_abc1c2c3c4de1e2e3e4/50
    if f >= 1:
        numM1_abc1c2c3c4de1e2e3e4f = numM1_abc1c2c3c4de1e2e3e4 - 50
        kaikei12 = imgSS46
    else:
        numM1_abc1c2c3c4de1e2e3e4f = numM1_abc1c2c3c4de1e2e3e4
        kaikei12 = None
    g1 = numM1_abc1c2c3c4de1e2e3e4f/10
    if g1 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1 = numM1_abc1c2c3c4de1e2e3e4f - 10
        kaikei13 = imgSS47
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1 = numM1_abc1c2c3c4de1e2e3e4f        
        kaikei13 = None
    g2 = numM1_abc1c2c3c4de1e2e3e4fg1/10
    if g2 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2 = numM1_abc1c2c3c4de1e2e3e4fg1 - 10
        kaikei14 = imgSS47
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2 = numM1_abc1c2c3c4de1e2e3e4fg1       
        kaikei14 = None
    g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2/10
    if g3 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2 - 10
        kaikei15 = imgSS47
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2        
        kaikei15 = None
    g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3/10
    if g4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3 - 10
        kaikei16 = imgSS47
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3      
        kaikei16 = None
    h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4/5
    if h >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 - 5
        kaikei17 = imgSS48
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4
        kaikei17 = None
    i1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h/1
    if i1 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h - 1
        kaikei18 = imgSS49
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h
        kaikei18 = None
    i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1/1
    if i2 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 - 1
        kaikei19 = imgSS49
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1        
        kaikei19 = None
    i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2/1
    if i3 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 - 1
        kaikei20 = imgSS49
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2        
        kaikei20 = None
    i4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3/1
    if i4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3i4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 - 1
        kaikei21 = imgSS49
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3
        kaikei21 = None               
    
    q = [kaikei1, kaikei2, kaikei3, kaikei4, kaikei5, kaikei6, kaikei7, kaikei8, kaikei9, kaikei10, kaikei11, kaikei12, kaikei13, kaikei14, kaikei15, kaikei16, kaikei17, kaikei18, kaikei19, kaikei20, kaikei21] 
    for r in range(21):
        uketori5.append(q[r])
        
    
    if gengo2 == 2:
        
        if 0 <= numM < 100:
            imgSS105 = tk.PhotoImage(file = 'imgSS/たまねぎ_gen.png', master = root)
        elif 100 <= numM < 200:
            imgSS105 = tk.PhotoImage(file = 'imgSS/トウモロコシ_gen.png', master = root)
        elif 200 <= numM < 300:
            imgSS105 = tk.PhotoImage(file = 'imgSS/ペットボトル_gen.png', master = root)
        elif 300 <= numM < 301:
            imgSS105 = tk.PhotoImage(file = 'imgSS/カップラーメン_gen.png', master = root)
        elif 301 <= numM < 350:
            imgSS105 = tk.PhotoImage(file = 'imgSS/ジャガイモ_gen.png', master = root)
        elif 350 <= numM < 400:
            imgSS105 = tk.PhotoImage(file = 'imgSS/コーラ_gen.png', master = root)
        elif 400 <= numM < 500:
            imgSS105 = tk.PhotoImage(file = 'imgSS/バナナ_gen.png', master = root)
        elif 500 <= numM < 600:
            imgSS105 = tk.PhotoImage(file = 'imgSS/ビール_gen.png', master = root)        
        elif 600 <= numM < 700:
            imgSS105 = tk.PhotoImage(file = 'imgSS/トマト_gen.png', master = root)
        elif 700 <= numM < 701:
            imgSS105 = tk.PhotoImage(file = 'imgSS/にんじん_gen.png', master = root)    
        elif 701 <= numM < 800:
            imgSS105 = tk.PhotoImage(file = 'imgSS/牛乳_gen.png', master = root)    
        elif 800 <= numM < 801:
            imgSS105 = tk.PhotoImage(file = 'imgSS/タバコ_gen.png', master = root)    
        elif 801 <= numM < 1200:
            imgSS105 = tk.PhotoImage(file = 'imgSS/レモン_gen.png', master = root)    
        elif 1200 <= numM < 1500:
            imgSS105 = tk.PhotoImage(file = 'imgSS/パン_gen.png', master = root)
        elif 1500 <= numM < 2000:
            imgSS105 = tk.PhotoImage(file = 'imgSS/チョコ_gen.png', master = root)
        elif 2000 <= numM < 3600:
            imgSS105 = tk.PhotoImage(file = 'imgSS/ハンバーガー_gen.png', master = root)
        elif 3600 <= numM < 4900:
            imgSS105 = tk.PhotoImage(file = 'imgSS/メロン_gen.png', master = root)    
        elif 4900 <= numM < 7000:
            imgSS105 = tk.PhotoImage(file = 'imgSS/傘_gen.png', master = root)        
        elif 7000 <= numM < 7001:
            imgSS105 = tk.PhotoImage(file = 'imgSS/フライパン_gen.png', master = root)         
        elif 7001 <= numM < 10000:#25000でドライヤーがあったが・・・
            imgSS105 = tk.PhotoImage(file = 'imgSS/包丁_gen.png', master = root)       
        else:
            imgSS105 = tk.PhotoImage(file = 'imgSS/syohinken.png', master = root)
        
    elif gengo2 == 3:
        
        if 0 <= numM < 34:
            imgSS105 = tk.PhotoImage(file = 'imgSS/にんじん_don.png', master = root)
        elif 34 <= numM < 77:
            imgSS105 = tk.PhotoImage(file = 'imgSS/ペットボトル_don.png', master = root)
        elif 77 <= numM < 90:
            imgSS105 = tk.PhotoImage(file = 'imgSS/トマト_don.png', master = root)
        elif 90 <= numM < 100:
            imgSS105 = tk.PhotoImage(file = 'imgSS/コーラ_don.png', master = root)
        elif 100 <= numM < 101:
            imgSS105 = tk.PhotoImage(file = 'imgSS/メロン_don.png', master = root)
        elif 101 <= numM < 119:
            imgSS105 = tk.PhotoImage(file = 'imgSS/パン_don.png', master = root)
        elif 119 <= numM < 120:
            imgSS105 = tk.PhotoImage(file = 'imgSS/カップラーメン_don.png', master = root)
        elif 120 <= numM < 121:
            imgSS105 = tk.PhotoImage(file = 'imgSS/バナナ_don.png', master = root)        
        elif 121 <= numM < 122:
            imgSS105 = tk.PhotoImage(file = 'imgSS/ジャガイモ_don.png', master = root)
        elif 122 <= numM < 129:
            imgSS105 = tk.PhotoImage(file = 'imgSS/タバコ_don.png', master = root)    
        elif 129 <= numM < 150:
            imgSS105 = tk.PhotoImage(file = 'imgSS/たまねぎ_don.png', master = root)    
        elif 150 <= numM < 151:
            imgSS105 = tk.PhotoImage(file = 'imgSS/ビール_don.png', master = root)    
        elif 151 <= numM < 155:
            imgSS105 = tk.PhotoImage(file = 'imgSS/レモン_don.png', master = root)    
        elif 155 <= numM < 200:
            imgSS105 = tk.PhotoImage(file = 'imgSS/トウモロコシ_don.png', master = root)
        elif 200 <= numM < 250:
            imgSS105 = tk.PhotoImage(file = 'imgSS/フライパン_don.png', master = root)
        elif 250 <= numM < 300:
            imgSS105 = tk.PhotoImage(file = 'imgSS/ハンバーガー_don.png', master = root)
        elif 300 <= numM < 301:
            imgSS105 = tk.PhotoImage(file = 'imgSS/牛乳_don.png', master = root)    
        elif 301 <= numM < 390:
            imgSS105 = tk.PhotoImage(file = 'imgSS/包丁_don.png', master = root)        
        elif 390 <= numM < 600:
            imgSS105 = tk.PhotoImage(file = 'imgSS/チョコ_don.png', master = root)         
        elif 600 <= numM < 1250:
            imgSS105 = tk.PhotoImage(file = 'imgSS/傘_don.png', master = root)       
        elif 1250 <= numM < 6999:
            imgSS105 = tk.PhotoImage(file = 'imgSS/ドライヤー_don.png', master = root)       
        else:
            imgSS105 = tk.PhotoImage(file = 'imgSS/syohinken.png', master = root)
    else:
        
        if 0 <= numM < 53:
            imgSS105 = tk.PhotoImage(file = 'imgSS/たまねぎ_yen.png', master = root)
        elif 53 <= numM < 72:
            imgSS105 = tk.PhotoImage(file = 'imgSS/ジャガイモ_yen.png', master = root)
        elif 72 <= numM < 107:
            imgSS105 = tk.PhotoImage(file = 'imgSS/にんじん_yen.png', master = root)
        elif 107 <= numM < 108:
            imgSS105 = tk.PhotoImage(file = 'imgSS/レモン_yen.png', master = root)
        elif 108 <= numM < 120:
            imgSS105 = tk.PhotoImage(file = 'imgSS/トマト_yen.png', master = root)
        elif 120 <= numM < 125:
            imgSS105 = tk.PhotoImage(file = 'imgSS/コーラ_yen.png', master = root)
        elif 125 <= numM < 138:
            imgSS105 = tk.PhotoImage(file = 'imgSS/チョコ_yen.png', master = root)
        elif 138 <= numM < 154:
            imgSS105 = tk.PhotoImage(file = 'imgSS/カップラーメン_yen.png', master = root)        
        elif 154 <= numM < 156:
            imgSS105 = tk.PhotoImage(file = 'imgSS/トウモロコシ_yen.png', master = root)
        elif 156 <= numM < 160:
            imgSS105 = tk.PhotoImage(file = 'imgSS/パン_yen.png', master = root)    
        elif 160 <= numM < 178:
            imgSS105 = tk.PhotoImage(file = 'imgSS/ハンバーガー_yen.png', master = root)    
        elif 178 <= numM < 198:
            imgSS105 = tk.PhotoImage(file = 'imgSS/牛乳_yen.png', master = root)    
        elif 198 <= numM < 450:
            imgSS105 = tk.PhotoImage(file = 'imgSS/バナナ_yen.png', master = root)    
        elif 450 <= numM < 480:
            imgSS105 = tk.PhotoImage(file = 'imgSS/タバコ_yen.png', master = root)
        elif 480 <= numM < 1226:
            imgSS105 = tk.PhotoImage(file = 'imgSS/ビール_yen.png', master = root)
        elif 1226 <= numM < 1542:
            imgSS105 = tk.PhotoImage(file = 'imgSS/フライパン_yen.png', master = root)
        elif 1542 <= numM < 2800:
            imgSS105 = tk.PhotoImage(file = 'imgSS/傘_yen.png', master = root)    
        elif 2800 <= numM < 3800:
            imgSS105 = tk.PhotoImage(file = 'imgSS/包丁_yen.png', master = root)        
        elif 3800 <= numM < 7603:
            imgSS105 = tk.PhotoImage(file = 'imgSS/メロン_yen.png', master = root)         
        elif 7603 <= numM < 10980:
            imgSS105 = tk.PhotoImage(file = 'imgSS/ドライヤー_yen.png', master = root)       
        else:
            imgSS105 = tk.PhotoImage(file = 'imgSS/syohinken.png', master = root)
    
        
def ahint(numM):#0125でだいぶタグ付けたどうなるか    
    global imgSS1, imgSS2, imgSS3, imgSS4, imgSS5, imgSS6, imgSS7, imgSS8, imgSS9, imgSS10, imgSS11, gengo, play5, play4, k3once, existA, hint, tigau, tagX, zahyohn, zahyohn2, zahyohn3, zahyohn4, zahyohn5, stptime, sttime, hayaku, susumu, mojiT, mojiTn, existA, mojiA, numM1, numM2, numM3, numM4, numM5, numF, mojiF, hantei, kekka_fortune, play2, hayaku, imgSS1, imgSS2, imgSS3, imgSS4, imgSS5, imgSS6, imgSS7, imgSS8, imgSS9, imgSS10, imgSS11, gengo, mojiN, mojiT, mojiTn, canvas, ima, mojiT, mojiTn, existA, nojiA, numM1, numM2, numM3, numM4, numM5, numF, mojiF, hantei, kekka_fortune, play2, hayaku, uketori
        
    canvas.create_image(1050, 500, image=imgSS98)#02161221
    #変更400, 500, image=imgSS98,黒板画像 水平方向184ピクセル　垂直方向130ピクセル
    canvas.place(x=550, y=550)
    canvas.pack()
    #ヒント機能黒板とミニ通貨を動かす。
    
    #これは教卓だったかな 変えてないかも
    canvas.create_image(1050, 620, image=imgSS118, tags = "mig")#点滅するからタグ入れてみるか0125
    canvas.place(x=400, y=550)
    canvas.pack()
    
    numM = round((numM), 1)#skai0125
    
        
    a = numM/10000
    if a >= 1:
        numM1_a = numM - 10000
        canvas.create_image(950, 430, image=imgSS41, tags = "mig")#tagudemotukeruka0125    
        #変更450, 450, image=imgSS41 ヒントをチェックしたときにお金の位置が代わる ドンはない
        canvas.place(x=550, y=550)
        canvas.pack()
        
    else:
        tagX.append("img")
        numM1_a = numM
        
    b = numM1_a/5000
    if b >= 1:
        numM1_ab = numM1_a - 5000
        canvas.create_image(1050, 430, image=imgSS42, tags = "mig")#tagudemotukeruka0125
        #変更450, 455, image=imgSS42
        canvas.place(x=355, y=465)
        canvas.pack()
        
    else:
        numM1_ab = numM1_a
        tagX.append("img2")
        
    c1 = numM1_ab/1000
    if c1 >= 1:
        numM1_abc1 = numM1_ab - 1000
        canvas.create_image(1140, 430, image=imgSS43, tags = "mig")#tagudemotukeruka0125)
        #変更450, 460, image=imgSS43
        canvas.place(x=350, y=560)
        canvas.pack()
        
    else:
        numM1_abc1 = numM1_ab
        
    c2 = numM1_abc1/1000
    if c2 >= 1:
        numM1_abc1c2 = numM1_abc1 - 1000
        canvas.create_image(1140, 470, image=imgSS43, tags = "mig")#tagudemotukeruka0125)
        #変更450, 465, image=imgSS43
        canvas.place(x=350, y=565)
        canvas.pack()
    else:
        numM1_abc1c2 = numM1_abc1
    c3 = numM1_abc1c2/1000
    if c3 >= 1:
        numM1_abc1c2c3 = numM1_abc1c2 - 1000
        canvas.create_image(1140, 510, image=imgSS43, tags = "mig")#tagudemotukeruka0125)
        #変更450, 470, image=imgSS43
        canvas.place(x=350, y=570)
        canvas.pack()
    else:
        numM1_abc1c2c3 = numM1_abc1c2
    c4 = numM1_abc1c2c3/1000
    if c4 >= 1:
        numM1_abc1c2c3c4 = numM1_abc1c2c3 - 1000
        canvas.create_image(1140, 550, image=imgSS43, tags = "mig")#tagudemotukeruka0125)
        #変更450, 475, image=imgSS43
        canvas.place(x=350, y=575)
        canvas.pack()
    else:
        numM1_abc1c2c3c4 = numM1_abc1c2c3
    d = numM1_abc1c2c3c4/500
    if d >= 1:
        numM1_abc1c2c3c4d = numM1_abc1c2c3c4 - 500
        canvas.create_image(950, 470, image=imgSS44, tags = "mig")#tagudemotukeruka0125)
        #変更400, 480, image=imgSS44
        canvas.place(x=550, y=580)
        canvas.pack()
    else:
        numM1_abc1c2c3c4d = numM1_abc1c2c3c4
        tagX.append("img4")
    e1 = numM1_abc1c2c3c4d/100
    if e1 >= 1:
        numM1_abc1c2c3c4de1 = numM1_abc1c2c3c4d - 100
        canvas.create_image(990, 470, image=imgSS45, tags = "mig")#tagudemotukeruka0125)
        #変更400, 500, image=imgSS45
        canvas.place(x=550, y=585)
        canvas.pack()
    else:
        numM1_abc1c2c3c4de1 = numM1_abc1c2c3c4d
    e2 = numM1_abc1c2c3c4de1/100
    if e2 >= 1:
        numM1_abc1c2c3c4de1e2 = numM1_abc1c2c3c4de1 - 100
        canvas.create_image(990, 500, image=imgSS45, tags = "mig")#tagudemotukeruka0125)
        #変更400, 520, image=imgSS45
        canvas.place(x=550, y=590)
        canvas.pack()
    else:
        numM1_abc1c2c3c4de1e2 = numM1_abc1c2c3c4de1
    e3 = numM1_abc1c2c3c4de1e2/100
    if e3 >= 1:
        numM1_abc1c2c3c4de1e2e3 = numM1_abc1c2c3c4de1e2 - 100
        canvas.create_image(990, 530, image=imgSS45, tags = "mig")#tagudemotukeruka0125)
        #変更400, 540, image=imgSS45
        canvas.place(x=550, y=595)
        canvas.pack()
    else:
        numM1_abc1c2c3c4de1e2e3 = numM1_abc1c2c3c4de1e2
    e4 = numM1_abc1c2c3c4de1e2e3/100
    if e4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4 = numM1_abc1c2c3c4de1e2e3 - 100
        canvas.create_image(990, 560, image=imgSS45, tags = "mig")#tagudemotukeruka0125)
        #変更400, 560, image=imgSS45
        canvas.place(x=550, y=600)
        canvas.pack()
    else:
        numM1_abc1c2c3c4de1e2e3e4 = numM1_abc1c2c3c4de1e2e3
    f = numM1_abc1c2c3c4de1e2e3e4/50
    if f >= 1:
        numM1_abc1c2c3c4de1e2e3e4f = numM1_abc1c2c3c4de1e2e3e4 - 50
        canvas.create_image(1040, 470, image=imgSS46, tags = "mig")#tagudemotukeruka0125)    
        #変更440, 480, image=imgSS46
        canvas.place(x=550, y=580)
        canvas.pack()
    else:
        numM1_abc1c2c3c4de1e2e3e4f = numM1_abc1c2c3c4de1e2e3e4
        tagX.append("img6")
    g1 = numM1_abc1c2c3c4de1e2e3e4f/10
    if g1 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1 = numM1_abc1c2c3c4de1e2e3e4f - 10
        canvas.create_image(1040, 500, image=imgSS47, tags = "mig")#tagudemotukeruka0125)
        #変更440, 500, image=imgSS47
        canvas.place(x=550, y=585)
        canvas.pack()
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1 = numM1_abc1c2c3c4de1e2e3e4f
    g2 = numM1_abc1c2c3c4de1e2e3e4fg1/10
    if g2 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2 = numM1_abc1c2c3c4de1e2e3e4fg1 - 10
        canvas.create_image(1040, 520, image=imgSS47, tags = "mig")#tagudemotukeruka0125)
        #変更440, 520, image=imgSS47
        canvas.place(x=550, y=590)
        canvas.pack()
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2 = numM1_abc1c2c3c4de1e2e3e4fg1
    g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2/10
    if g3 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2 - 10
        canvas.create_image(1040, 540, image=imgSS47, tags = "mig")#tagudemotukeruka0125)
        #変更440, 540, image=imgSS47
        canvas.place(x=560, y=595)
        canvas.pack()
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2
    g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3/10
    if g4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3 - 10
        canvas.create_image(1040, 560, image=imgSS47, tags = "mig")#tagudemotukeruka0125)
        #変更440, 560, image=imgSS47
        canvas.place(x=560, y=600)
        canvas.pack()
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3
    h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4/5
    if h >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 - 5
        canvas.create_image(1080, 470, image=imgSS48, tags = "mig")#tagudemotukeruka0125)
        #変更480, 480, image=imgSS48元はない
        canvas.place(x=570, y=580)
        canvas.pack()
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4
        tagX.append("img8")
    i1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h/1
    if i1 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h - 1
        canvas.create_image(1080, 500, image=imgSS49, tags = "mig")#tagudemotukeruka0125)
        #変更480, 500, image=imgSS49　元はない
        canvas.place(x=100, y=100)#02161221
        #変更x=570, y=585
        canvas.pack()
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h
    i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1/1
    if i2 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 - 1
        canvas.create_image(1080, 520, image=imgSS49, tags = "mig")#tagudemotukeruka0125)
        #変更480, 520, image=imgSS49
        canvas.place(x=100, y=100)#02161221
        #変更x=570, y=590
        canvas.pack()
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1
    i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2/1
    if i3 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 - 1
        canvas.create_image(1080, 540, image=imgSS49, tags = "mig")#tagudemotukeruka0125)
        #変更480, 540, image=imgSS49
        canvas.place(x=100, y=100)#02161221
        #変更x=570, y=595
        canvas.pack()
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2
    i4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3/1
    if i4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3i4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 - 1
        canvas.create_image(1080, 560, image=imgSS49, tags = "mig")#tagudemotukeruka0125)
        #変更480, 560, image=imgSS49
        canvas.place(x=100, y=100)#02161221
        #変更x=570, y=600
        canvas.pack()
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3
        
        
    
    
def anahint(numM):
    global imgSS1, imgSS2, imgSS3, imgSS4, imgSS5, imgSS6, imgSS7, imgSS8, imgSS9, imgSS10, imgSS11, gengo, play5, play4, k3once, existA, hint, tigau, tagX, zahyohn, zahyohn2, zahyohn3, zahyohn4, zahyohn5, stptime, sttime, hayaku, susumu, mojiT, mojiTn, existA, mojiA, numM1, numM2, numM3, numM4, numM5, numF, mojiF, hantei, kekka_fortune, play2, hayaku, imgSS1, imgSS2, imgSS3, imgSS4, imgSS5, imgSS6, imgSS7, imgSS8, imgSS9, imgSS10, imgSS11, gengo, mojiN, mojiT, mojiTn, canvas, ima, mojiT, mojiTn, existA, nojiA, numM1, numM2, numM3, numM4, numM5, numF, mojiF, hantei, kekka_fortune, play2, hayaku
    
    
    numM = round((numM), 1)#skai0125
    
    a = numM/10000
    if a >= 1:
        numM1_a = numM - 10000
    
    else:
        tagX.append("img")
        numM1_a = numM
    b = numM1_a/5000
    if b >= 1:
        numM1_ab = numM1_a - 5000
    else:
        numM1_ab = numM1_a
        tagX.append("img2")
    c1 = numM1_ab/1000
    if c1 >= 1:
        numM1_abc1 = numM1_ab - 1000
    else:
        numM1_abc1 = numM1_ab
        tagX.append("img3")
    c2 = numM1_abc1/1000
    if c2 >= 1:
        numM1_abc1c2 = numM1_abc1 - 1000
    else:
        numM1_abc1c2 = numM1_abc1
    c3 = numM1_abc1c2/1000
    if c3 >= 1:
        numM1_abc1c2c3 = numM1_abc1c2 - 1000
    else:
        numM1_abc1c2c3 = numM1_abc1c2
    c4 = numM1_abc1c2c3/1000
    if c4 >= 1:
        numM1_abc1c2c3c4 = numM1_abc1c2c3 - 1000
    else:
        numM1_abc1c2c3c4 = numM1_abc1c2c3
    d = numM1_abc1c2c3c4/500
    if d >= 1:
        numM1_abc1c2c3c4d = numM1_abc1c2c3c4 - 500
    else:
        numM1_abc1c2c3c4d = numM1_abc1c2c3c4
        tagX.append("img4")
    e1 = numM1_abc1c2c3c4d/100
    if e1 >= 1:
        numM1_abc1c2c3c4de1 = numM1_abc1c2c3c4d - 100
    else:
        numM1_abc1c2c3c4de1 = numM1_abc1c2c3c4d
        tagX.append("img5")
    e2 = numM1_abc1c2c3c4de1/100
    if e2 >= 1:
        numM1_abc1c2c3c4de1e2 = numM1_abc1c2c3c4de1 - 100
    else:
        numM1_abc1c2c3c4de1e2 = numM1_abc1c2c3c4de1
    e3 = numM1_abc1c2c3c4de1e2/100
    if e3 >= 1:
        numM1_abc1c2c3c4de1e2e3 = numM1_abc1c2c3c4de1e2 - 100
    else:
        numM1_abc1c2c3c4de1e2e3 = numM1_abc1c2c3c4de1e2
    e4 = numM1_abc1c2c3c4de1e2e3/100
    if e4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4 = numM1_abc1c2c3c4de1e2e3 - 100
    else:
        numM1_abc1c2c3c4de1e2e3e4 = numM1_abc1c2c3c4de1e2e3
    f = numM1_abc1c2c3c4de1e2e3e4/50
    if f >= 1:
        numM1_abc1c2c3c4de1e2e3e4f = numM1_abc1c2c3c4de1e2e3e4 - 50
    else:
        numM1_abc1c2c3c4de1e2e3e4f = numM1_abc1c2c3c4de1e2e3e4
        tagX.append("img6")
    g1 = numM1_abc1c2c3c4de1e2e3e4f/10
    if g1 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1 = numM1_abc1c2c3c4de1e2e3e4f - 10
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1 = numM1_abc1c2c3c4de1e2e3e4f
        tagX.append("img7")
    g2 = numM1_abc1c2c3c4de1e2e3e4fg1/10
    if g2 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2 = numM1_abc1c2c3c4de1e2e3e4fg1 - 10
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2 = numM1_abc1c2c3c4de1e2e3e4fg1
    g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2/10
    if g3 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2 - 10
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3 = numM1_abc1c2c3c4de1e2e3e4fg1g2
    g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3/10
    if g4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3 - 10
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3
    h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4/5
    if h >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4 - 5
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4
        tagX.append("img8")
    i1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h/1
    if i1 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h - 1
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4h
        tagX.append("img9")
    i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1/1
    if i2 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1 - 1
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1
    i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2/1
    if i3 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2 - 1
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2
    i4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3/1
    if i4 >= 1:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3i4 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 - 1
    else:
        numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3 = numM1_abc1c2c3c4de1e2e3e4fg1g2g3g4hi1i2i3
async def sleeping(sec):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, time.sleep, sec)
    released()
    
class Timer:
    global zaq, bln, chk, bln2, chk2, flag, hantei, imgMA, imgMB, imgMC, imgMD, imgME, imgMF, imgMG, imgMH, imgMI, imgMJ, emojiTn, mojiTd, mojiTg, ahint, anahint, imgSS1, imgSS2, imgSS3, imgSS4, imgSS5, imgSS6, imgSS7, imgSS8, imgSS9, imgSS10, imgSS11, gengo, gengo2, mojiN, mojiT, mojiTn, canvas, ima, mojiT, mojiTn, existA, nojiA, numM1, numM2, numM3, numM4, numM5, numF, mojiF, hantei, kekka_fortune, play2, hayaku, Knum, released, sleeping
    def __init__(self):
        self.root = canvas
        self.label = tk.Label(self.root)
        self.label["font"] = ("Helvetica", 32)
        self.label["bg"] = "#32CD30"
        self.label["fg"] = "white"
        self.label.place(x = 5, y = 105)#02161221
            
        self.label2 = tk.Label(self.root)
        self.label2["font"] = ("Helvetica", 32)
        self.label2["bg"] = "#32CD30"
        self.label2["fg"] = "white"
        self.label2["text"] = "のこり"
    
        self.label3 = tk.Label(self.root)
        self.label3["font"] = ("Helvetica", 32)
        self.label3["bg"] = "#32CD30"
        self.label3["fg"] = "white"
        self.label3["text"] = "     秒"
                
        self.labelR = tk.Label(self.root)
        self.labelR["font"] = ("Helvetica", 20)
        self.labelR["bg"] = "#32CD30"
        self.labelR["fg"] = "black"
        self.label.place(x = 300, y = 300)#0125
        
    def changeLabelText(self):
        global zaq, bln, chk, bln2, chk2, flag, hantei, imgMA, imgMB, imgMC, imgMD, imgME, imgMF, imgMG, imgMH, imgMI, imgMJ, emojiTn, mojiTg, mojiTd, ahint, anahint, imgSS1, imgSS2, imgSS3, imgSS4, imgSS5, imgSS6, imgSS7, imgSS8, imgSS9, imgSS10, imgSS11, gengo, gengo2, play5, play4, k3once, existA, hint, tigau, tagX, zahyohn, zahyohn2, zahyohn3, zahyohn4, zahyohn5, stptime, sttime, hayaku, susumu, mojiT, mojiTn, existA, mojiA, numM1, numM2, numM3, numM4, numM5, numF, mojiF, hantei, kekka_fortune, play2, hayaku, Knum, released, sleeping
        
        while True:
        
            if sttime == 3:
                
                susumu = time.time() - ima
                hayaku = 300.00 - susumu
    
                if hayaku < 0.00:
                    hantei = 1
                    mojiT.pack_forget()
                    mojiTn.pack_forget()
                    emojiT.pack_forget()
                    kekka_fortune()
                #変更x = 2, y = 543 のこり
                #さらに変更x = 2, y = 543 のこり
                self.label2.place(x = 900, y = 80)#02161226
                self.label3.place(x = 928, y = 135)#02161226
                realK3()#0125deike
                #0128 kokodakedemoiika madakijo↓
                self.labelR.place(x = 600, y = 5)#sikatanai0125
                self.label["bg"] = "#32CD30"
                self.label["fg"] = "white"
                self.label2["bg"] = "#32CD30"
                self.label2["fg"] = "white"
                self.label3["bg"] = "#32CD30"
                self.label3["fg"] = "white"
                
                self.labelR["bg"] = "#32CD30"#02160125
                self.labelR["fg"] = "black"#0128madamikaijo
                self.label.place(x = 900, y = 135)#02161226
                self.label3.lower()#02161226
        
                #0128madamikaijo
                self.labelR.lower()#geyadondebmadabaguru0125
                if 0.10 <= hayaku <= 15.00:                    
                    self.label["bg"] = "yellow"
                    self.label["fg"] = "red"
                    self.label2["bg"] = "yellow"
                    self.label2["fg"] = "red"
                    self.label3["bg"] = "yellow"
                    self.label3["fg"] = "red"
                    #変更変更x = 230, y = 543
                    #さらに変更x = 230, y = 543
        
                    play2()
                                    
                self.label["text"] = format(hayaku, '.0f')                
                #m0128madamikaijo labelR
                if gengo2 == 2:
                    Knum = Knum/100
                elif gengo2 == 3:
                    Knum = Knum*100
                self.labelR["text"] = format(Knum, '.1f')#zatudakedokoresikaneena0125
                if gengo2 == 2:
                    Knum = Knum*100
                elif gengo2 == 3:
                    Knum = Knum/100
                
            if stptime == 3:
                self.label.place_forget()
                self.label2.place_forget()
                self.label3.place_forget()
                self.labelR.place_forget()#0128mada
            elif stptime == 0 and existA == 1000000:
                self.label.place_forget()
                self.label2.place_forget()
                self.label3.place_forget()
                self.labelR.place_forget()#0128mada
                sttime = 0
                stptime = 3
            
            if k3once == 3:
                mojiF.pack_forget()
                mojiT.pack_forget()
                emojiT.pack_forget()
                
                
                
                if hint == 1:
                    tagX = []
                    anahint(numM1)
                    if tigau == 1:
                        tgbutton.place(x = 130, y = 210)#02161225
    #                     hint = 1
                    else:
                        tgbutton.place_forget()
                    
                
                if existA == 0:
                    existA = 3
                    hnbutton.place_forget()
                    
                    if zahyohn == 1:
                        hnbutton['text'] = "正解!"
                        hnbutton.place(x = 5, y = 250)
                        
                        
                        play5()
                    elif zahyohn == 2:
                        existA = 100000
                        
                    else:
                        pass
        
                    
                elif existA == 3:
                    canvas.delete("all")
    
    
                    if gengo == 2:
                        imgSS2 = tk.PhotoImage(file = 'imgSS/50元札_小.png', master = root)
                        imgSS3 = tk.PhotoImage(file = 'imgSS/5元札_小.png', master = root)
                        imgSS4 = tk.PhotoImage(file = 'imgSS/5角札_小.png', master = root)
                        imgSS5 = tk.PhotoImage(file = 'imgSS/travel_passport2.png', master = root)
                        imgSS6 = tk.PhotoImage(file = 'imgSS/100元札_小.png', master = root)
                        imgSS7 = tk.PhotoImage(file = 'imgSS/10元札_小.png', master = root)
                        imgSS8 = tk.PhotoImage(file = 'imgSS/1元札_小.png', master = root)
                        imgSS9 = tk.PhotoImage(file = 'imgSS/1角札_小.png', master = root)
                        imgSS10 = tk.PhotoImage(file = 'imgSS/travel_passport2.png', master = root)
    
                        imgSS94 = tk.PhotoImage(file = 'imgSS/nitobe1-14.png', master = root)
                        imgSS93 = tk.PhotoImage(file = 'imgSS/natumekyu1000.png', master = root)
                        imgSS92 = tk.PhotoImage(file = 'imgSS/money_10000_shibusawa.png', master = root)
                        imgSS91 = tk.PhotoImage(file = 'imgSS/travel_passport2.png', master = root)
                        imgSS90 = tk.PhotoImage(file = 'imgSS/money_2000.png', master = root)
                        imgSS89 = tk.PhotoImage(file = 'imgSS/money_1000_kitazato.png', master = root)
                        imgSS88 = tk.PhotoImage(file = 'imgSS/money_5000_tsuda.png', master = root)
                        imgSS87 = tk.PhotoImage(file = 'imgSS/morioka4489.png', master = root)
                        imgSS86 = tk.PhotoImage(file = 'imgSS/nise_2000.png', master = root)
    
                    elif gengo == 3:
                        imgSS2 = tk.PhotoImage(file = 'imgSS/50万ドン_小.png', master = root)
                        imgSS3 = tk.PhotoImage(file = 'imgSS/5万ドン_小.png', master = root)
                        imgSS4 = tk.PhotoImage(file = 'imgSS/5千ドン_小.png', master = root)
                        imgSS5 = tk.PhotoImage(file = 'imgSS/5百ドン_小.png', master = root)
                        imgSS6 = tk.PhotoImage(file = 'imgSS/travel_passport2.png', master = root)
                        imgSS7 = tk.PhotoImage(file = 'imgSS/10万ドン_小.png', master = root)
                        imgSS8 = tk.PhotoImage(file = 'imgSS/1万ドン_小.png', master = root)
                        imgSS9 = tk.PhotoImage(file = 'imgSS/千ドン_小.png', master = root)
                        imgSS10 = tk.PhotoImage(file = 'imgSS/百ドン_小.png', master = root)
                        
                        imgSS94 = tk.PhotoImage(file = 'imgSS/eur100.png', master = root)
                        imgSS93 = tk.PhotoImage(file = 'imgSS/eur50.png', master = root)
                        imgSS92 = tk.PhotoImage(file = 'imgSS/eur10.png', master = root)
                        imgSS91 = tk.PhotoImage(file = 'imgSS/eur5.png', master = root)
                        imgSS90 = tk.PhotoImage(file = 'imgSS/1eurocoin.png', master = root)
                        imgSS89 = tk.PhotoImage(file = 'imgSS/50eurocent.png', master = root)
                        imgSS88 = tk.PhotoImage(file = 'imgSS/10eurocent.png', master = root)
                        imgSS87 = tk.PhotoImage(file = 'imgSS/5eurocent.png', master = root)
                        imgSS86 = tk.PhotoImage(file = 'imgSS/1eurocent.png', master = root)
                    elif gengo == 5:
                        imgSS2 = tk.PhotoImage(file = 'imgSS/50元札_小.png', master = root)
                        imgSS3 = tk.PhotoImage(file = 'imgSS/5元札_小.png', master = root)
                        imgSS4 = tk.PhotoImage(file = 'imgSS/5角札_小.png', master = root)
                        imgSS5 = tk.PhotoImage(file = 'imgSS/travel_passport2.png', master = root)
                        imgSS6 = tk.PhotoImage(file = 'imgSS/100元札_小.png', master = root)
                        imgSS7 = tk.PhotoImage(file = 'imgSS/10元札_小.png', master = root)
                        imgSS8 = tk.PhotoImage(file = 'imgSS/1元札_小.png', master = root)
                        imgSS9 = tk.PhotoImage(file = 'imgSS/1角札_小.png', master = root)
                        imgSS10 = tk.PhotoImage(file = 'imgSS/travel_passport2.png', master = root)
    
    
                        imgSS94 = tk.PhotoImage(file = 'imgSS/nitobe1-14.png', master = root)
                        imgSS93 = tk.PhotoImage(file = 'imgSS/natumekyu1000.png', master = root)
                        imgSS92 = tk.PhotoImage(file = 'imgSS/money_10000_shibusawa.png', master = root)
                        imgSS91 = tk.PhotoImage(file = 'imgSS/travel_passport2.png', master = root)
                        imgSS90 = tk.PhotoImage(file = 'imgSS/money_2000.png', master = root)
                        imgSS89 = tk.PhotoImage(file = 'imgSS/money_1000_kitazato.png', master = root)
                        imgSS88 = tk.PhotoImage(file = 'imgSS/money_5000_tsuda.png', master = root)
                        imgSS87 = tk.PhotoImage(file = 'imgSS/morioka4489.png', master = root)
                        imgSS86 = tk.PhotoImage(file = 'imgSS/nise_2000.png', master = root)
                    elif gengo == 6:
                        imgSS2 = tk.PhotoImage(file = 'imgSS/50万ドン_小.png', master = root)
                        imgSS3 = tk.PhotoImage(file = 'imgSS/5万ドン_小.png', master = root)
                        imgSS4 = tk.PhotoImage(file = 'imgSS/5千ドン_小.png', master = root)
                        imgSS5 = tk.PhotoImage(file = 'imgSS/5百ドン_小.png', master = root)
                        imgSS6 = tk.PhotoImage(file = 'imgSS/travel_passport2.png', master = root)
                        imgSS7 = tk.PhotoImage(file = 'imgSS/10万ドン_小.png', master = root)
                        imgSS8 = tk.PhotoImage(file = 'imgSS/1万ドン_小.png', master = root)
                        imgSS9 = tk.PhotoImage(file = 'imgSS/千ドン_小.png', master = root)
                        imgSS10 = tk.PhotoImage(file = 'imgSS/百ドン_小.png', master = root)
                      
                        imgSS94 = tk.PhotoImage(file = 'imgSS/eur100.png', master = root)
                        imgSS93 = tk.PhotoImage(file = 'imgSS/eur50.png', master = root)
                        imgSS92 = tk.PhotoImage(file = 'imgSS/eur10.png', master = root)
                        imgSS91 = tk.PhotoImage(file = 'imgSS/eur5.png', master = root)
                        imgSS90 = tk.PhotoImage(file = 'imgSS/1eurocoin.png', master = root)
                        imgSS89 = tk.PhotoImage(file = 'imgSS/50eurocent.png', master = root)
                        imgSS88 = tk.PhotoImage(file = 'imgSS/10eurocent.png', master = root)
                        imgSS87 = tk.PhotoImage(file = 'imgSS/5eurocent.png', master = root)
                        imgSS86 = tk.PhotoImage(file = 'imgSS/1eurocent.png', master = root)
                    else:
                        imgSS2 = tk.PhotoImage(file = 'imgSS/money_5000.png', master = root)
                        imgSS3 = tk.PhotoImage(file = 'imgSS/money_500.png', master = root)
                        imgSS4 = tk.PhotoImage(file = 'imgSS/money_50.png', master = root)
                        imgSS5 = tk.PhotoImage(file = 'imgSS/money_5.png', master = root)
                        imgSS6 = tk.PhotoImage(file = 'imgSS/money_10000.png', master = root)
                        imgSS7 = tk.PhotoImage(file = 'imgSS/money_1000.png', master = root)
                        imgSS8 = tk.PhotoImage(file = 'imgSS/money_100.png', master = root)
                        imgSS9 = tk.PhotoImage(file = 'imgSS/money_10.png', master = root)
                        imgSS10 = tk.PhotoImage(file = 'imgSS/money_1.png', master = root)
    
                        
                        imgSS94 = tk.PhotoImage(file = 'imgSS/money_100dollar_new.png', master = root)
                        imgSS93 = tk.PhotoImage(file = 'imgSS/money_dollar50.png', master = root)
                        imgSS92 = tk.PhotoImage(file = 'imgSS/money_dollar10.png', master = root)
                        imgSS91 = tk.PhotoImage(file = 'imgSS/money_dollar5.png', master = root)
                        imgSS90 = tk.PhotoImage(file = 'imgSS/money_dollar1.png', master = root)
                        imgSS89 = tk.PhotoImage(file = 'imgSS/money_coin_america_25_reverse.png', master = root)
                        imgSS88 = tk.PhotoImage(file = 'imgSS/money_coin_america_10_reverse.png', master = root)
                        imgSS87 = tk.PhotoImage(file = 'imgSS/money_coin_america_5_reverse.png', master = root)
                        imgSS86 = tk.PhotoImage(file = 'imgSS/money_coin_america_1_reverse.png', master = root)
                        
                    if hint == 1:
                        tagX = []
                        ahint(numM1)
                        if tigau == 1:
                            tgbutton.place(x = 130, y = 210)#02161225
                        else:
                            tgbutton.place_forget()
     
                    mojiTn.pack_forget()
                    mojiTd.pack_forget()
                    mojiTg.pack_forget()
                
                    if gengo == 2:
                        mojiTg = tk.Text(height=1, width=62, wrap="none")#02161221
                        #変更width=25 白のテキスト変更
        
                        mojiTg.tag_configure("f", foreground="#FF0100")
                        mojiTg.tag_configure("r", foreground="#000000")
                        mojiTg.tag_configure("g", foreground="#FF0000")
                        mojiTg.tag_configure("b", foreground="#000000")
    #                     mojiTn.insert("end", "次‼", 'f')
                        mojiTg.insert("end","　　　　　　　　　　　トレーに", 'r')#02161221
            #変更半角スペースあける
                        mojiTg.insert("end", str(numM1/100), 'g')
                        mojiTg.insert("end", "元ピッタリはらって!", 'b')#02161226
                        mojiTg.configure(state="disabled") # 読取専用に
                        mojiTg.pack(anchor='n',expand=1)
                    elif gengo == 3:
                        mojiTd = tk.Text(height=1, width=62, wrap="none")#02161221
                        #変更width=25
        
                        mojiTd.tag_configure("f", foreground="#FF0100")
                        mojiTd.tag_configure("r", foreground="#000000")
                        mojiTd.tag_configure("g", foreground="#FF0000")
                        mojiTd.tag_configure("b", foreground="#000000")
    #                     mojiTn.insert("end", "次‼", 'f')
                        mojiTd.insert("end","　　　　　　　　　　　トレーに", 'r')#02161221
            #変更半角スペースあける
                        mojiTd.insert("end", str(numM1*100), 'g')
                        mojiTd.insert("end", "ドンピッタリはらって!", 'b')
                        mojiTd.configure(state="disabled") # 読取専用に
                        mojiTd.pack(anchor='n',expand=1)
                    elif gengo == 1:                        
                        mojiTn = tk.Text(height=1, width=62, wrap="none")#02161221
                        #変更width=25
        
                        mojiTn.tag_configure("f", foreground="#FF0100")
                        mojiTn.tag_configure("r", foreground="#000000")
                        mojiTn.tag_configure("g", foreground="#FF0000")
                        mojiTn.tag_configure("b", foreground="#000000")
    #                     mojiTn.insert("end", "次‼", 'f')
                        mojiTn.insert("end","　　　　　　　　　　　トレーに", 'r')#02161221
            #変更半角スペースあける
                        mojiTn.insert("end", str(numM1), 'g')
                        mojiTn.insert("end", "円ピッタリはらって!", 'b')
                        mojiTn.configure(state="disabled") # 読取専用に
                        mojiTn.pack(anchor='n',expand=1)
                    else:
                        emojiTn = tk.Text(height=1, width=62, wrap="none")#02161223
                        emojiTn.tag_configure("r", foreground="#000000")
                        emojiTn.tag_configure("g", foreground="#FF0000")
                        emojiTn.tag_configure("b", foreground="#000000")
                        emojiTn.insert("end", "　　　　　　　　　　　　2つの商品の", 'r')#02161223
                        
                        emojiTn.insert("end", "合計額を", 'g')
                        emojiTn.insert("end", "ピッタリはらって!", 'b')
                        emojiTn.configure(state="disabled")
                        emojiTn.pack(anchor='n',expand=1)
                        
                        canvas.create_image(50, 50, image=imgMA)#02161225
        #50, 165, image=imgMA#hs
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(210, 50, image=imgMB)#02161225
        #210, 165, image=imgMB#hs
                        canvas.place(x=100, y=100)
                        canvas.pack()
            
            
                        canvas.create_image(130, 50, image=imgSS109, tags = "mig")#02160125)
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(290, 50, image=imgSS115, tags = "mig")#02160125)
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(370, 60, image=imgSS116)
                        canvas.place(x=100, y=100)
                        canvas.pack()                                                
                        
        
                    canvas.create_image(650, 100, image=imgSS96)
                    canvas.place(x=150, y=150)
                    canvas.pack()
                
                    #0206
                    stockX = []
                    stockY = []
                    a1man = random.randint(10,800)
                    stockX.append(a1man)
                    b1man = random.randint(250,650)
                    stockY.append(b1man)
                    singi = True
                    while singi:
                        signal = "yes"
                        a5000 = random.randint(10,800)
                        for you in range(len(stockX)):                            
                            if stockX[you]+30 >= a5000 >= stockX[you]-30:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockX.append(a5000)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        b5000 = random.randint(250,650)
                        for you in range(len(stockY)):                            
                            if stockY[you]+10 >= b5000 >= stockY[you]-10:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockY.append(b5000)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        a500 = random.randint(10,800)
                        for you in range(len(stockX)):                            
                            if stockX[you]+30 >= a500 >= stockX[you]-30:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockX.append(a500)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        b500 = random.randint(250,650)
                        for you in range(len(stockY)):                            
                            if stockY[you]+10 >= b500 >= stockY[you]-10:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockY.append(b500)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        a50 = random.randint(10,800)
                        for you in range(len(stockX)):                            
                            if stockX[you]+30 >= a50 >= stockX[you]-30:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockX.append(a50)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        b50 = random.randint(250,650)
                        for you in range(len(stockY)):                            
                            if stockY[you]+10 >= b50 >= stockY[you]-10:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockY.append(b50)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        a5en = random.randint(10,800)
                        for you in range(len(stockX)):                            
                            if stockX[you]+30 >= a5en >= stockX[you]-30:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockX.append(a5en)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        b5en = random.randint(250,650)
                        for you in range(len(stockY)):                            
                            if stockY[you]+10 >= b5en >= stockY[you]-10:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockY.append(b5en)
                            singi = False
                    singi = True
                    for me in range(4):
                        singi = True
                        while singi:
                            signal = "yes"
                            a1000 = random.randint(10,800)
                            for you in range(len(stockX)):                            
                                if stockX[you]+30 >= a1000 >= stockX[you]-30:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockX.append(a1000)
                                singi = False
                        singi = True
                        while singi:
                            signal = "yes"
                            b1000 = random.randint(250,650)
                            for you in range(len(stockY)):                            
                                if stockY[you]+10 >= b1000 >= stockY[you]-10:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockY.append(b1000)
                                singi = False                                
                        canvas.create_image(a1000, b1000, image=imgSS7, tags = "img3")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    for me in range(4):
                        singi = True
                        while singi:
                            signal = "yes"
                            a100 = random.randint(10,800)
                            for you in range(len(stockX)):                            
                                if stockX[you]+20 >= a100 >= stockX[you]-20:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockX.append(a100)
                                singi = False
                        singi = True
                        while singi:
                            signal = "yes"
                            b100 = random.randint(250,650)
                            for you in range(len(stockY)):                            
                                if stockY[you]+10 >= b100 >= stockY[you]-10:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockY.append(b100)
                                singi = False                                
                        canvas.create_image(a100, b100, image=imgSS8, tags = "img5")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    for me in range(4):
                        singi = True
                        while singi:
                            signal = "yes"
                            a10 = random.randint(10,800)
                            for you in range(len(stockX)):                            
                                if stockX[you]+20 >= a10 >= stockX[you]-20:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockX.append(a10)
                                singi = False
                        singi = True
                        while singi:
                            signal = "yes"
                            b10 = random.randint(250,650)
                            for you in range(len(stockY)):                            
                                if stockY[you]+10 >= b10 >= stockY[you]-10:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockY.append(b10)
                                singi = False                                
                        canvas.create_image(a10, b10, image=imgSS9, tags = "img7")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    for me in range(4):
                        singi = True
                        while singi:
                            signal = "yes"
                            a1en = random.randint(10,800)
                            for you in range(len(stockX)):                            
                                if stockX[you]+20 >= a1en >= stockX[you]-20:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockX.append(a1en)
                                singi = False
                        singi = True
                        while singi:
                            signal = "yes"
                            b1en = random.randint(250,650)
                            for you in range(len(stockY)):                            
                                if stockY[you]+10 >= b1en >= stockY[you]-10:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockY.append(b1en)
                                singi = False                                
                        canvas.create_image(a1en, b1en, image=imgSS10, tags = "img9")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                                               
                    for ii in range(1):
    
    #                     a1man = random.randint(1,400)
                #変更(1,400)
    #                     b1man = random.randint(100,500)
                #変更(100,500)
                        canvas.create_image(a1man, b1man, image=imgSS6, tags = "img")
                        canvas.place(x=100, y=100)
                        canvas.pack()
    #                     a5000 = random.randint(1,400)
                #変更(1,400)
    #                     b5000 = random.randint(100,500)
                #変更(100,500)
                        canvas.create_image(a5000, b5000, image=imgSS2, tags = "img2")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                            
    #                     a500 = random.randint(1,400)
                    #変更(1,400)
    #                     b500 = random.randint(100,500)
                #変更(100,500)
                        canvas.create_image(a500, b500, image=imgSS3, tags = "img4")
                        canvas.place(x=100, y=100)
                        canvas.pack()
    #                     a50 = random.randint(1,400)
                    #変更(1,400)
    #                     b50 = random.randint(100,500)
                #変更(100,500)
                        canvas.create_image(a50, b50, image=imgSS4, tags = "img6")
                        canvas.place(x=100, y=100)
                        canvas.pack()
    #                     a5en = random.randint(1,400)
                    #変更(1,400)
    #                     b5en = random.randint(100,500)
                #変更(100,500)
                        canvas.create_image(a5en, b5en, image=imgSS5, tags = "img8")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    
                    if zaq == 1:#02161226 tamesini zaqzaq mode 1set
    
                        a100d = random.randint(1,700)#02161221#hs 1,1100
                        b100d = random.randint(200,600)#02161221#hs 100,600
                        canvas.create_image(a100d, b100d, image=imgSS94, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        a50d = random.randint(1,700)#02161221#hs 1,1100
                        b50d = random.randint(200,600)#02161221#hs 100,600
                        canvas.create_image(a50d, b50d, image=imgSS93, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        for i in range(4):
                            a10d = random.randint(1,700)#02161221#hs 1,1100
                            b10d = random.randint(200,600)#02161221#hs 100,600
                            canvas.create_image(a10d, b10d, image=imgSS92, tags = "img1")
                            canvas.place(x=100, y=100)
                            canvas.pack()
                        a5d = random.randint(1,700)#02161221#hs 1,1100
                        b5d = random.randint(200,600)#02161221#hs 100,600
                        canvas.create_image(a5d, b5d, image=imgSS91, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        for i in range(4):
                            a1d = random.randint(1,700)#02161221#hs 1,1100
                            b1d = random.randint(200,600)#02161221#hs 100,600
                            canvas.create_image(a1d, b1d, image=imgSS90, tags = "img1")
                            canvas.place(x=100, y=100)
                            canvas.pack()
                        a50c = random.randint(1,700)#02161221#hs 1,1100
                        b50c = random.randint(200,600)#02161221#hs 100,600
                        canvas.create_image(a50c, b50c, image=imgSS89, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        for i in range(4):
                            a10c = random.randint(1,700)#02161221#hs 1,1100
                            b10c = random.randint(200,600)#02161221#hs100,600
                            canvas.create_image(a10c, b10c, image=imgSS88, tags = "img1")
                            canvas.place(x=100, y=100)
                            canvas.pack()
                        a5c = random.randint(1,700)#02161221#hs 1,1100
                        b5c = random.randint(200,600)#02161221#hs100,600
                        canvas.create_image(a5c, b5c, image=imgSS87, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        for i in range(4):
                            a1c = random.randint(1,700)#02161221#hs 1,1100
                            b1c = random.randint(200,600)#02161221#hs100,600
                            canvas.create_image(a1c, b1c, image=imgSS86, tags = "img1")
                            canvas.place(x=100, y=100)
                            canvas.pack()
                           
                        zm1button.place(x=860, y=100)#02161221
                        
                    
                    existA = 10
                elif existA == 100000:
                    k3once = 18
                else:
                    existA = 10
            
            elif k3once == 6:
                mojiF.pack_forget()
                mojiT.pack_forget()
                emojiT.pack_forget()
                            
                
                if hint == 1:
                    tagX = []
                    anahint(numM2)
                    
                    if tigau == 1:
                        tgbutton.place(x = 5, y = 210)
    #                     hint = 1
                    else:
                        tgbutton.place_forget()
                
                if existA == 10:
                    existA = 30
                    hnbutton.place_forget()
                    zm1button.place_forget()
                    zm2button.place_forget()
                    zm3button.place_forget()
                    zm4button.place_forget()
                    zm5button.place_forget()
                    
                    if zahyohn2 == 1:
                        hnbutton['text'] = "Q1正解"  
                        
                        hnbutton.place(x = 5, y = 250)#02161226
                        play5()
                        
                        canvas.create_image(630, 300, image=imgSS106)#02161225
                    #250, 300, image=imgSS106#hs
                        canvas.place(x=250, y=300)
                        canvas.pack()
                        
                    elif zahyohn2 == 2:
                        existA = 100000
                        
                        canvas.create_image(630, 300, image=imgSS107)#02161225
            #250, 300, image=imgSS107
                        canvas.place(x=250, y=300)
                        canvas.pack()
                        
                    else:
    
    
                        canvas.create_image(630, 300, image=imgSS108)#hen1225
            #250, 300, image=imgSS108#
                        canvas.place(x=250, y=300)
                        canvas.pack()
                        
                        existA = 100000#長らく封印してたが1224に解除
                    
                elif existA == 30:
                    canvas.delete("all")
                    
                    
                    if hint == 1:
                        tagX = []
                        ahint(numM2)
                        
                        if tigau == 1:
                            tgbutton.place(x = 130, y = 210)#02161225
        #x = 5, y = 210
                        else:
                            tgbutton.place_forget()
                    
                    mojiTn.pack_forget()
                    mojiTd.pack_forget()
                    mojiTg.pack_forget()
                    emojiTn.pack_forget()
                    
                    if gengo == 2:
                        mojiTg = tk.Text(height=1, width=62, wrap="none")#02161222
                #変更width=25
                        mojiTg.tag_configure("f", foreground="#FF0100")
                        mojiTg.tag_configure("r", foreground="#000000")
                        mojiTg.tag_configure("g", foreground="#FF0000")
                        mojiTg.tag_configure("b", foreground="#000000")
    #                     mojiTn.insert("end", "次‼", 'f')
                        mojiTg.insert("end","　　　　　　　　　　　トレーに", 'r')#02161222
            #変更半角スペース開ける
                        mojiTg.insert("end", str(numM2/100), 'g')
                        mojiTg.insert("end", "元ピッタリはらって!", 'b')
                        mojiTg.configure(state="disabled") # 読取専用に
                        mojiTg.pack(anchor='n',expand=1)
                    elif gengo == 3:
                        mojiTd = tk.Text(height=1, width=62, wrap="none")#02161222
                        #変更width=25
                        mojiTd.tag_configure("f", foreground="#FF0100")
                        mojiTd.tag_configure("r", foreground="#000000")
                        mojiTd.tag_configure("g", foreground="#FF0000")
                        mojiTd.tag_configure("b", foreground="#000000")
    #                     mojiTn.insert("end", "次‼", 'f')
                        mojiTd.insert("end","　　　　　　　　　　　トレーに", 'r')#02161222
            #変更半角スペース開ける
                        mojiTd.insert("end", str(numM2*100), 'g')
                        mojiTd.insert("end", "ドンピッタリはらって!", 'b')
                        mojiTd.configure(state="disabled") # 読取専用に
                        mojiTd.pack(anchor='n',expand=1)
                    elif gengo == 1:                        
                        mojiTn = tk.Text(height=1, width=62, wrap="none")#02161222
                        #変更width=25
                        mojiTn.tag_configure("f", foreground="#FF0100")
                        mojiTn.tag_configure("r", foreground="#000000")
                        mojiTn.tag_configure("g", foreground="#FF0000")
                        mojiTn.tag_configure("b", foreground="#000000")
    #                     mojiTn.insert("end", "次‼", 'f')
                        mojiTn.insert("end","　　　　　　　　　　　トレーに", 'r')#02161222
            #変更半角スペース開ける
                        mojiTn.insert("end", str(numM2), 'g')
                        mojiTn.insert("end", "円ピッタリはらって!", 'b')
                        mojiTn.configure(state="disabled") # 読取専用に
                        mojiTn.pack(anchor='n',expand=1)
                    else:
                        emojiTn = tk.Text(height=1, width=62, wrap="none")#02161223
                        emojiTn.tag_configure("r", foreground="#000000")
                        emojiTn.tag_configure("g", foreground="#FF0000")
                        emojiTn.tag_configure("b", foreground="#000000")
                        emojiTn.insert("end", "　　　　　　　　　　　　2つの商品の", 'r')#02161223
    
                        emojiTn.insert("end", "合計額を", 'g')
                        emojiTn.insert("end", "ピッタリはらって!", 'b')
                        emojiTn.configure(state="disabled")
                        emojiTn.pack(anchor='n',expand=1)
                        
                        canvas.create_image(50, 50, image=imgMC)#02161225
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(210, 50, image=imgMD)#02161225
        #商品210, 165, image=imgMD#
                        canvas.place(x=100, y=100)
                        canvas.pack()
            
            
                        canvas.create_image(130, 50, image=imgSS109, tags = "mig")#02160125)
        #130, 165, image=imgSS109 +
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(290, 50, image=imgSS115, tags = "mig")#02160125)
                        #290, 165, image=imgSS115 =
                        canvas.place(x=100, y=100)
                        canvas.pack()
                
                        canvas.create_image(370, 60, image=imgSS116)#02161225
                        #370, 165, image=imgSS116 ?
                        canvas.place(x=100, y=100)
                        canvas.pack()                                                
                        
                    canvas.create_image(650, 100, image=imgSS96)#02161222
                #変更250,50
                    canvas.place(x=150, y=150)
                    canvas.pack()
                    
                    #0206
                    stockX = []
                    stockY = []
                    a1man = random.randint(10,800)
                    stockX.append(a1man)
                    b1man = random.randint(250,650)
                    stockY.append(b1man)
                    singi = True
                    while singi:
                        signal = "yes"
                        a5000 = random.randint(10,800)
                        for you in range(len(stockX)):                            
                            if stockX[you]+30 >= a5000 >= stockX[you]-30:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockX.append(a5000)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        b5000 = random.randint(250,650)
                        for you in range(len(stockY)):                            
                            if stockY[you]+10 >= b5000 >= stockY[you]-10:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockY.append(b5000)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        a500 = random.randint(10,800)
                        for you in range(len(stockX)):                            
                            if stockX[you]+30 >= a500 >= stockX[you]-30:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockX.append(a500)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        b500 = random.randint(250,650)
                        for you in range(len(stockY)):                            
                            if stockY[you]+10 >= b500 >= stockY[you]-10:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockY.append(b500)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        a50 = random.randint(10,800)
                        for you in range(len(stockX)):                            
                            if stockX[you]+30 >= a50 >= stockX[you]-30:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockX.append(a50)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        b50 = random.randint(250,650)
                        for you in range(len(stockY)):                            
                            if stockY[you]+10 >= b50 >= stockY[you]-10:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockY.append(b50)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        a5en = random.randint(10,800)
                        for you in range(len(stockX)):                            
                            if stockX[you]+30 >= a5en >= stockX[you]-30:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockX.append(a5en)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        b5en = random.randint(250,650)
                        for you in range(len(stockY)):                            
                            if stockY[you]+10 >= b5en >= stockY[you]-10:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockY.append(b5en)
                            singi = False
                    singi = True
                    for me in range(4):
                        singi = True
                        while singi:
                            signal = "yes"
                            a1000 = random.randint(10,800)
                            for you in range(len(stockX)):                            
                                if stockX[you]+30 >= a1000 >= stockX[you]-30:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockX.append(a1000)
                                singi = False
                        singi = True
                        while singi:
                            signal = "yes"
                            b1000 = random.randint(250,650)
                            for you in range(len(stockY)):                            
                                if stockY[you]+10 >= b1000 >= stockY[you]-10:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockY.append(b1000)
                                singi = False                                
                        canvas.create_image(a1000, b1000, image=imgSS7, tags = "img3")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    for me in range(4):
                        singi = True
                        while singi:
                            signal = "yes"
                            a100 = random.randint(10,800)
                            for you in range(len(stockX)):                            
                                if stockX[you]+20 >= a100 >= stockX[you]-20:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockX.append(a100)
                                singi = False
                        singi = True
                        while singi:
                            signal = "yes"
                            b100 = random.randint(250,650)
                            for you in range(len(stockY)):                            
                                if stockY[you]+10 >= b100 >= stockY[you]-10:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockY.append(b100)
                                singi = False                                
                        canvas.create_image(a100, b100, image=imgSS8, tags = "img5")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    for me in range(4):
                        singi = True
                        while singi:
                            signal = "yes"
                            a10 = random.randint(10,800)
                            for you in range(len(stockX)):                            
                                if stockX[you]+20 >= a10 >= stockX[you]-20:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockX.append(a10)
                                singi = False
                        singi = True
                        while singi:
                            signal = "yes"
                            b10 = random.randint(250,650)
                            for you in range(len(stockY)):                            
                                if stockY[you]+10 >= b10 >= stockY[you]-10:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockY.append(b10)
                                singi = False                                
                        canvas.create_image(a10, b10, image=imgSS9, tags = "img7")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    for me in range(4):
                        singi = True
                        while singi:
                            signal = "yes"
                            a1en = random.randint(10,800)
                            for you in range(len(stockX)):                            
                                if stockX[you]+20 >= a1en >= stockX[you]-20:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockX.append(a1en)
                                singi = False
                        singi = True
                        while singi:
                            signal = "yes"
                            b1en = random.randint(250,650)
                            for you in range(len(stockY)):                            
                                if stockY[you]+10 >= b1en >= stockY[you]-10:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockY.append(b1en)
                                singi = False                                
                        canvas.create_image(a1en, b1en, image=imgSS10, tags = "img9")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    
                    for iii in range(1):#02161226
        
    #                     a1man = random.randint(1,400)
                #変更(1,400)
    #                     b1man = random.randint(100,500)
                #変更(100,600)
                        canvas.create_image(a1man, b1man, image=imgSS6, tags = "img")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(a5000, b5000, image=imgSS2, tags = "img2")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(a500, b500, image=imgSS3, tags = "img4")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(a50, b50, image=imgSS4, tags = "img6")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(a5en, b5en, image=imgSS5, tags = "img8")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    if zaq == 1:#02161226 tamesini zaqzaq mode 1set
    
                        a100d = random.randint(1,700)#02161221#hs 1,1100
                        b100d = random.randint(200,600)#02161221#hs 100,600
                        canvas.create_image(a100d, b100d, image=imgSS94, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        a50d = random.randint(1,700)#02161221#hs 1,1100
                        b50d = random.randint(200,600)#02161221#hs 100,600
                        canvas.create_image(a50d, b50d, image=imgSS93, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        for i in range(4):
                            a10d = random.randint(1,700)#02161221#hs 1,1100
                            b10d = random.randint(200,600)#02161221#hs 100,600
                            canvas.create_image(a10d, b10d, image=imgSS92, tags = "img1")
                            canvas.place(x=100, y=100)
                            canvas.pack()
                        a5d = random.randint(1,700)#02161221#hs 1,1100
                        b5d = random.randint(200,600)#02161221#hs 100,600
                        canvas.create_image(a5d, b5d, image=imgSS91, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        for i in range(4):
                            a1d = random.randint(1,700)#02161221#hs 1,1100
                            b1d = random.randint(200,600)#02161221#hs 100,600
                            canvas.create_image(a1d, b1d, image=imgSS90, tags = "img1")
                            canvas.place(x=100, y=100)
                            canvas.pack()
                        a50c = random.randint(1,700)#02161221#hs 1,1100
                        b50c = random.randint(200,600)#02161221#hs 100,600
                        canvas.create_image(a50c, b50c, image=imgSS89, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        for i in range(4):
                            a10c = random.randint(1,700)#02161221#hs 1,1100
                            b10c = random.randint(200,600)#02161221#hs100,600
                            canvas.create_image(a10c, b10c, image=imgSS88, tags = "img1")
                            canvas.place(x=100, y=100)
                            canvas.pack()
                        a5c = random.randint(1,700)#02161221#hs 1,1100
                        b5c = random.randint(200,600)#02161221#hs100,600
                        canvas.create_image(a5c, b5c, image=imgSS87, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        for i in range(4):
                            a1c = random.randint(1,700)#02161221#hs 1,1100
                            b1c = random.randint(200,600)#02161221#hs100,600
                            canvas.create_image(a1c, b1c, image=imgSS86, tags = "img1")
                            canvas.place(x=100, y=100)
                            canvas.pack()
                    
                    
                    zm2button.place(x=860, y=100)#02161222
                    
                    existA = 100
                elif existA == 100000:
                    k3once = 18
                else:
                    existA = 100
            elif k3once == 9:
                mojiF.pack_forget()
                mojiT.pack_forget()
                emojiT.pack_forget()
                
                
                if hint == 1:
                    tagX = []
                    anahint(numM3)
                    if tigau == 1:
                        tgbutton.place(x = 130, y = 210)#02161225
    #                     hint = 1
                    else:
                        tgbutton.place_forget()
                
                
                if existA == 100:
                    existA = 300
                    hnbutton.place_forget()
                    zm1button.place_forget()
                    zm2button.place_forget()
                    zm3button.place_forget()
                    zm4button.place_forget()
                    zm5button.place_forget()
                    
                    if zahyohn3 == 1:
                        hnbutton['text'] = "Q2正解"
                        hnbutton.place(x = 5, y = 250)#02161226
                        play()
                        
                        canvas.create_image(630, 300, image=imgSS106)#02161225
                    #250, 300, image=imgSS106
        
                        canvas.place(x=250, y=300)
                        canvas.pack()
                        
                    elif zahyohn3 == 2:
                        existA = 100000
                        
                        
                        canvas.create_image(630, 300, image=imgSS107)#02161225
                #250, 300, image=imgSS107
                        canvas.place(x=250, y=300)
                        canvas.pack()
                        
                    else:
    
                        canvas.create_image(630, 300, image=imgSS108)#02161225
            #250, 300, image=imgSS108#
                        canvas.place(x=250, y=300)
                        canvas.pack()
                        existA = 100000#長らく封印してたが1224に解除
                    
                elif existA == 300:
                    canvas.delete("all")
                    
                    
                    if hint == 1:
                        tagX = []
                        ahint(numM3)
                        
                        if tigau == 1:
                            tgbutton.place(x = 130, y = 210)#02161225
        #x = 5, y = 210
                        else:
                            tgbutton.place_forget()
    
                    mojiTn.pack_forget()
                    mojiTd.pack_forget()
                    mojiTg.pack_forget()
                    emojiTn.pack_forget()
                
                    
                    if gengo == 2:
                        mojiTg = tk.Text(height=1, width=62, wrap="none")#02161222
                    #変更width=25
                        mojiTg.tag_configure("f", foreground="#FF0100")
                        mojiTg.tag_configure("r", foreground="#000000")
                        mojiTg.tag_configure("g", foreground="#FF0000")
                        mojiTg.tag_configure("b", foreground="#000000")
    #                     mojiTn.insert("end", "次‼", 'f')
                        mojiTg.insert("end", "                               トレーに", 'r')#02161222
            #変更半角スペース開ける
                        mojiTg.insert("end", str(numM3/100), 'g')
                        mojiTg.insert("end", "元ピッタリはらって!", 'b')
                        mojiTg.configure(state="disabled") # 読取専用に
                        mojiTg.pack(anchor='n',expand=1)
                    elif gengo == 3:
                        mojiTd = tk.Text(height=1, width=62, wrap="none")#02161222
                        #変更
                        mojiTd.tag_configure("f", foreground="#FF0100")
                        mojiTd.tag_configure("r", foreground="#000000")
                        mojiTd.tag_configure("g", foreground="#FF0000")
                        mojiTd.tag_configure("b", foreground="#000000")
    #                     mojiTn.insert("end", "次‼", 'f')
                        mojiTd.insert("end", "　　　　　　　　　　トレーに", 'r')#02161222
            #変更半角スペース開ける
                        mojiTd.insert("end", str(numM3*100), 'g')
                        mojiTd.insert("end", "ドンピッタリはらって!", 'b')
                        mojiTd.configure(state="disabled") # 読取専用に
                        mojiTd.pack(anchor='n',expand=1)
                    elif gengo == 1:                        
                        mojiTn = tk.Text(height=1, width=62, wrap="none")#02161222
                        #変更
                        mojiTn.tag_configure("f", foreground="#FF0100")
                        mojiTn.tag_configure("r", foreground="#000000")
                        mojiTn.tag_configure("g", foreground="#FF0000")
                        mojiTn.tag_configure("b", foreground="#000000")
    #                     mojiTn.insert("end", "次‼", 'f')
                        mojiTn.insert("end","　　　　　　　　　　　トレーに", 'r')#02161221
            #変更半角スペース開ける
                        mojiTn.insert("end", str(numM3), 'g')
                        mojiTn.insert("end", "円ピッタリはらって!", 'b')
                        mojiTn.configure(state="disabled") # 読取専用に
                        mojiTn.pack(anchor='n',expand=1)
                    else:
                        emojiTn = tk.Text(height=1, width=62, wrap="none")#02161223
                        emojiTn.tag_configure("r", foreground="#000000")
                        emojiTn.tag_configure("g", foreground="#FF0000")
                        emojiTn.tag_configure("b", foreground="#000000")
                        emojiTn.insert("end", "　　　　　　　　　　　　2つの商品の", 'r')#02161223
    
                        emojiTn.insert("end", "合計額を", 'g')
                        emojiTn.insert("end", "ピッタリはらって!", 'b')
                        emojiTn.configure(state="disabled")
                        emojiTn.pack(anchor='n',expand=1)
                        
                        canvas.create_image(50, 50, image=imgME)#02161225
        #50, 165, image=imgME#
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(210, 50, image=imgMF)#02161225
        #210, 165, image=imgMF
                        canvas.place(x=100, y=100)
                        canvas.pack()
            
            
                        canvas.create_image(130, 50, image=imgSS109, tags = "mig")#02160125)
        
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        #290, 165, image=imgSS115
                        canvas.create_image(290, 50, image=imgSS115, tags = "mig")#02160125)
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(370, 60, image=imgSS116)#02161225
                        #370, 165, image=imgSS116#
                        canvas.place(x=100, y=100)
                        canvas.pack()                                                
            
                    canvas.create_image(650, 100, image=imgSS96)#02161222
                    #変更250
                    canvas.place(x=150, y=150)
                    canvas.pack()
    
                    #0206
                    stockX = []
                    stockY = []
                    a1man = random.randint(10,800)
                    stockX.append(a1man)
                    b1man = random.randint(250,650)
                    stockY.append(b1man)
                    singi = True
                    while singi:
                        signal = "yes"
                        a5000 = random.randint(10,800)
                        for you in range(len(stockX)):                            
                            if stockX[you]+30 >= a5000 >= stockX[you]-30:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockX.append(a5000)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        b5000 = random.randint(250,650)
                        for you in range(len(stockY)):                            
                            if stockY[you]+10 >= b5000 >= stockY[you]-10:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockY.append(b5000)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        a500 = random.randint(10,800)
                        for you in range(len(stockX)):                            
                            if stockX[you]+30 >= a500 >= stockX[you]-30:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockX.append(a500)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        b500 = random.randint(250,650)
                        for you in range(len(stockY)):                            
                            if stockY[you]+10 >= b500 >= stockY[you]-10:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockY.append(b500)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        a50 = random.randint(10,800)
                        for you in range(len(stockX)):                            
                            if stockX[you]+30 >= a50 >= stockX[you]-30:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockX.append(a50)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        b50 = random.randint(250,650)
                        for you in range(len(stockY)):                            
                            if stockY[you]+10 >= b50 >= stockY[you]-10:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockY.append(b50)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        a5en = random.randint(10,800)
                        for you in range(len(stockX)):                            
                            if stockX[you]+30 >= a5en >= stockX[you]-30:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockX.append(a5en)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        b5en = random.randint(250,650)
                        for you in range(len(stockY)):                            
                            if stockY[you]+10 >= b5en >= stockY[you]-10:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockY.append(b5en)
                            singi = False
                    singi = True
                    for me in range(4):
                        singi = True
                        while singi:
                            signal = "yes"
                            a1000 = random.randint(10,800)
                            for you in range(len(stockX)):                            
                                if stockX[you]+30 >= a1000 >= stockX[you]-30:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockX.append(a1000)
                                singi = False
                        singi = True
                        while singi:
                            signal = "yes"
                            b1000 = random.randint(250,650)
                            for you in range(len(stockY)):                            
                                if stockY[you]+10 >= b1000 >= stockY[you]-10:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockY.append(b1000)
                                singi = False                                
                        canvas.create_image(a1000, b1000, image=imgSS7, tags = "img3")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    for me in range(4):
                        singi = True
                        while singi:
                            signal = "yes"
                            a100 = random.randint(10,800)
                            for you in range(len(stockX)):                            
                                if stockX[you]+20 >= a100 >= stockX[you]-20:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockX.append(a100)
                                singi = False
                        singi = True
                        while singi:
                            signal = "yes"
                            b100 = random.randint(250,650)
                            for you in range(len(stockY)):                            
                                if stockY[you]+10 >= b100 >= stockY[you]-10:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockY.append(b100)
                                singi = False                                
                        canvas.create_image(a100, b100, image=imgSS8, tags = "img5")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    for me in range(4):
                        singi = True
                        while singi:
                            signal = "yes"
                            a10 = random.randint(10,800)
                            for you in range(len(stockX)):                            
                                if stockX[you]+20 >= a10 >= stockX[you]-20:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockX.append(a10)
                                singi = False
                        singi = True
                        while singi:
                            signal = "yes"
                            b10 = random.randint(250,650)
                            for you in range(len(stockY)):                            
                                if stockY[you]+10 >= b10 >= stockY[you]-10:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockY.append(b10)
                                singi = False                                
                        canvas.create_image(a10, b10, image=imgSS9, tags = "img7")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    for me in range(4):
                        singi = True
                        while singi:
                            signal = "yes"
                            a1en = random.randint(10,800)
                            for you in range(len(stockX)):                            
                                if stockX[you]+20 >= a1en >= stockX[you]-20:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockX.append(a1en)
                                singi = False
                        singi = True
                        while singi:
                            signal = "yes"
                            b1en = random.randint(250,650)
                            for you in range(len(stockY)):                            
                                if stockY[you]+10 >= b1en >= stockY[you]-10:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockY.append(b1en)
                                singi = False                                
                        canvas.create_image(a1en, b1en, image=imgSS10, tags = "img9")
                        canvas.place(x=100, y=100)
                        canvas.pack()
    
                    for iv in range(1):#02161226
                        canvas.create_image(a1man, b1man, image=imgSS6, tags = "img")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(a5000, b5000, image=imgSS2, tags = "img2")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(a500, b500, image=imgSS3, tags = "img4")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(a50, b50, image=imgSS4, tags = "img6")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(a5en, b5en, image=imgSS5, tags = "img8")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    if zaq == 1:#02161226 tamesini zaqzaq mode 1set
    
                        a100d = random.randint(1,700)#02161221#hs 1,1100
                        b100d = random.randint(200,600)#02161221#hs 100,600
                        canvas.create_image(a100d, b100d, image=imgSS94, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        a50d = random.randint(1,700)#02161221#hs 1,1100
                        b50d = random.randint(200,600)#02161221#hs 100,600
                        canvas.create_image(a50d, b50d, image=imgSS93, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        for i in range(4):
                            a10d = random.randint(1,700)#02161221#hs 1,1100
                            b10d = random.randint(200,600)#02161221#hs 100,600
                            canvas.create_image(a10d, b10d, image=imgSS92, tags = "img1")
                            canvas.place(x=100, y=100)
                            canvas.pack()
                        a5d = random.randint(1,700)#02161221#hs 1,1100
                        b5d = random.randint(200,600)#02161221#hs 100,600
                        canvas.create_image(a5d, b5d, image=imgSS91, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        for i in range(4):
                            a1d = random.randint(1,700)#02161221#hs 1,1100
                            b1d = random.randint(200,600)#02161221#hs 100,600
                            canvas.create_image(a1d, b1d, image=imgSS90, tags = "img1")
                            canvas.place(x=100, y=100)
                            canvas.pack()
                        a50c = random.randint(1,700)#02161221#hs 1,1100
                        b50c = random.randint(200,600)#02161221#hs 100,600
                        canvas.create_image(a50c, b50c, image=imgSS89, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        for i in range(4):
                            a10c = random.randint(1,700)#02161221#hs 1,1100
                            b10c = random.randint(200,600)#02161221#hs100,600
                            canvas.create_image(a10c, b10c, image=imgSS88, tags = "img1")
                            canvas.place(x=100, y=100)
                            canvas.pack()
                        a5c = random.randint(1,700)#02161221#hs 1,1100
                        b5c = random.randint(200,600)#02161221#hs100,600
                        canvas.create_image(a5c, b5c, image=imgSS87, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        for i in range(4):
                            a1c = random.randint(1,700)#02161221#hs 1,1100
                            b1c = random.randint(200,600)#02161221#hs100,600
                            canvas.create_image(a1c, b1c, image=imgSS86, tags = "img1")
                            canvas.place(x=100, y=100)
                            canvas.pack()
                                        
                    zm3button.place(x=860, y=100)#02161222
                    
                    existA = 1000
                elif existA == 100000:
                    k3once = 18
                else:
                    existA = 1000
        
            elif k3once == 12:
                mojiF.pack_forget()
                mojiT.pack_forget()
                emojiT.pack_forget()
                
                
                if hint == 1:
                    tagX = []
                    anahint(numM4)
                    if tigau == 1:
                        tgbutton.place(x = 130, y = 210)#02161225
        
    #                     hint = 1
                    else:
                        tgbutton.place_forget()
                
                
                if existA == 1000:
                    existA = 3000
                    hnbutton.place_forget()
                    zm1button.place_forget()
                    zm2button.place_forget()
                    zm3button.place_forget()
                    zm4button.place_forget()
                    zm5button.place_forget()
                    
                    if zahyohn4 == 1:
                        hnbutton['text'] = "Q3正解"
                        hnbutton.place(x = 5, y = 250)#02161226
                        play5()
                        
                        canvas.create_image(630, 300, image=imgSS106)#02161225
                    #250, 300, image=imgSS106
                        canvas.place(x=250, y=300)
                        canvas.pack()
                        
                    elif zahyohn4 == 2:
                        existA = 100000
                        
                        canvas.create_image(630, 300, image=imgSS107)#02161225
            #250, 300, image=imgSS107
                        canvas.place(x=250, y=300)
                        canvas.pack()                        
                        
                    else:
                
                        canvas.create_image(630, 300, image=imgSS108)#02161225
                #250, 300, image=imgSS108
                        canvas.place(x=250, y=300)
                        canvas.pack()
                        
                        existA = 100000#長らく封印してたが1224に解除
                    
                elif existA == 3000:
                    canvas.delete("all")
                    
                    if hint == 1:
                        tagX = []
                        ahint(numM4)
                        
                        if tigau == 1:
                            tgbutton.place(x = 130, y = 210)#02161225
        #x = 5, y = 210
                        else:
                            tgbutton.place_forget()
                    
    
                    mojiTn.pack_forget()
                    mojiTd.pack_forget()
                    mojiTg.pack_forget()
                    emojiTn.pack_forget()
                
                        
                    if gengo == 2:
                        mojiTg = tk.Text(height=1, width=62, wrap="none")#02161222
                        #変更width=25
                        mojiTg.tag_configure("f", foreground="#FF0100")
                        mojiTg.tag_configure("r", foreground="#000000")
                        mojiTg.tag_configure("g", foreground="#FF0000")
                        mojiTg.tag_configure("b", foreground="#000000")#02161222？？？　何か入ってた
    #                     mojiTn.insert("end", "次‼", 'f')
                        mojiTg.insert("end","　　　　　　　　　　　トレーに", 'r')#02161222
            #変更半角スペースあける
                        mojiTg.insert("end", str(numM4/100), 'g')
                        mojiTg.insert("end", "元ピッタリはらって!", 'b')
                        mojiTg.configure(state="disabled") # 読取専用に
                        mojiTg.pack(anchor='n',expand=1)
                    elif gengo == 3:
                        mojiTd = tk.Text(height=1, width=62, wrap="none")#02161222
                        #変更width=25
                        mojiTd.tag_configure("f", foreground="#FF0100")
                        mojiTd.tag_configure("r", foreground="#000000")
                        mojiTd.tag_configure("g", foreground="#FF0000")
                        mojiTd.tag_configure("b", foreground="#000000")
    #                     mojiTn.insert("end", "次‼", 'f')
                        mojiTd.insert("end","　　　　　　　　　　　トレーに", 'r')#02161222
            #変更半角スペースあける
                        mojiTd.insert("end", str(numM4*100), 'g')
                        mojiTd.insert("end", "ドンピッタリはらって!", 'b')
                        mojiTd.configure(state="disabled") # 読取専用に
                        mojiTd.pack(anchor='n',expand=1)
                    elif gengo == 1:                        
                        mojiTn = tk.Text(height=1, width=62, wrap="none")#02161222
                        #変更width=25
                        mojiTn.tag_configure("f", foreground="#FF0100")
                        mojiTn.tag_configure("r", foreground="#000000")
                        mojiTn.tag_configure("g", foreground="#FF0000")
                        mojiTn.tag_configure("b", foreground="#000000")
    #                     mojiTn.insert("end", "次‼", 'f')
                        mojiTn.insert("end","　　　　　　　　　　　トレーに", 'r')#02161222
            #変更半角スペースあける
                        mojiTn.insert("end", str(numM4), 'g')
                        mojiTn.insert("end", "円ピッタリはらって!", 'b')
                        mojiTn.configure(state="disabled") # 読取専用に
                        mojiTn.pack(anchor='n',expand=1)
                    else:
                        emojiTn = tk.Text(height=1, width=62, wrap="none")#02161223
                        emojiTn.tag_configure("r", foreground="#000000")
                        emojiTn.tag_configure("g", foreground="#FF0000")
                        emojiTn.tag_configure("b", foreground="#000000")
                        emojiTn.insert("end", "　　　　　　　　　　　　2つの商品の", 'r')#02161223
    
                        emojiTn.insert("end", "合計額を", 'g')
                        emojiTn.insert("end", "ピッタリはらって!", 'b')
                        emojiTn.configure(state="disabled")
                        emojiTn.pack(anchor='n',expand=1)
                        
                        canvas.create_image(50, 50, image=imgMG)#02161225
        #50, 50, image=imgMG
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(210,50, image=imgMH)#02161225
        #210, 165, image=imgMH#
                        canvas.place(x=100, y=100)
                        canvas.pack()
            
                        canvas.create_image(130, 50, image=imgSS109, tags = "mig")#02160125)
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        #290, 165, image=imgSS115
                        canvas.create_image(290, 50, image=imgSS115, tags = "mig")#02160125)
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(370, 60, image=imgSS116)#02161225
                        #370, 165, image=imgSS116
                        canvas.place(x=100, y=100)
                        canvas.pack()                                                
                        
        
                    canvas.create_image(650, 100, image=imgSS96)#02161222
                    canvas.place(x=150, y=150)
                    canvas.pack()
            
        
                    #0206
                    stockX = []
                    stockY = []
                    a1man = random.randint(10,800)
                    stockX.append(a1man)
                    b1man = random.randint(250,650)
                    stockY.append(b1man)
                    singi = True
                    while singi:
                        signal = "yes"
                        a5000 = random.randint(10,800)
                        for you in range(len(stockX)):                            
                            if stockX[you]+30 >= a5000 >= stockX[you]-30:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockX.append(a5000)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        b5000 = random.randint(250,650)
                        for you in range(len(stockY)):                            
                            if stockY[you]+10 >= b5000 >= stockY[you]-10:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockY.append(b5000)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        a500 = random.randint(10,800)
                        for you in range(len(stockX)):                            
                            if stockX[you]+30 >= a500 >= stockX[you]-30:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockX.append(a500)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        b500 = random.randint(250,650)
                        for you in range(len(stockY)):                            
                            if stockY[you]+10 >= b500 >= stockY[you]-10:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockY.append(b500)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        a50 = random.randint(10,800)
                        for you in range(len(stockX)):                            
                            if stockX[you]+30 >= a50 >= stockX[you]-30:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockX.append(a50)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        b50 = random.randint(250,650)
                        for you in range(len(stockY)):                            
                            if stockY[you]+10 >= b50 >= stockY[you]-10:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockY.append(b50)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        a5en = random.randint(10,800)
                        for you in range(len(stockX)):                            
                            if stockX[you]+30 >= a5en >= stockX[you]-30:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockX.append(a5en)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        b5en = random.randint(250,650)
                        for you in range(len(stockY)):                            
                            if stockY[you]+10 >= b5en >= stockY[you]-10:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockY.append(b5en)
                            singi = False
                    singi = True
                    for me in range(4):
                        singi = True
                        while singi:
                            signal = "yes"
                            a1000 = random.randint(10,800)
                            for you in range(len(stockX)):                            
                                if stockX[you]+30 >= a1000 >= stockX[you]-30:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockX.append(a1000)
                                singi = False
                        singi = True
                        while singi:
                            signal = "yes"
                            b1000 = random.randint(250,650)
                            for you in range(len(stockY)):                            
                                if stockY[you]+10 >= b1000 >= stockY[you]-10:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockY.append(b1000)
                                singi = False                                
                        canvas.create_image(a1000, b1000, image=imgSS7, tags = "img3")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    for me in range(4):
                        singi = True
                        while singi:
                            signal = "yes"
                            a100 = random.randint(10,800)
                            for you in range(len(stockX)):                            
                                if stockX[you]+20 >= a100 >= stockX[you]-20:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockX.append(a100)
                                singi = False
                        singi = True
                        while singi:
                            signal = "yes"
                            b100 = random.randint(250,650)
                            for you in range(len(stockY)):                            
                                if stockY[you]+10 >= b100 >= stockY[you]-10:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockY.append(b100)
                                singi = False                                
                        canvas.create_image(a100, b100, image=imgSS8, tags = "img5")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    for me in range(4):
                        singi = True
                        while singi:
                            signal = "yes"
                            a10 = random.randint(10,800)
                            for you in range(len(stockX)):                            
                                if stockX[you]+20 >= a10 >= stockX[you]-20:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockX.append(a10)
                                singi = False
                        singi = True
                        while singi:
                            signal = "yes"
                            b10 = random.randint(250,650)
                            for you in range(len(stockY)):                            
                                if stockY[you]+10 >= b10 >= stockY[you]-10:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockY.append(b10)
                                singi = False                                
                        canvas.create_image(a10, b10, image=imgSS9, tags = "img7")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    for me in range(4):
                        singi = True
                        while singi:
                            signal = "yes"
                            a1en = random.randint(10,800)
                            for you in range(len(stockX)):                            
                                if stockX[you]+20 >= a1en >= stockX[you]-20:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockX.append(a1en)
                                singi = False
                        singi = True
                        while singi:
                            signal = "yes"
                            b1en = random.randint(250,650)
                            for you in range(len(stockY)):                            
                                if stockY[you]+10 >= b1en >= stockY[you]-10:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockY.append(b1en)
                                singi = False                                
                        canvas.create_image(a1en, b1en, image=imgSS10, tags = "img9")
                        canvas.place(x=100, y=100)
                        canvas.pack()
        
                    for vi in range(1):#02161226
                        canvas.create_image(a1man, b1man, image=imgSS6, tags = "img")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(a5000, b5000, image=imgSS2, tags = "img2")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(a500, b500, image=imgSS3, tags = "img4")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(a50, b50, image=imgSS4, tags = "img6")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(a5en, b5en, image=imgSS5, tags = "img8")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    if zaq == 1:#02161226 tamesini zaqzaq mode 1set
    
                        a100d = random.randint(1,700)#02161221#hs 1,1100
                        b100d = random.randint(200,600)#02161221#hs 100,600
                        canvas.create_image(a100d, b100d, image=imgSS94, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        a50d = random.randint(1,700)#02161221#hs 1,1100
                        b50d = random.randint(200,600)#02161221#hs 100,600
                        canvas.create_image(a50d, b50d, image=imgSS93, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        for i in range(4):
                            a10d = random.randint(1,700)#02161221#hs 1,1100
                            b10d = random.randint(200,600)#02161221#hs 100,600
                            canvas.create_image(a10d, b10d, image=imgSS92, tags = "img1")
                            canvas.place(x=100, y=100)
                            canvas.pack()
                        a5d = random.randint(1,700)#02161221#hs 1,1100
                        b5d = random.randint(200,600)#02161221#hs 100,600
                        canvas.create_image(a5d, b5d, image=imgSS91, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        for i in range(4):
                            a1d = random.randint(1,700)#02161221#hs 1,1100
                            b1d = random.randint(200,600)#02161221#hs 100,600
                            canvas.create_image(a1d, b1d, image=imgSS90, tags = "img1")
                            canvas.place(x=100, y=100)
                            canvas.pack()
                        a50c = random.randint(1,700)#02161221#hs 1,1100
                        b50c = random.randint(200,600)#02161221#hs 100,600
                        canvas.create_image(a50c, b50c, image=imgSS89, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        for i in range(4):
                            a10c = random.randint(1,700)#02161221#hs 1,1100
                            b10c = random.randint(200,600)#02161221#hs100,600
                            canvas.create_image(a10c, b10c, image=imgSS88, tags = "img1")
                            canvas.place(x=100, y=100)
                            canvas.pack()
                        a5c = random.randint(1,700)#02161221#hs 1,1100
                        b5c = random.randint(200,600)#02161221#hs100,600
                        canvas.create_image(a5c, b5c, image=imgSS87, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        for i in range(4):
                            a1c = random.randint(1,700)#02161221#hs 1,1100
                            b1c = random.randint(200,600)#02161221#hs100,600
                            canvas.create_image(a1c, b1c, image=imgSS86, tags = "img1")
                            canvas.place(x=100, y=100)
                            canvas.pack()
                    zm4button.place(x=860, y=100)#02161222
                    
                    
                    existA = 10000
                elif existA == 100000:
                    k3once = 18
                else:
                    existA = 10000
            
            elif k3once == 15:
                mojiF.pack_forget()
                mojiT.pack_forget()
                emojiT.pack_forget()
                
                if hint == 1:
                    tagX = []
                    anahint(numM5)
                    if tigau == 1:
                        tgbutton.place(x = 130, y = 210)#02161225
                    else:
                        tgbutton.place_forget()
                
                if existA == 10000:
                    existA = 30000
                    hnbutton.place_forget()
                    zm1button.place_forget()
                    zm2button.place_forget()
                    zm3button.place_forget()
                    zm4button.place_forget()
                    zm5button.place_forget()
                    
                    if zahyohn5 == 1:
                        hnbutton['text'] = "Q4正解"
                        hnbutton.place(x = 5, y = 250)#02161226
                        play5()
                        
                        canvas.create_image(630, 300, image=imgSS106)#02161225
                    #250, 300, image=imgSS106
                        canvas.place(x=250, y=300)
                        canvas.pack()
                        
                        
                    elif zahyohn5 == 2:
                        existA = 100000
                        
                        canvas.create_image(630, 300, image=imgSS107)#02161225
            #250, 300, image=imgSS107
                        canvas.place(x=250, y=300)
                        canvas.pack()
                    else:
                        canvas.create_image(630, 300, image=imgSS108)#02161225
                #250, 300, image=imgSS108
                        canvas.place(x=250, y=300)
                        canvas.pack()
                    
                        existA = 100000#長らく封印してたが1224に解除
                    
                elif existA == 30000:
                    canvas.delete("all")
                    
                    if hint == 1:
                        tagX = []
                        ahint(numM5)
                        
                        if tigau == 1:
                            tgbutton.place(x = 130, y = 210)#02161225
        #x = 5, y = 210
                        else:
                            tgbutton.place_forget()
     
                    mojiTn.pack_forget()
                    mojiTd.pack_forget()
                    mojiTg.pack_forget()
                    emojiTn.pack_forget()
                        
                    if gengo == 2:
                        mojiTg = tk.Text(height=1, width=62, wrap="none")#02161222
                        #width=25
                        mojiTg.tag_configure("f", foreground="#FF0100")
                        mojiTg.tag_configure("r", foreground="#000000")
                        mojiTg.tag_configure("g", foreground="#FF0000")
                        mojiTg.tag_configure("b", foreground="#000000")
    #                     mojiTn.insert("end", "次‼", 'f')
                        mojiTg.insert("end","　　　　　　　　　　　トレーに", 'r')#02161222
            #変更半角スペースあける
                        mojiTg.insert("end", str(numM5/100), 'g')
                        mojiTg.insert("end", "元ピッタリはらって!", 'b')
                        mojiTg.configure(state="disabled") # 読取専用に
                        mojiTg.pack(anchor='n',expand=1)
                    elif gengo == 3:
                        mojiTd = tk.Text(height=1, width=62, wrap="none")#02161222
                        #width=25
                        mojiTd.tag_configure("f", foreground="#FF0100")
                        mojiTd.tag_configure("r", foreground="#000000")
                        mojiTd.tag_configure("g", foreground="#FF0000")
                        mojiTd.tag_configure("b", foreground="#000000")
    #                     mojiTn.insert("end", "次‼", 'f')
                        mojiTd.insert("end","　　　　　　　　　　　トレーに", 'r')#02161222
            #変更半角スペースあける
                        mojiTd.insert("end", str(numM5*100), 'g')
                        mojiTd.insert("end", "ドンピッタリはらって!", 'b')
                        mojiTd.configure(state="disabled") # 読取専用に
                        mojiTd.pack(anchor='n',expand=1)
                    elif gengo == 1:                        
                        mojiTn = tk.Text(height=1, width=62, wrap="none")#02161222
                        #width=25
                        mojiTn.tag_configure("f", foreground="#FF0100")
                        mojiTn.tag_configure("r", foreground="#000000")
                        mojiTn.tag_configure("g", foreground="#FF0000")
                        mojiTn.tag_configure("b", foreground="#000000")
    #                     mojiTn.insert("end", "次‼", 'f')
                        mojiTn.insert("end","　　　　　　　　　　　トレーに", 'r')#02161222
            #変更半角スペースあける
                        mojiTn.insert("end", str(numM5), 'g')
                        mojiTn.insert("end", "円ピッタリはらって!", 'b')
                        mojiTn.configure(state="disabled") # 読取専用に
                        mojiTn.pack(anchor='n',expand=1)
                    else:
                        emojiTn = tk.Text(height=1, width=62, wrap="none")#02161223
                        emojiTn.tag_configure("r", foreground="#000000")
                        emojiTn.tag_configure("g", foreground="#FF0000")
                        emojiTn.tag_configure("b", foreground="#000000")
                        emojiTn.insert("end", "　　　　　　　　　　　　2つの商品の", 'r')#02161223
    
                        emojiTn.insert("end", "合計額を", 'g')
                        emojiTn.insert("end", "ピッタリはらって!", 'b')
                        emojiTn.configure(state="disabled")
                        emojiTn.pack(anchor='n',expand=1)
                        
                        canvas.create_image(50, 50, image=imgMI)#02161225
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(210, 50, image=imgMJ)#02161225
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(130, 50, image=imgSS109, tags = "mig")#02160125)
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(290, 50, image=imgSS115, tags = "mig")#02160125)
                        
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(370, 60, image=imgSS116)#02161225
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        
                        flag += 1
                    canvas.create_image(650, 100, image=imgSS96)#02161222
                    canvas.place(x=150, y=150)
                    canvas.pack()
                    
                    #0206
                    stockX = []
                    stockY = []
                    a1man = random.randint(10,800)
                    stockX.append(a1man)
                    b1man = random.randint(250,650)
                    stockY.append(b1man)
                    singi = True
                    while singi:
                        signal = "yes"
                        a5000 = random.randint(10,800)
                        for you in range(len(stockX)):                            
                            if stockX[you]+30 >= a5000 >= stockX[you]-30:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockX.append(a5000)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        b5000 = random.randint(250,650)
                        for you in range(len(stockY)):                            
                            if stockY[you]+10 >= b5000 >= stockY[you]-10:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockY.append(b5000)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        a500 = random.randint(10,800)
                        for you in range(len(stockX)):                            
                            if stockX[you]+30 >= a500 >= stockX[you]-30:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockX.append(a500)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        b500 = random.randint(250,650)
                        for you in range(len(stockY)):                            
                            if stockY[you]+10 >= b500 >= stockY[you]-10:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockY.append(b500)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        a50 = random.randint(10,800)
                        for you in range(len(stockX)):                            
                            if stockX[you]+30 >= a50 >= stockX[you]-30:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockX.append(a50)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        b50 = random.randint(250,650)
                        for you in range(len(stockY)):                            
                            if stockY[you]+10 >= b50 >= stockY[you]-10:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockY.append(b50)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        a5en = random.randint(10,800)
                        for you in range(len(stockX)):                            
                            if stockX[you]+30 >= a5en >= stockX[you]-30:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockX.append(a5en)
                            singi = False
                    singi = True
                    while singi:
                        signal = "yes"
                        b5en = random.randint(250,650)
                        for you in range(len(stockY)):                            
                            if stockY[you]+10 >= b5en >= stockY[you]-10:
                                signal = "no"
                            else:
                                pass
                        if signal == "no":
                            singi = True
                        else:
                            stockY.append(b5en)
                            singi = False
                    singi = True
                    for me in range(4):
                        singi = True
                        while singi:
                            signal = "yes"
                            a1000 = random.randint(10,800)
                            for you in range(len(stockX)):                            
                                if stockX[you]+30 >= a1000 >= stockX[you]-30:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockX.append(a1000)
                                singi = False
                        singi = True
                        while singi:
                            signal = "yes"
                            b1000 = random.randint(250,650)
                            for you in range(len(stockY)):                            
                                if stockY[you]+10 >= b1000 >= stockY[you]-10:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockY.append(b1000)
                                singi = False                                
                        canvas.create_image(a1000, b1000, image=imgSS7, tags = "img3")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    for me in range(4):
                        singi = True
                        while singi:
                            signal = "yes"
                            a100 = random.randint(10,800)
                            for you in range(len(stockX)):                            
                                if stockX[you]+20 >= a100 >= stockX[you]-20:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockX.append(a100)
                                singi = False
                        singi = True
                        while singi:
                            signal = "yes"
                            b100 = random.randint(250,650)
                            for you in range(len(stockY)):                            
                                if stockY[you]+10 >= b100 >= stockY[you]-10:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockY.append(b100)
                                singi = False                                
                        canvas.create_image(a100, b100, image=imgSS8, tags = "img5")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    for me in range(4):
                        singi = True
                        while singi:
                            signal = "yes"
                            a10 = random.randint(10,800)
                            for you in range(len(stockX)):                            
                                if stockX[you]+20 >= a10 >= stockX[you]-20:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockX.append(a10)
                                singi = False
                        singi = True
                        while singi:
                            signal = "yes"
                            b10 = random.randint(250,650)
                            for you in range(len(stockY)):                            
                                if stockY[you]+10 >= b10 >= stockY[you]-10:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockY.append(b10)
                                singi = False                                
                        canvas.create_image(a10, b10, image=imgSS9, tags = "img7")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    for me in range(4):
                        singi = True
                        while singi:
                            signal = "yes"
                            a1en = random.randint(10,800)
                            for you in range(len(stockX)):                            
                                if stockX[you]+20 >= a1en >= stockX[you]-20:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockX.append(a1en)
                                singi = False
                        singi = True
                        while singi:
                            signal = "yes"
                            b1en = random.randint(250,650)
                            for you in range(len(stockY)):                            
                                if stockY[you]+10 >= b1en >= stockY[you]-10:
                                    signal = "no"
                                else:
                                    pass
                            if signal == "no":
                                singi = True
                            else:
                                stockY.append(b1en)
                                singi = False                                
                        canvas.create_image(a1en, b1en, image=imgSS10, tags = "img9")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    
                    for vii in range(1):#02161226
                        canvas.create_image(a1man, b1man, image=imgSS6, tags = "img")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(a5000, b5000, image=imgSS2, tags = "img2")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(a500, b500, image=imgSS3, tags = "img4")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(a50, b50, image=imgSS4, tags = "img6")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        canvas.create_image(a5en, b5en, image=imgSS5, tags = "img8")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                    if zaq == 1:#02161226 tamesini zaqzaq mode 1set
    
                        a100d = random.randint(1,700)#02161221#hs 1,1100
                        b100d = random.randint(200,600)#02161221#hs 100,600
                        canvas.create_image(a100d, b100d, image=imgSS94, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        a50d = random.randint(1,700)#02161221#hs 1,1100
                        b50d = random.randint(200,600)#02161221#hs 100,600
                        canvas.create_image(a50d, b50d, image=imgSS93, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        for i in range(4):
                            a10d = random.randint(1,700)#02161221#hs 1,1100
                            b10d = random.randint(200,600)#02161221#hs 100,600
                            canvas.create_image(a10d, b10d, image=imgSS92, tags = "img1")
                            canvas.place(x=100, y=100)
                            canvas.pack()
                        a5d = random.randint(1,700)#02161221#hs 1,1100
                        b5d = random.randint(200,600)#02161221#hs 100,600
                        canvas.create_image(a5d, b5d, image=imgSS91, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        for i in range(4):
                            a1d = random.randint(1,700)#02161221#hs 1,1100
                            b1d = random.randint(200,600)#02161221#hs 100,600
                            canvas.create_image(a1d, b1d, image=imgSS90, tags = "img1")
                            canvas.place(x=100, y=100)
                            canvas.pack()
                        a50c = random.randint(1,700)#02161221#hs 1,1100
                        b50c = random.randint(200,600)#02161221#hs 100,600
                        canvas.create_image(a50c, b50c, image=imgSS89, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        for i in range(4):
                            a10c = random.randint(1,700)#02161221#hs 1,1100
                            b10c = random.randint(200,600)#02161221#hs100,600
                            canvas.create_image(a10c, b10c, image=imgSS88, tags = "img1")
                            canvas.place(x=100, y=100)
                            canvas.pack()
                        a5c = random.randint(1,700)#02161221#hs 1,1100
                        b5c = random.randint(200,600)#02161221#hs100,600
                        canvas.create_image(a5c, b5c, image=imgSS87, tags = "img1")
                        canvas.place(x=100, y=100)
                        canvas.pack()
                        for i in range(4):
                            a1c = random.randint(1,700)#02161221#hs 1,1100
                            b1c = random.randint(200,600)#02161221#hs100,600
                            canvas.create_image(a1c, b1c, image=imgSS86, tags = "img1")
                            canvas.place(x=100, y=100)
                            canvas.pack()
                    
                        
                    zm5button.place(x=860, y=100)#02161222
                    
                    existA = 100000
                elif existA == 100000:
                    pass
                else:
                    existA = 100000
            
            elif k3once == 18:
                mojiF.pack_forget()
                mojiT.pack_forget()
                emojiT.pack_forget()
                mojiTn.pack_forget()
                mojiTd.pack_forget()
                mojiTg.pack_forget()
                
                
                if existA == 100000:
                    existA = 300000
                    hnbutton.place_forget()
                    button.place(x = 550, y = 550)#02161226
                    mojiTn.pack_forget()
                    k3button.place_forget()
                    k15button.place_forget()                    
                    zm1button.place_forget()
                    zm2button.place_forget()
                    zm3button.place_forget()
                    zm4button.place_forget()
                    zm5button.place_forget()
                    
                    if zahyohn5 == 1:
                        hnbutton['text'] = "Q5正解"
                        hnbutton.place(x = 5, y = 250)#02161226
                        play5()
                        
                        
                        canvas.create_image(250, 300, image=imgSS106)
                        canvas.place(x=250, y=300)
                        canvas.pack()
                        
                        
                        
                    elif zahyohn5 == 2:
                        
                        
                        canvas.create_image(250, 300, image=imgSS107)
                        canvas.place(x=250, y=300)
                        canvas.pack()
                        
                    else:
                        pass
                    
                elif existA == 300000:
                    canvas.delete("all")
                    mojiA.pack(anchor='n',expand=1)
                    canvas.create_image(650, 100, image=imgSS96)#02161222
                    canvas.place(x=150, y=150)
                    canvas.pack()
                    
                    mojiTn.pack_forget()
                    emojiTn.pack_forget()
                    
    
                    canvas.create_image(800, 550, image=imgSS119)#santa1225
                    
                    existA = 1000000
                else:
                    existA = 1000000
                    
       
            time.sleep(0.4)#0216 で　1226 〇表示を修理　0.4にしてみる
 
        loop = asyncio.get_event_loop()#jikkousaretenai0205
        loop.run_until_complete(sleeping(2))
    
#     if __name__ == '__main__':#sleepinggajamaninaranaitoiiga0205
#         main()
                    
button = tk.Button(root, text = "結果発表!",command=kekka_fortune, bg = "white", fg = "red")
button.place(x = 200, y = 550)
gm1button = tk.Button(root, text = "かんたん",command=gaming1, bg = "white", fg = "red")
gm2button = tk.Button(root, text = "ザクザクモード",command=gaming2, bg = "white", fg = "red")
gm3button = tk.Button(root, text = "チャレンジモード",command=gaming3, bg = "white", fg = "red")
gm4button = tk.Button(root, text = "かんたん",command=gaming4, bg = "white", fg = "red")
gm5button = tk.Button(root, text = "ザクザクモード",command=gaming5, bg = "white", fg = "red")
gm6button = tk.Button(root, text = "チャレンジモード",command=gaming6, bg = "white", fg = "red")
gm7button = tk.Button(root, text = "かんたん",command=gaming7, bg = "white", fg = "red")
gm8button = tk.Button(root, text = "ザクザクモード",command=gaming8, bg = "white", fg = "red")
gm9button = tk.Button(root, text = "チャレンジモード",command=gaming9, bg = "white", fg = "red")
er1button = tk.Button(root, text = "日本￥",command=opening1, bg = "white", fg = "red")
er2button = tk.Button(root, text = "中国元",command=opening2, bg = "white", fg = "green")
er3button = tk.Button(root, text = "ベトナムｄ",command=opening3, bg = "white", fg = "blue")
gobutton = tk.Button(root, text = "ゲームセレクトへ",command=erabing, bg = "white", fg = "red")
zm1button = tk.Button(root, text = "のこり5問", state=tk.DISABLED, bg = "white", fg = "red")
zm2button = tk.Button(root, text = "のこり4問", state=tk.DISABLED, bg = "white", fg = "red")
zm3button = tk.Button(root, text = "のこり3問", state=tk.DISABLED, bg = "white", fg = "red")
zm4button = tk.Button(root, text = "のこり2問", state=tk.DISABLED, bg = "white", fg = "red")
zm5button = tk.Button(root, text = "のこり1問", state=tk.DISABLED, bg = "white", fg = "red")
stbutton = tk.Button(root, text = "TOPへ",command=ning, bg = "white", fg = "red")
rtbutton = tk.Button(root, text = "1つ前へ",command=erabing, bg = "white", fg = "red")
edbutton = tk.Button(root, text = "エンディング(￥)",command=ending, bg = "white", fg = "red")
ed2button = tk.Button(root, text = "エンディング(元)",command=ending2, bg = "white", fg = "red")
ed3button = tk.Button(root, text = "エンディング(ｄ)",command=ending3, bg = "white", fg = "red")
k3button = tk.Button(root, text = "はらう!",command=k3, bg = "white", fg = "red")
k3button.place(x = 500, y = 250)#早く連続押すとバグって止まります、もう改善不能？
k15button = tk.Button(root, text = "あきらめる!",command=k15, bg = "white", fg = "blue", font = ("", 20))
hnbutton = tk.Button(root, text = "正解!",state=tk.DISABLED, bg = "white", fg = "red", font = ("", 30))
tgbutton = tk.Button(root, text = "ヒントみてね",state=tk.DISABLED, bg = "white", fg = "red", font = ("", 30))#0125 hs忘れてる
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
nkbutton = tk.Button(root, text = "のこりタイム",state=tk.DISABLED, bg = "green", fg = "white", font=fontStyle)
bln = tk.BooleanVar()
bln.set(False)
chk = tk.Checkbutton(root, variable=bln, text='ヒントつける', bg = "yellow", fg = "red")
bln2 = tk.BooleanVar()
bln2.set(False)
chk2 = tk.Checkbutton(root, variable=bln2, text='ザクザク？', bg = "yellow", fg = "blue")
print("起動完了")
ning()            
timer = Timer()
thread = threading.Thread(target=timer.changeLabelText)
thread.start()
timer.root.mainloop()
print("訓練の記念に")
root.mainloop()