import asyncio
from tkinter import *

import pyaudio as pa
# import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

import guitar

# длительность звука
duration_tone = 1 / 64.0
# частота дискретизации
SAMPLE_RATE = 44100
# 16-ти битный звук (2 ** 16 -- максимальное значение для int16)
S_16BIT = 2 ** 16
# номер октавы от 0 до 6
"""  НОМЕР ОКТАВЫ"""
OCT_NUMBER = 3
# названия октав
OCTAVES = ["contr", "greate", "small", "first", "second", "third", "fourth"]

GENERATION_TYPE = "sin"
GENERATION_TYPES = ["sin", "saw", 'guitar']
EFFECTS = {'distortion': 1}

pressed_keys = set()


def generate_sample(freq, duration, volume):
    # амплитуда
    amplitude = np.round(S_16BIT * volume / 4)
    # длительность генерируемого звука в сэмплах
    total_samples = np.round(SAMPLE_RATE * duration)
    # частоте дискретизации (пересчитанная)
    w = 2.0 * np.pi * freq / SAMPLE_RATE
    # массив сэмплов
    k = np.arange(0, SAMPLE_RATE)
    # _T = 1 / freq
    # массив значений функции (с округлением)

    data = dict.fromkeys(GENERATION_TYPES)
    data['sin'] = np.round(amplitude * np.sin(k * w))

    data['saw'] = np.round(2 * amplitude / np.pi *
                           np.arctan(np.tan(np.pi * k * freq / SAMPLE_RATE)))
    data['guitar'] = guitar.guitarString(freq, sample_rate=SAMPLE_RATE, toType=False)
    # plt.plot(data['guitar'])
    # plt.show()
    # exit(0)
    dist_parameter = EFFECTS['distortion']
    if dist_parameter != 1.0:
        np.clip(data[GENERATION_TYPE], data[GENERATION_TYPE].min() * dist_parameter,
                data[GENERATION_TYPE].max() * dist_parameter, out=data[GENERATION_TYPE])
    data[GENERATION_TYPE] /= dist_parameter
    return data[GENERATION_TYPE]


def func(n):
    global OCT_NUMBER
    n += OCT_NUMBER * 12 + 2
    return 27.5 * float(2 ** float(n / 12))


"""  ОКТАВА                   до       ре      ми     фа     соль    ля      си     """
"""  freq_array = np.array([261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88])"""


def generate_tones(duration):
    plt.close()
    plt.plot()
    tones = []
    i = 0
    print([func(n) for n in range(1, 14, 1)])
    freq_array = np.array([func(n) for n in range(1, 14)])
    for freq in freq_array:
        i += 1
        # np.array нужен для преобразования данных под формат 16 бит (dtype=np.int16)
        tone = np.array(generate_sample(freq, duration, 1), dtype=np.int16)
        tones.append(tone)
        if i > 3:
            continue
        plt.plot(tone[0:1000])
    plt.show()
    return tones


def C1():
    stream.write(tones[0])


def Db():
    stream.write(tones[1])


def D():
    stream.write(tones[2])


def Eb():
    stream.write(tones[3])


def E():
    stream.write(tones[4])


def F():
    stream.write(tones[5])


def Gb():
    stream.write(tones[6])


def G():
    stream.write(tones[7])


def Ab():
    stream.write(tones[8])


def A():
    stream.write(tones[9])


def Hb():
    stream.write(tones[10])


def H():
    stream.write(tones[11])


def C2():
    stream.write(tones[12])


def OctPlus():
    global OCT_NUMBER
    if OCT_NUMBER != 6:
        OCT_NUMBER += 1
    labelOctNumber.config(text="{}".format(OCTAVES[OCT_NUMBER]))
    global duration_tone
    global tones
    tones = generate_tones(duration_tone)


def OctMinus():
    global OCT_NUMBER
    if OCT_NUMBER != 0:
        OCT_NUMBER -= 1
    labelOctNumber.config(text="{}".format(OCTAVES[OCT_NUMBER]))
    global duration_tone
    global tones
    tones = generate_tones(duration_tone)


def generation_change():
    global GENERATION_TYPE
    GENERATION_TYPE = GENERATION_TYPES[(GENERATION_TYPES.index(GENERATION_TYPE) + 1) % len(GENERATION_TYPES)]
    btnGC.config(text="{}".format(GENERATION_TYPE))
    global duration_tone
    global tones
    tones = generate_tones(duration_tone)


def config_duration(string):
    if not string.replace('.', '').isdigit():
        return
    num = float(string)
    if 100 > num > 1:
        num /= 100
    if num < 0.1:
        num = 0.
    if num >= 100:
        num = 1

    if EFFECTS['distortion'] == num:
        return
    EFFECTS['distortion'] = num
    print(f"distortion: {EFFECTS['distortion']}")
    global duration_tone
    global tones
    tones = generate_tones(duration_tone)


def distortion_change():
    s = str(scaleDist.get())
    config_duration(s)


def keydown(event):
    global pressed_keys
    pressed_keys.add(event.keysym)
    print(*pressed_keys)
    key_list = ["q", "2", "w", "3", "e", "r", "7", "u", "8", "i", "9", "o", "p"]
    try:
        index = key_list.index(event.keysym)
        if index == 0:
            btnC1.config(bg="#888888", relief="sunken")
        elif index == 1:
            btnDb.config(bg="#888888", relief="sunken")
        elif index == 2:
            btnD.config(bg="#888888", relief="sunken")
        elif index == 3:
            btnEb.config(bg="#888888", relief="sunken")
        elif index == 4:
            btnE.config(bg="#888888", relief="sunken")
        elif index == 5:
            btnF.config(bg="#888888", relief="sunken")
        elif index == 6:
            btnGb.config(bg="#888888", relief="sunken")
        elif index == 7:
            btnG.config(bg="#888888", relief="sunken")
        elif index == 8:
            btnAb.config(bg="#888888", relief="sunken")
        elif index == 9:
            btnA.config(bg="#888888", relief="sunken")
        elif index == 10:
            btnHb.config(bg="#888888", relief="sunken")
        elif index == 11:
            btnH.config(bg="#888888", relief="sunken")
        elif index == 12:
            btnC2.config(bg="#888888", relief="sunken")
    except ValueError:
        pass
    asyncio.run(play_note())
    asyncio.sleep(1)


def keyup(event):
    global pressed_keys
    pressed_keys.discard(event.keysym)
    key_list = ["q", "2", "w", "3", "e", "r", "7", "u", "8", "i", "9", "o", "p"]
    try:
        index = key_list.index(event.keysym)
        if index == 0:
            btnC1.config(bg="white", relief="raised")
        elif index == 1:
            btnDb.config(bg="black", relief="raised")
        elif index == 2:
            btnD.config(bg="white", relief="raised")
        elif index == 3:
            btnEb.config(bg="black", relief="raised")
        elif index == 4:
            btnE.config(bg="white", relief="raised")
        elif index == 5:
            btnF.config(bg="white", relief="raised")
        elif index == 6:
            btnGb.config(bg="black", relief="raised")
        elif index == 7:
            btnG.config(bg="white", relief="raised")
        elif index == 8:
            btnAb.config(bg="black", relief="raised")
        elif index == 9:
            btnA.config(bg="white", relief="raised")
        elif index == 10:
            btnHb.config(bg="black", relief="raised")
        elif index == 11:
            btnH.config(bg="white", relief="raised")
        elif index == 12:
            btnC2.config(bg="white", relief="raised")
    except ValueError:
        pass


async def play_note():
    global pressed_keys
    key_list = ["q", "2", "w", "3", "e", "r", "7", "u", "8", "i", "9", "o", "p"]
    sound = [0] * len(tones[0])
    sound = np.array(sound, dtype=np.int32)
    maximum = 100000000
    for i in pressed_keys:
        try:
            index = key_list.index(i)
            maximum = min(maximum, max(tones[index]))
            sound = list(map(lambda x, y: x + y, sound, tones[index]))
        except ValueError:
            pass

    sound = sound / max(sound) * maximum
    stream.write(np.array(sound, dtype=np.int16))


window = Tk()
window.title("FL studio")
window.geometry("960x540")

labelOctNumber = Label(window, text="{}".format(OCTAVES[OCT_NUMBER]), font="Times 20", bg="black", fg="white")
labelOctNumber.place(relx=0.26, rely=0, relwidth=0.48, relheight=0.09)

btnOctPlus = Button(window, text="Oct+", font="Times 16", bg="#00FFFF", fg="black", activebackground="#00DDDD",
                    activeforeground="black", command=OctPlus)
btnOctPlus.place(relx=0.875, rely=0.9, relwidth=0.125, relheight=0.1)

btnOctMinus = Button(window, text="Oct-", font="Times 16", bg="#00FFFF", fg="black", activebackground="#00DDDD",
                     activeforeground="black", command=OctMinus)
btnOctMinus.place(relx=0, rely=0.9, relwidth=0.125, relheight=0.1)

btnC1 = Button(window, text="C1", font="Times 20", bg="white", fg="black", activebackground="#888888",
               activeforeground="black", command=C1)
btnC1.place(relx=0, rely=0.2, relwidth=0.125, relheight=0.69)

btnD = Button(window, text="D", font="Times 20", bg="white", fg="black", activebackground="#888888",
              activeforeground="black", command=D)
btnD.place(relx=0.125, rely=0.2, relwidth=0.125, relheight=0.69)

btnE = Button(window, text="E", font="Times 20", bg="white", fg="black", activebackground="#888888",
              activeforeground="black", command=E)
btnE.place(relx=0.25, rely=0.2, relwidth=0.125, relheight=0.69)

btnF = Button(window, text="F", font="Times 20", bg="white", fg="black", activebackground="#888888",
              activeforeground="black", command=F)
btnF.place(relx=0.375, rely=0.2, relwidth=0.125, relheight=0.69)

btnG = Button(window, text="G", font="Times 20", bg="white", fg="black", activebackground="#888888",
              activeforeground="black", command=G)
btnG.place(relx=0.5, rely=0.2, relwidth=0.125, relheight=0.69)

btnA = Button(window, text="A", font="Times 20", bg="white", fg="black", activebackground="#888888",
              activeforeground="black", command=A)
btnA.place(relx=0.625, rely=0.2, relwidth=0.125, relheight=0.69)

btnH = Button(window, text="H", font="Times 20", bg="white", fg="black", activebackground="#888888",
              activeforeground="black", command=H)
btnH.place(relx=0.75, rely=0.2, relwidth=0.125, relheight=0.69)

btnC2 = Button(window, text="C2", font="Times 20", bg="white", fg="black", activebackground="#888888",
               activeforeground="black", command=C2)
btnC2.place(relx=0.875, rely=0.2, relwidth=0.125, relheight=0.69)

btnDb = Button(window, text="Db", font="Times 16", bg="black", fg="white", activebackground="#888888",
               activeforeground="white", command=Db)
btnDb.place(relx=0.085, rely=0.2, relwidth=0.08, relheight=0.34)

btnEb = Button(window, text="Eb", font="Times 16", bg="black", fg="white", activebackground="#888888",
               activeforeground="white", command=Eb)
btnEb.place(relx=0.21, rely=0.2, relwidth=0.08, relheight=0.34)

btnGb = Button(window, text="Gb", font="Times 16", bg="black", fg="white", activebackground="#888888",
               activeforeground="white", command=Gb)
btnGb.place(relx=0.46, rely=0.2, relwidth=0.08, relheight=0.34)

btnAb = Button(window, text="Ab", font="Times 16", bg="black", fg="white", activebackground="#888888",
               activeforeground="white", command=Ab)
btnAb.place(relx=0.585, rely=0.2, relwidth=0.08, relheight=0.34)

btnHb = Button(window, text="Hb", font="Times 16", bg="black", fg="white", activebackground="#888888",
               activeforeground="white", command=Hb)
btnHb.place(relx=0.71, rely=0.2, relwidth=0.08, relheight=0.34)

btnGC = Button(window, text="{}".format(GENERATION_TYPE), font="Times 16", bg="#00FFFF", fg="black",
               activebackground="#00DDDD", activeforeground="black", command=generation_change)
btnGC.place(relx=0.38, rely=0.1, relwidth=0.24, relheight=0.09)

labelDist = Label(window, text="Distortion:", font="Times 16", bg="black", fg="white")
labelDist.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.09)

scaleDist = Scale(window, from_=10, to=100, orient="horizontal")
scaleDist.place(relx=0.75, rely=0.1, relwidth=0.25, relheight=0.09)

btnDist = Button(window, text="Set", font="Times 16", bg="#00FFFF", fg="black", activebackground="#00DDDD",
                 activeforeground="black", command=distortion_change)
btnDist.place(relx=0.63, rely=0.1, relwidth=0.11, relheight=0.09)

# генерируем тона с заданной длительностью
tones = generate_tones(duration_tone)
# инициализируем
p = pa.PyAudio()
# создаём поток для вывода
stream = p.open(format=p.get_format_from_width(width=2),
                channels=2, rate=SAMPLE_RATE, output=True, frames_per_buffer=100000)

window.bind("<KeyPress>", keydown)
window.bind("<KeyRelease>", keyup)

window.mainloop()
