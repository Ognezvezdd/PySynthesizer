import time
from tkinter import *
from winsound import Beep, SND_ALIAS, PlaySound, SND_FILENAME


class Metronome:

    def __init__(self, root):
        """Initiate default values for class and call interface().

        Args:
            root (tkinter.Tk): Main class instance for tkinter.
        """
        self.root = root
        self.start = False
        self.bpm = 0
        self.count = 0
        self.beat = 4
        self.time = 0
        self.fixed = 1
        self.var = StringVar()
        self.var.set(self.count)

    def stop_counter(self):
        """Stop counter by setting self.start to False."""
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
        """Control counter display and audio with calculated time delay.

        Args:
            spinbox (tkinter.Spinbox): tkinter Spinbox widget to get beat.
        """
        if self.start:
            print(time.time())
            print(f"BPM: {self.bpm}")
            self.time = int((60 / (self.bpm+18*self.bpm/60) - 0.1) * 1000)  # Math for delay
            self.beat = self.bpm / 60
            # print(self.time)
            self.count += 1
            self.var.set(self.count)

            if self.count >= self.beat:
                self.count = 0
            PlaySound('sound1.wav', SND_FILENAME)

            # Calls this method after a certain amount of time (self.time).
            self.root.after(self.time, lambda: self.counter())

def main():
    """Call Metronome class instance with tkinter root class settings."""
    root = Tk()
    root.title("Metronome")

    Metronome(root)

    root.mainloop()


if __name__ == "__main__":
    main()
