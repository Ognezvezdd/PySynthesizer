import threading
import time
import matplotlib.pyplot as plt

from enum import Enum


class WorkerThreadName(Enum):
    RECORD = 2


class Worker(threading.Thread):

    def __init__(self, num_thread):
        # вызываем конструктор базового класса
        super().__init__()
        # определяем аргументы собственного класса
        self.num_thread = num_thread
        self.run_task = False
        self.active = True

    def record(self):
        pass

    def run(self):
        print(f"Началось выполнение {self.num_thread} задачи")
        while self.active:
            if self.run_task:
                if self.num_thread == WorkerThreadName.RECORD.value:
                    self.record()

                self.run_task = False
            else:
                time.sleep(0.1)
