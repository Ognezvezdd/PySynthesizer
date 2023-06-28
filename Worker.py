import threading
import time


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

                if self.num_thread == 1:
                    self.graph()
                elif self.num_thread == 2:
                    self.record()

                self.flag = False
            else:
                time.sleep(0.1)
