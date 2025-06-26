from random import choice
from turtle import *
from freegames import floor, vector
import pygame
import os

pygame.init()
# Inisialisasi turtle
pena_gambar = Turtle(visible=False)
tulisan_skor = Turtle(visible=False)
tulisan_skor.penup()
tulisan_skor.goto(-200, 190)
tulisan_skor.color('purple')

arah_gerakan_player = vector(5, 0)
posisi_player = vector(-40, -80)
daftar_musuh = [
    vector(-180, 160),
    vector(-180, -160),
    vector(100, 160),
    vector(100, -160),
]
daftar_arah_musuh = [
    vector(5, 0),
    vector(0, 5),
    vector(0, -5),
    vector(-5, 0),
]

skor = 0  

set_makanan = set()

peta_permainan = [ # peta permainan, 0 = dinding, 1 = jalan, 2 = titik yang sudah dimakan 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

#agar fungsi square menggambar persegi berwarna pink pada koordinat x, y
def square(x, y):
    pena_gambar.up()
    pena_gambar.goto(x, y)
    pena_gambar.down()
    pena_gambar.begin_fill()
    for _ in range(4):
        pena_gambar.forward(20)
        pena_gambar.left(90)
    pena_gambar.end_fill()

#agar fungsi offset mengubah koordinat titik menjadi indeks peta
def offset(titik): 
    x = int((floor(titik.x, 20) + 200) / 20)
    y = int((180 - floor(titik.y, 20)) / 20)
    return x, y

#agar fungsi valid untuk memeriksa apakah titik berada pada peta dan tidak berada di dinding
def valid(titik):
    x, y = offset(titik)
    if peta_permainan[y][x] == 0:
        return False
    x2, y2 = offset(titik + 19)
    if peta_permainan[y2][x2] == 0:
        return False
    return titik.x % 20 == 0 or titik.y % 20 == 0

def tampilkan_skor():
    tulisan_skor.clear()
    tulisan_skor.write(f"Skor: {skor}", font=('Arial', 12, 'bold'))

def tampilan_teks(teks, warna):
    pena_gambar.goto(0, 0)
    pena_gambar.color(warna)
    pena_gambar.write(teks, align='center', font=('Arial', 35, 'bold'))

def gambar_tombol():
    # Tombol ulang
    pena_gambar.up()
    pena_gambar.goto(-125, -220)
    pena_gambar.color('brown')
    pena_gambar.begin_fill()
    for _ in range(2):
        pena_gambar.forward(100)
        pena_gambar.left(90)
        pena_gambar.forward(40)
        pena_gambar.left(90)
    pena_gambar.end_fill()
    pena_gambar.goto(-70, -210)
    pena_gambar.color('white')
    pena_gambar.write("Ulang ", align='center', font=('Arial', 12, 'bold'))

    # Tombol keluar
    pena_gambar.up()
    pena_gambar.goto(5, -220)
    pena_gambar.color('brown')
    pena_gambar.begin_fill()
    for _ in range(2):
        pena_gambar.forward(100)
        pena_gambar.left(90)
        pena_gambar.forward(40)
        pena_gambar.left(90)
    pena_gambar.end_fill()
    pena_gambar.goto(55, -210)
    pena_gambar.color('white')
    pena_gambar.write("Keluar", align='center', font=('Arial', 12, 'bold'))

def klik(x, y):
    if -120 <= x <= -20 and -220 <= y <= -180:
        reset()
    elif 20 <= x <= 120 and -220 <= y <= -180:
        bye()

def tampilan_peta():
    bgcolor('white')
    pena_gambar.color('pink')
    for y in range(len(peta_permainan)):
        for x in range(len(peta_permainan[y])):  # <-- diperbaiki di sini
            peta = peta_permainan[y][x]
            pos_x = x * 20 - 200
            pos_y = 180 - y * 20
            if peta > 0:
                square(pos_x, pos_y)
                if peta == 1:
                    posisi_makanan = (pos_x + 10, pos_y + 10)
                    set_makanan.add(posisi_makanan)
                    pena_gambar.up()
                    pena_gambar.goto(posisi_makanan)
                    pena_gambar.dot(3, 'pink')

#agar fungsi menggerakkan player, memeriksa musuh, makanan, dan menang
def pergerakan():
    global skor
    clear()
    if valid(posisi_player + arah_gerakan_player):
        posisi_player.move(arah_gerakan_player)

    # Cek musuh
    path_suara_gameover = os.path.join(os.path.dirname(__file__), "gameover.wav")
    gameover_sound = pygame.mixer.Sound(path_suara_gameover)
    for musuh in daftar_musuh:
        if abs(posisi_player.x - musuh.x) < 20 and abs(posisi_player.y - musuh.y) < 20:
            gameover_sound.play()
            tulis_skor_ke_file()
            tampilan_teks("GAME OVER    ", "red")
            gambar_tombol()
            onscreenclick(klik)
            return

    # Makan makanan
    posisi_makan = (posisi_player.x + 10, posisi_player.y + 10)
    if posisi_makan in set_makanan:
        set_makanan.remove(posisi_makan)
        skor += 10
        tampilkan_skor()
        makan_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "makan.wav"))
        makan_sound.play()

    if posisi_makan in set_makanan:
        tampilkan_skor()
        makan_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "makan.wav"))
        makan_sound.play()

    # Menang
    if not set_makanan:
        win_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "win.wav"))
        win_sound.play()
        tulis_skor_ke_file()
        tampilan_teks("YOU WIN!   ", "green")
        gambar_tombol()
        onscreenclick(klik)
        return

    # Gambar player
    up()
    goto(posisi_player.x + 10, posisi_player.y + 10)
    dot(20, 'white')

    # Musuh
    for i in range(len(daftar_musuh)):
        posisi_sekarang = daftar_musuh[i]
        arah_sekarang = daftar_arah_musuh[i]
        posisi_tujuan = posisi_sekarang + arah_sekarang
        if valid(posisi_tujuan):
            daftar_musuh[i] = posisi_tujuan
        else:
            kemungkinan_arah = [vector(5, 0), vector(-5, 0), vector(0, 5), vector(0, -5)]
            arah_valid=[ ]
            for arah_alternatif in kemungkinan_arah:
                if valid(posisi_sekarang + arah_alternatif):
                    arah_valid.append(arah_alternatif)
            if arah_valid:
                daftar_arah_musuh[i] = choice(arah_valid)
                daftar_musuh[i] = posisi_sekarang + daftar_arah_musuh[i]
        up()
        goto(daftar_musuh[i].x + 10, daftar_musuh[i].y + 10)
        dot(20, 'magenta')

    # Gambar makanan
    for posisi_makanan in set_makanan:
        up()
        goto(posisi_makanan)
        dot(3, 'white')

    update()
    ontimer(pergerakan, 90) 

def ubah_arah_player(x, y):
    if valid(posisi_player+ vector(x, y)):
        arah_gerakan_player.x = x
        arah_gerakan_player.y = y

def reset():
    global skor
    skor = 0
    tampilkan_skor()
    pena_gambar.clear()
    onscreenclick(None)
    set_makanan.clear()
    posisi_player.x = -40
    posisi_player.y = -80
    daftar_musuh[0].x = -180
    daftar_musuh[0].y = 160
    daftar_musuh[1].x = -180
    daftar_musuh[1].y = -160
    daftar_musuh[2].x = 100
    daftar_musuh[2].y = 160
    daftar_musuh[3].x = 100
    daftar_musuh[3].y = -160
    tampilan_peta()
    pergerakan()

def tulis_skor_ke_file():
        path_file = os.path.join(os.path.dirname(__file__), "skor_player.txt")
        with open(path_file, "a") as file:
            file.write(f"skor : {skor}\n")

def keyboard_right():
    ubah_arah_player(5, 0)
onkey(keyboard_right, 'Right')
def keyboard_left():
    ubah_arah_player(-5, 0)
onkey(keyboard_left, 'Left')
def keyboard_up():
    ubah_arah_player(0, 5)
onkey(keyboard_up, 'Up')
def keyboard_down():
    ubah_arah_player(0, -5)
onkey(keyboard_down, 'Down')

hideturtle()
tracer(False)
listen()
tampilan_peta()
tampilkan_skor()
pergerakan()
done()
