import asyncio
import os
import time
import tkinter
import wave
from tkinter import *
import numpy as np
import pyaudio as pa
from playsound import playsound
import Metrognome
import Samples
import Worker
import Melodis
from constants import *

pressed_keys = set()
is_stop_please = False

melody = Melodis.Melodis()


async def play_sound_mario():
    global is_stop_please

    event = tkinter.Event
    event.keysym = 'q'
    global melody
    # print(melody.this_list)
    for i in melody.this_list:
        if is_stop_please:
            return
        if i[0] == -1:
            await asyncio.sleep(0.08)
            continue
        for j in i:
            if len(btns[j[0]][j[1]].cget('text')) >= 2 and btns[j[0]][j[1]].cget('text')[1] == "b":
                btns[j[0]][j[1]].config(bg="#444444", relief="sunken")
            else:
                btns[j[0]][j[1]].config(bg="#DDDDDD", relief="sunken")
            play_note_by_btn(NOTES[j[1]], j[0])
        window.update()

        await asyncio.sleep(0.25 * DURATION)
        for j in i:
            if len(btns[j[0]][j[1]].cget('text')) >= 2 and btns[j[0]][j[1]].cget('text')[1] == "b":
                btns[j[0]][j[1]].config(bg="black", relief="raised")
            else:
                btns[j[0]][j[1]].config(bg="white", relief="raised")
        window.update()


async def start_sins():
    task1 = asyncio.create_task(play_sound_mario())
    await task1


def keydown(event):
    """" """

    global is_stop_please
    if 'F1' == event.keysym:
        is_stop_please = False
        asyncio.run(start_sins())
        return
    if 'F2' == event.keysym:
        is_stop_please = True
        return

    if 'F3' == event.keysym:
        if (1 - OCT_NUMBERS[1]) != 0:
            oct_change(1 - OCT_NUMBERS[1], 1)
        if GENERATION_TYPES[0] == "saw":
            pass
        elif GENERATION_TYPES[0] == "sinus":
            gen_change(0)
        else:
            gen_change(0)
            gen_change(0)

        if GENERATION_TYPES[1] == "saw":
            pass
        elif GENERATION_TYPES[1] == "sinus":
            gen_change(1)
        else:
            gen_change(1)
            gen_change(1)
        return
    if "F5" == event.keysym:
        global melody
        melody.change_song()
        # print("NOW MELODY")
        # print(melody.this_list)
        return

    worker.btn_is_up = False
    global pressed_keys
    pressed_keys.add(event.keysym)
    # print(event.keysym)
    for now_piano_num in range(0, AMOUNT_PIANOS):
        try:
            index = BIND_KEYS[now_piano_num].index(event.keysym)
            if len(NOTES[index]) >= 2 and NOTES[index][1] == "b":
                btns[now_piano_num][index].config(bg="#444444", relief="sunken")
            else:
                btns[now_piano_num][index].config(bg="#DDDDDD", relief="sunken")
        except ValueError:
            pass
    window.update()
    play_note_by_key()


def keyup(event):
    worker.btn_is_up = True
    global pressed_keys
    pressed_keys.discard(event.keysym)

    for now_piano_num in range(0, AMOUNT_PIANOS):
        try:
            index = BIND_KEYS[now_piano_num].index(event.keysym)
            if len(NOTES[index]) >= 2 and NOTES[index][1] == "b":
                btns[now_piano_num][index].config(bg="black", relief="raised")
            else:
                btns[now_piano_num][index].config(bg="white", relief="raised")
        except ValueError:
            pass


def oct_change(side, piano_num):
    OCT_NUMBERS[piano_num] = (OCT_NUMBERS[piano_num] + side) % (len(OCTAVES) - AMOUNT_OCT + 1)
    labels_octnumber[piano_num].config(text=f"{(OCTAVES[OCT_NUMBERS[piano_num]])}")

    GENERATORS[piano_num].OCT_NUMBER = OCT_NUMBERS[piano_num]
    GENERATORS[piano_num].generate_tones()


def gen_change(piano_num):
    global GENERATION_TYPES
    GENERATION_TYPES[piano_num] = GENERATIONS_TYPES[
        (GENERATIONS_TYPES.index(GENERATION_TYPES[piano_num]) + 1) % len(GENERATIONS_TYPES)]
    btns_gen_change[piano_num].config(text=f"{GENERATION_TYPES[piano_num]}")

    GENERATORS[piano_num].GENERATION_TYPE = GENERATION_TYPES[piano_num]
    GENERATORS[piano_num].generate_tones()


def dist_change(piano_num):
    GENERATORS[piano_num].config_duration(str(scales_dist[piano_num].get()))


def metronome_switch():
    metronome.start_counter(scale_metronome)


frames = []


def stop_record():
    # print(frames)
    # print('Finished recording!')
    current_time = str(time.strftime("%H-%M-%S", time.localtime()))
    filename = "Records/" + "record " + current_time + ".wav"
    file_path = f'Records/{filename}'
    if os.path.exists(file_path):
        filename = filename[:-5] + "1" + ".wav"
    # print(filename)
    wf = wave.open(filename, 'wb')
    channels = 2
    wf.setnchannels(channels)
    wf.setsampwidth(py_audio.get_sample_size(py_audio.get_format_from_width(width=2)))
    wf.setframerate(SAMPLE_RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def start_record():
    worker.run_task = True
    # print('Recording...')
    global frames
    frames = []


def record():
    global record_on
    global now_playing_sound_and_recording
    if record_on:
        btn_record.config(text="not rec")
        record_on = False
        now_playing_sound_and_recording = False
        worker.is_recording_now = False
        stop_record()
    else:
        btn_record.config(text="recording")
        record_on = True
        now_playing_sound_and_recording = False
        worker.is_recording_now = True
        start_record()


def record_play():
    directory = 'Records'
    last = max([os.path.join(directory, filename) for filename in os.listdir(directory)], key=os.path.getctime)
    last = last.replace('\\', '/')
    # print(f"I play: {last}")
    playsound(os.path.abspath(last), block=True)


def play_note_by_btn(note, piano_num):
    STREAMS[piano_num].write(GENERATORS[piano_num].tones[NOTES.index(note)])
    # print(note)
    if record_on:
        frames.append(GENERATORS[piano_num].tones[NOTES.index(note)])


def play_note_by_key():
    sound = [0] * len(GENERATORS[0].tones[0])
    sound = np.array(sound, dtype=np.int32)
    maximum = 100000000
    for _key in pressed_keys:
        try:
            if AMOUNT_PIANOS != 1:
                piano_num = [i for i in range(0, AMOUNT_PIANOS) if _key in BIND_KEYS[i]][0]
            else:
                piano_num = 0
            index = BIND_KEYS[piano_num].index(_key)
            maximum = min(maximum, max(GENERATORS[piano_num].tones[index]))
            sound = list(map(lambda x, y: x + y, sound, GENERATORS[piano_num].tones[index]))
        except EXCEPTION as ex:
            pass
        else:
            pass

    sound = sound / max(sound) * maximum
    STREAMS[0].write(np.array(sound, dtype=np.int16))
    if record_on:
        frames.append(worker.update_frame())
        frames.append(np.array(sound, dtype=np.int16))
        # print(len(STREAMS[0].read(BUFFER)))


window = Tk()
window.title("FL studio")
window.configure(bg=FIRST_COLOR)
width = WHITE_NOTES * 90
height = AMOUNT_PIANOS * 360 + 180
window.geometry(f"{width}x{height}")
# window.geometry("960x540")

labels_octnumber = []
btns_oct_plus = []
btns_oct_minus = []
btns_gen_change = []
labels_dist = []
scales_dist = []
btns_dist_change = []
btns = []

for piano_num in range(0, AMOUNT_PIANOS):

    labels_octnumber.append(
        Label(window, text=f"{(OCTAVES[OCT_NUMBERS[piano_num]])}", font=FONT, bg="black", fg="white"))
    labels_octnumber[piano_num].place(relx=0.38, rely=(0.9 / AMOUNT_PIANOS) * piano_num + 0.01 / AMOUNT_PIANOS,
                                      relwidth=0.24,
                                      relheight=0.08 / AMOUNT_PIANOS)
    btns_oct_plus.append(
        Button(window, text="Oct+", font=FONT, bg=SECOND_COLOR, fg="black", activebackground=SECOND_COLOR_PRESSED,
               activeforeground="black", command=lambda arg=piano_num: oct_change(1, arg)))
    btns_oct_plus[piano_num].place(relx=0.63, rely=(0.9 / AMOUNT_PIANOS) * piano_num + 0.01 / AMOUNT_PIANOS,
                                   relwidth=0.11,
                                   relheight=0.08 / AMOUNT_PIANOS)
    btns_oct_minus.append(
        Button(window, text="Oct-", font=FONT, bg=SECOND_COLOR, fg="black", activebackground=SECOND_COLOR_PRESSED,
               activeforeground="black", command=lambda arg=piano_num: oct_change(-1, arg)))
    btns_oct_minus[piano_num].place(relx=0.26, rely=(0.9 / AMOUNT_PIANOS) * piano_num + 0.01 / AMOUNT_PIANOS,
                                    relwidth=0.11,
                                    relheight=0.08 / AMOUNT_PIANOS)

    btns_gen_change.append(Button(window, text=f"{GENERATION_TYPES[piano_num]}", font=FONT, bg=SECOND_COLOR, fg="black",
                                  activebackground=SECOND_COLOR_PRESSED, activeforeground="black",
                                  command=lambda arg=piano_num: gen_change(arg)))
    btns_gen_change[piano_num].place(relx=0.38, rely=(0.9 / AMOUNT_PIANOS) * piano_num + 0.1 / AMOUNT_PIANOS,
                                     relwidth=0.24,
                                     relheight=0.09 / AMOUNT_PIANOS)

    labels_dist.append(Label(window, text="Distortion:", font=FONT, bg="black", fg="white"))
    labels_dist[piano_num].place(relx=0.75, rely=(0.9 / AMOUNT_PIANOS) * piano_num + 0.01 / AMOUNT_PIANOS,
                                 relwidth=0.24, relheight=0.08 / AMOUNT_PIANOS)
    scales_dist.append(Scale(window, from_=10, to=100, orient="horizontal", bg="black", fg="white", font="arial 10"))
    scales_dist[piano_num].place(relx=0.75, rely=(0.9 / AMOUNT_PIANOS) * piano_num + 0.1 / AMOUNT_PIANOS, relwidth=0.24,
                                 relheight=0.09 / AMOUNT_PIANOS)
    btns_dist_change.append(
        Button(window, text="Set", font=FONT, bg=SECOND_COLOR, fg="black", activebackground=SECOND_COLOR_PRESSED,
               activeforeground="black", command=lambda arg=piano_num: dist_change(arg)))
    btns_dist_change[piano_num].place(relx=0.63, rely=(0.9 / AMOUNT_PIANOS) * piano_num + 0.1 / AMOUNT_PIANOS,
                                      relwidth=0.11, relheight=0.09 / AMOUNT_PIANOS)

    buttons = [0] * len(NOTES)
    offset = 0
    for note in NOTES:
        if len(note) == 1 or (len(note) >= 2 and note[1] != "b"):
            buttons[NOTES.index(note)] = Button(window, text=note, font=FONT, bg="white", fg="black",
                                                activebackground="#DDDDDD", activeforeground="black",
                                                command=lambda arg=note, arg2=piano_num: play_note_by_btn(arg, arg2))
            buttons[NOTES.index(note)].place(relx=0 + offset * (1 / WHITE_NOTES),
                                             rely=(0.9 / AMOUNT_PIANOS) * piano_num + 0.2 / AMOUNT_PIANOS,
                                             relwidth=1 / WHITE_NOTES, relheight=0.69 / AMOUNT_PIANOS)
            offset += 1
    offset = 0
    for note in NOTES:
        if len(note) >= 2 and note[1] == "b":
            buttons[NOTES.index(note)] = Button(window, text=note, font=FONT, bg="black", fg="white",
                                                activebackground="#444444", activeforeground="white",
                                                command=lambda arg=note, arg2=piano_num: play_note_by_btn(arg, arg2))

            if offset % 7 == 2:
                offset += 1
            if offset % 7 == 6:
                offset += 1

            buttons[NOTES.index(note)].place(relx=(1 / WHITE_NOTES) * 0.68 + offset * (1 / WHITE_NOTES),
                                             rely=(0.9 / AMOUNT_PIANOS) * piano_num + 0.2 / AMOUNT_PIANOS,
                                             relwidth=(1 / WHITE_NOTES) * 0.64, relheight=0.34 / AMOUNT_PIANOS)
            offset += 1
    btns.append(buttons)

record_on = False
now_playing_sound_and_recording = False
btn_record = Button(window, text="not rec", font=FONT, bg=SECOND_COLOR, fg="black",
                    activebackground=SECOND_COLOR_PRESSED,
                    activeforeground="black", command=record)
btn_record.place(relx=0.75, rely=0.9, relwidth=0.115, relheight=0.09)
btn_record_play = Button(window, text="play", font=FONT, bg=SECOND_COLOR, fg="black",
                         activebackground=SECOND_COLOR_PRESSED,
                         activeforeground="black", command=record_play)
btn_record_play.place(relx=0.875, rely=0.9, relwidth=0.115, relheight=0.09)

metronome_on = False
label_metronome = Label(window, text="Metrognome BPM:", font=FONT, bg="black", fg="white")
label_metronome.place(relx=0.01, rely=0.9, relwidth=0.24, relheight=0.09)
scale_metronome = Scale(window, from_=0, to=180, orient="horizontal", bg="black", fg="white", font="arial 10")
scale_metronome.place(relx=0.26, rely=0.9, relwidth=0.23, relheight=0.09)
btn_metronome_switch = Button(window, text="Set", font=FONT, bg=SECOND_COLOR, fg="black",
                              activebackground=SECOND_COLOR_PRESSED,
                              activeforeground="black", command=metronome_switch)
btn_metronome_switch.place(relx=0.51, rely=0.9, relwidth=0.23, relheight=0.09)

worker = Worker.Worker(2)
worker.start()
worker.run_task = True

GENERATORS = []
for piano in range(AMOUNT_PIANOS):
    gen = Samples.Generator(DURATION, S_16BIT, SAMPLE_RATE, GENERATIONS_TYPES, GENERATION_TYPES[0],
                            EFFECTS,
                            OCT_NUMBERS[0], AMOUNT_OCT, False)

    GENERATORS.append(gen)
    GENERATORS[piano].generate_tones()
    GENERATORS[piano].USED_GRAPHS = False

metronome = Metrognome.Metronome(root=window)

# Инициализируем
py_audio = pa.PyAudio()
# Создаём поток для вывода
# BUFFER = 1024 * 8 * 3
BUFFER = int(SAMPLE_RATE * DURATION)
STREAMS = []

# print(py_audio.get_default_output_device_info())
for piano in range(AMOUNT_PIANOS):
    s = py_audio.open(format=py_audio.get_format_from_width(width=2),
                      channels=2, rate=SAMPLE_RATE, output=True, frames_per_buffer=BUFFER)
    STREAMS.append(s)

window.bind("<KeyPress>", keydown)
window.bind("<KeyRelease>", keyup)

window.mainloop()
# http://ru.battleship-game.org/id89615982
# https://chordify.net/chords/super-mario-theme-easy-piano-piaknowitall
worker.active = False
