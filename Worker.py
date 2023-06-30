"""КЛАСС ДЛЯ СОЗДАНИЯ 2 ПОТОКА
   ДЕЛАЕТ ПАУЗЫ ПРИ ЗАПИСИ"""

import threading
import time
import matplotlib.pyplot as plt
from constants import SAMPLE_RATE
from enum import Enum
import numpy as np


class WorkerThreadName(Enum):
    RECORD = 2


class Worker(threading.Thread):

    def __init__(self, num_thread):
        # вызываем конструктор базового класса
        super().__init__()
        # определяем аргументы собственного класса
        self.frames = []
        self.num_thread = num_thread
        self.is_recording_now = False
        self.run_task = False
        self.active = True
        self.btn_is_up = True

    def update_frame(self):
        f = self.frames
        self.frames = []
        return np.array(f, dtype=np.int16)

    def record(self):

        if self.is_recording_now and self.btn_is_up:
            # print("nothing happens")
            temp = [0] * int(SAMPLE_RATE / 5)
            # temp = [0]
            self.frames.append(temp)
            time.sleep(0.1)

    def run(self):
        print(f"Началось выполнение {self.num_thread} задачи\n")
        while self.active:
            if self.run_task:
                while self.is_recording_now:
                    if self.num_thread == WorkerThreadName.RECORD.value:
                        self.record()
                self.run_task = False
            else:
                time.sleep(0.1)
