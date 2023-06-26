import time
from tkinter import *
from winsound import Beep, SND_ALIAS, PlaySound, SND_FILENAME


class Metronome:

    def __init__(self, root):

        self.root = root
        self.start = False
        self.bpm = 0
        self.time = 0
        self.fixed = 1

    def stop_counter(self):
        self.start = False

    def start_counter(self, entry):
        if self.fixed % 2 == 0:
            self.stop_counter()
            self.fixed += 1
            return
        self.fixed += 1
        if not self.start:
            try:
                self.bpm = int(entry.get())
            except ValueError:
                self.bpm = 60
        if self.bpm == 0:
            self.stop_counter()
        else:
            self.start = True
            self.counter()

    def counter(self):
        if self.start:
            print(time.time())
            print(f"BPM: {self.bpm}")
            self.time = int((60 / self.bpm) * 1000) - 330  # Math for delay

            PlaySound('sound1.wav', SND_FILENAME)
            # Calls this method after a certain amount of time (self.time).

            print(self.time)
            self.root.after(self.time, lambda: self.counter())


def main():
    """Call Metronome class instance with tkinter root class settings."""
    root = Tk()
    root.title("Metronome")

    Metronome(root)

    root.mainloop()


if __name__ == "__main__":
    main()
