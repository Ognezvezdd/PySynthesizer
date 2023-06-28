import threading, time


class Worker(threading.Thread):

    def __init__(self, num_thread):
        # вызываем конструктор базового класса
        super().__init__()
        # определяем аргументы собственного класса
        self.num_thread = num_thread
        self.flag = False
        self.active = True

    def run(self):
        while self.active:
            if self.flag:
                print("YES")
                self.flag = False
            else:
                time.sleep(0.1)
