import matplotlib.pyplot as plt
import numpy as np

import guitar


class Generator:

    def __init__(self, S_16BIT, SAMPLE_RATE, GENERATION_TYPES, GENERATION_TYPE, EFFECTS, OCT_NUMBER,
                 USED_GRAPHS=True):
        self.OCT_NUMBER = OCT_NUMBER
        self.S_16BIT = S_16BIT
        self.SAMPLE_RATE = SAMPLE_RATE
        self.GENERATION_TYPES = GENERATION_TYPES
        self.GENERATION_TYPE = GENERATION_TYPE
        self.EFFECTS = EFFECTS
        self.USED_GRAPHS = USED_GRAPHS

    def generate_sample(self, freq, duration, volume):
        # амплитуда
        amplitude = np.round(self.S_16BIT * volume / 4)
        # длительность генерируемого звука в сэмплах
        total_samples = np.round(self.SAMPLE_RATE * duration)
        # частоте дискретизации (пересчитанная)
        w = 2.0 * np.pi * freq / self.SAMPLE_RATE
        # массив сэмплов
        k = np.arange(0, self.SAMPLE_RATE)
        T = 1 / freq
        # массив значений функции (с округлением)

        data = dict.fromkeys(self.GENERATION_TYPES)
        data['sin'] = np.round(amplitude * np.sin(k * w))

        data['saw'] = np.round(2 * amplitude / np.pi *
                               np.arctan(np.tan(np.pi * k * freq / self.SAMPLE_RATE)))
        data['guitar'] = guitar.guitarString(freq, sample_rate=self.SAMPLE_RATE, toType=False)

        dist_parameter = self.EFFECTS['distortion']
        if dist_parameter != 1.0:
            np.clip(data[self.GENERATION_TYPE], data[self.GENERATION_TYPE].min() * dist_parameter,
                    data[self.GENERATION_TYPE].max() * dist_parameter, out=data[self.GENERATION_TYPE])
        data[self.GENERATION_TYPE] /= dist_parameter
        return data[self.GENERATION_TYPE]

    def generate_notes(self, n):
        self.OCT_NUMBER = 5
        n += self.OCT_NUMBER * 12 + 2
        return 27.5 * float(2 ** float(n / 12))

    def generate_tones(self, duration):
        plt.close()
        tones = []
        i = 0
        print([self.generate_notes(n) for n in range(1, 14, 1)])
        freq_array = np.array([self.generate_notes(n) for n in range(1, 14)])
        for freq in freq_array:
            i += 1
            # np.array нужен для преобразования данных под формат 16 бит (dtype=np.int16)
            tone = np.array(self.generate_sample(freq, duration, 1), dtype=np.int16)
            tones.append(tone)
            if i > 3:
                continue
            if self.USED_GRAPHS:
                plt.plot(tone[0:1000])
                plt.show()
        return tones
