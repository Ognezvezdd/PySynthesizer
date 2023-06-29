import threading
import time
import matplotlib.pyplot as plt
from constants import SAMPLE_RATE
from enum import Enum


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

    def record(self):
        if self.is_recording_now and self.btn_is_up:
            print("nothing happens")
            self.frames.insert([0]*SAMPLE_RATE/10)

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
