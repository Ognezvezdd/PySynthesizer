import time
from tkinter import *
from winsound import Beep
import asyncio
import pyaudio as pa
import numpy as np

import Samples

DURATION_TONE = 1 / 64.0
# частота дискретизации
SAMPLE_RATE = 44100
# 16-ти битный звук (2 ** 16 -- максимальное значение для int16)
S_16BIT = 2 ** 16

OCT_NUMBER = 3
OCTAVES = ["contr", "greate", "small", "first", "second", "third", "fourth"]

GENERATION_TYPE = "sinus"
GENERATION_TYPES = ["sinus", "saw", 'guitar']
EFFECTS = {'distortion': 1}

BIND_KEYS = ["q", "2", "w", "3", "e", "r", "7", "u", "8", "i", "9", "o", "p"]
NOTES = ["C1", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Hb", "H", "C2"]
WHITE_NOTES = 8

FONT = "Arial 16"
FIRST_COLOR = "#666666"
SECOND_COLOR = "#BB0000"
SECOND_COLOR_PRESSED = "#990000"

pressed_keys = set()


def keydown(event):
    global pressed_keys
    pressed_keys.add(event.keysym)
    try:
        index = BIND_KEYS.index(event.keysym)
        if len(NOTES[index]) >= 2 and NOTES[index][1] == "b":
            buttons[index].config(bg="#444444", relief="sunken")
        else:
            buttons[index].config(bg="#DDDDDD", relief="sunken")
    except ValueError:
        pass
    asyncio.run(play_note_by_key())


def keyup(event):
    global pressed_keys
    pressed_keys.discard(event.keysym)
    print(event.keysym)
    try:
        index = BIND_KEYS.index(event.keysym)
        if len(NOTES[index]) >= 2 and NOTES[index][1] == "b":
            buttons[index].config(bg="black", relief="raised")
        else:
            buttons[index].config(bg="white", relief="raised")
    except ValueError:
        pass


def oct_change(side):
    global OCT_NUMBER
    OCT_NUMBER = (OCT_NUMBER + side) % len(OCTAVES)
    label_octnumber.config(text=f"{(OCTAVES[OCT_NUMBER])}")

    generator.OCT_NUMBER = OCT_NUMBER
    global tones
    tones = generator.generate_tones(DURATION_TONE)


def gen_change():
    global GENERATION_TYPE
    GENERATION_TYPE = GENERATION_TYPES[(GENERATION_TYPES.index(GENERATION_TYPE) + 1) % len(GENERATION_TYPES)]
    btn_gen_change.config(text=f"{GENERATION_TYPE}")

    generator.GENERATION_TYPE = GENERATION_TYPE
    global tones
    tones = generator.generate_tones(DURATION_TONE)


def dist_change():
    generator.config_duration(str(scale_dist.get()))
    global tones
    tones = generator.generate_tones(DURATION_TONE)


def metronome(start_time, beat_offset):
    global metronome_on
    while time.time() < start_time + beat_offset:
        time.sleep(0.01)
    start_time += beat_offset
    Beep(440, 100)

    if metronome_on:
        metronome(start_time, beat_offset)


def metronome_switch():
    global metronome_on
    if metronome_on == False:
        metronome_on = True
    else:
        metronome_on = False
    metronome(time.time(), 60/scale_metronome.get())

def play_note_by_btn(note):
    stream.write(tones[NOTES.index(note)])
    print(note)


async def play_note_by_key():
    sound = [0] * len(tones[0])
    sound = np.array(sound, dtype=np.int32)
    maximum = 100000000
    for i in pressed_keys:
        try:
            index = BIND_KEYS.index(i)
            maximum = min(maximum, max(tones[index]))
            sound = list(map(lambda x, y: x + y, sound, tones[index]))
        except ValueError:
            pass

    sound = sound / max(sound) * maximum
    stream.write(np.array(sound, dtype=np.int16))


window = Tk()
window.title("FL studio")
window.configure(bg=FIRST_COLOR)
window.geometry("960x540")

label_octnumber = Label(window, text=f"{(OCTAVES[OCT_NUMBER])}", font=FONT, bg="black", fg="white")
label_octnumber.place(relx=0.26, rely=0, relwidth=0.48, relheight=0.09)
btn_oct_plus = Button(window, text="Oct+", font=FONT, bg=SECOND_COLOR, fg="black",
                      activebackground=SECOND_COLOR_PRESSED, activeforeground="black", command=lambda: oct_change(1))
btn_oct_plus.place(relx=0.875, rely=0.9, relwidth=0.125, relheight=0.1)
btn_oct_minus = Button(window, text="Oct-", font=FONT, bg=SECOND_COLOR, fg="black",
                       activebackground=SECOND_COLOR_PRESSED, activeforeground="black", command=lambda: oct_change(-1))
btn_oct_minus.place(relx=0, rely=0.9, relwidth=0.125, relheight=0.1)

btn_gen_change = Button(window, text=f"{GENERATION_TYPE}", font=FONT, bg=SECOND_COLOR, fg="black",
                        activebackground=SECOND_COLOR_PRESSED, activeforeground="black", command=gen_change)
btn_gen_change.place(relx=0.38, rely=0.1, relwidth=0.24, relheight=0.09)

label_dist = Label(window, text="Distortion:", font=FONT, bg="black", fg="white")
label_dist.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.09)
scale_dist = Scale(window, from_=10, to=100, orient="horizontal", bg="black", fg="white")
scale_dist.place(relx=0.75, rely=0.1, relwidth=0.25, relheight=0.09)
btn_dist_change = Button(window, text="Set", font=FONT, bg=SECOND_COLOR, fg="black",
                         activebackground=SECOND_COLOR_PRESSED,
                         activeforeground="black", command=dist_change)
btn_dist_change.place(relx=0.63, rely=0.1, relwidth=0.11, relheight=0.09)

metronome_on = False
label_metronome = Label(window, text="Metrognome BPM:", font=FONT, bg="black", fg="white")
label_metronome.place(relx=0, rely=0, relwidth=0.25, relheight=0.09)
scale_metronome = Scale(window, from_=0, to=240, orient="horizontal", bg="black", fg="white")
scale_metronome.place(relx=0., rely=0.1, relwidth=0.25, relheight=0.09)
btn_metronome_switch = Button(window, text="Set", font=FONT, bg=SECOND_COLOR, fg="black",
                              activebackground=SECOND_COLOR_PRESSED,
                              activeforeground="black", command=metronome_switch)
btn_metronome_switch.place(relx=0.26, rely=0.1, relwidth=0.11, relheight=0.09)

buttons = [0] * len(NOTES)
offset = 0
for note in NOTES:
    if len(note) == 1 or (len(note) >= 2 and note[1] != "b"):
        buttons[NOTES.index(note)] = Button(window, text=note, font=FONT, bg="white", fg="black",
                                            activebackground="#DDDDDD", activeforeground="black",
                                            command=lambda arg=note: play_note_by_btn(arg))
        buttons[NOTES.index(note)].place(relx=0 + offset * (1 / WHITE_NOTES), rely=0.2, relwidth=1 / WHITE_NOTES,
                                         relheight=0.69)
        offset += 1
offset = 0
for note in NOTES:
    if len(note) >= 2 and note[1] == "b":
        buttons[NOTES.index(note)] = Button(window, text=note, font=FONT, bg="black", fg="white",
                                            activebackground="#444444", activeforeground="white",
                                            command=lambda arg=note: play_note_by_btn(arg))

        if offset == 2:
            offset = 3
        if offset == 6:
            offset = 7
        if offset == 9:
            offset = 10

        buttons[NOTES.index(note)].place(relx=(1 / WHITE_NOTES) * 0.68 + offset * (1 / WHITE_NOTES), rely=0.2,
                                         relwidth=(1 / WHITE_NOTES) * 0.64, relheight=0.34)
        offset += 1

# Генерируем тона с заданной длительностью
generator = Samples.Generator(S_16BIT, SAMPLE_RATE, GENERATION_TYPES, GENERATION_TYPE, EFFECTS, OCT_NUMBER, False)
tones = generator.generate_tones(DURATION_TONE)
generator.USED_GRAPHS = False
# Инициализируем
py_audio = pa.PyAudio()
# Создаём поток для вывода
stream = py_audio.open(format=py_audio.get_format_from_width(width=2),
                       channels=2, rate=SAMPLE_RATE, output=True, frames_per_buffer=50000)

window.bind("<KeyPress>", keydown)
window.bind("<KeyRelease>", keyup)

window.mainloop()
