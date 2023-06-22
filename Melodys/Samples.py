import numpy as np
from main import S_16BIT, SAMPLE_RATE, GENERATION_TYPES, GENERATION_TYPE, EFFECTS
import guitar


def generate_sample(freq, duration, volume):
    print("i calc smth")
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
