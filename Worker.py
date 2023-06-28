import threading
import time
import matplotlib.pyplot as plt

from enum import Enum


class WorkerThreadName(Enum):
    GRAPH = 1
    RECORD = 2


class Worker(threading.Thread):

    def __init__(self, num_thread):
        # вызываем конструктор базового класса
        super().__init__()
        # определяем аргументы собственного класса
        self.num_thread = num_thread
        self.flag = False
        self.active = True

    def graph(self):
        pass

    def record(self):
        pass

    def run(self):
        print(f"Началось выполнение {self.num_thread} задачи")
        while self.active:
            if self.flag:

                if self.num_thread == WorkerThreadName.GRAPH:
                    self.graph()
                elif self.num_thread == WorkerThreadName.RECORD:
                    self.record()

                self.flag = False
            else:
                time.sleep(0.1)
