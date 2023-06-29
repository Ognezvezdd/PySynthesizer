import numpy as np
import pyaudio as pa
import os
import time
import wave
py_audio = pa.PyAudio()

def mario(GENERATORS):
    frames = []

    frames.append(GENERATORS[0].tones[16])
    frames.append(GENERATORS[0].tones[16])
    frames.append(GENERATORS[0].tones[12])
    frames.append(GENERATORS[0].tones[16])
    frames.append(GENERATORS[0].tones[19])
    frames.append(GENERATORS[0].tones[12])
    frames.append(GENERATORS[0].tones[7])
    frames.append(GENERATORS[0].tones[4])
    frames.append(GENERATORS[0].tones[9])
    frames.append(GENERATORS[0].tones[11])
    frames.append(GENERATORS[0].tones[10])
    frames.append(GENERATORS[0].tones[9])
    frames.append(GENERATORS[0].tones[7])

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