import numpy as np
import pyaudio as pa
import os
import time
import wave
import Samples
from constants import *

py_audio = pa.PyAudio()

GENERATORS = []

gen = Samples.Generator(DURATION_TONE, 0.8, S_16BIT, SAMPLE_RATE, GENERATIONS_TYPES, "saw", EFFECTS,
                        3, AMOUNT_OCT, False)
GENERATORS.append(gen)
GENERATORS[0].generate_tones()
GENERATORS[0].USED_GRAPHS = False

gen = Samples.Generator(DURATION_TONE, 0.8, S_16BIT, SAMPLE_RATE, GENERATIONS_TYPES, "saw", EFFECTS,
                        1, AMOUNT_OCT, False)
GENERATORS.append(gen)
GENERATORS[1].generate_tones()
GENERATORS[1].USED_GRAPHS = False

frames = []


def accord(notes):
    sound = [0] * len(GENERATORS[0].tones[0])
    sound = np.array(sound, dtype=np.int32)
    maximum = 100000000

    for note in notes:
        maximum = min(maximum, max(GENERATORS[note[0]].tones[note[1]]))
        sound = list(map(lambda x, y: x + y, sound, GENERATORS[note[0]].tones[note[1]]))

    sound = sound / max(sound) * maximum
    frames.append(np.array(sound, dtype=np.int16))


def mario():
    accord([[0, 16], [1, 14]])
    accord([[0, 16], [1, 14]])
    accord([[0, 12], [1, 14]])
    accord([[0, 16], [1, 14]])


    accord([[0, 19], [1, 19]])
    accord([[1, 7]])

    accord([[0, 12], [1, 12]])
    accord([[0, 7], [1, 12]])
    accord([[0, 4], [1, 12]])

    accord([[0, 9], [1, 5]])
    accord([[0, 11], [1, 5]])
    accord([[0, 10], [1, 5]])
    accord([[0, 9], [1, 5]])

    print(frames)
    print('Finished recording!')
    current_time = str(time.strftime("%H-%M-%S", time.localtime()))
    filename = "Records/" + "record " + current_time + ".wav"
    file_path = f'Records/{filename}'
    if os.path.exists(file_path):
        filename = filename[:-5] + "1" + ".wav"
    print(filename)
    wf = wave.open(filename, 'wb')
    channels = 2
    wf.setnchannels(channels)
    wf.setsampwidth(py_audio.get_sample_size(py_audio.get_format_from_width(width=2)))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()


mario()
