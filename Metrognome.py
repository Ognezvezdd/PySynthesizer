from tkinter import *
from winsound import Beep, SND_ALIAS, PlaySound


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

        self.var = StringVar()
        self.var.set(self.count)

        # self.interface()

    def interface(self):
        """Set interface for Metronome app."""
        frame = Frame()
        frame.pack()

        entry = Entry(frame, width=8, justify="center")
        entry.insert(0, "60")
        entry.grid(row=0, column=0, padx=5, sticky="E")

        label_bpm = Label(frame, text="BPM:")
        label_bpm.grid(row=0, column=0, sticky="W")
        label_count = Label(frame, textvariable=self.var, font=("Arial", 30))
        label_count.grid(row=1, column=0, columnspan=2)

        button_start = Button(frame, text="Start", width=10, height=2,
                              command=lambda: self.start_counter(entry))
        button_start.grid(row=2, column=0, padx=10, sticky="W")

        button_stop = Button(frame, text="Stop", width=10, height=2,
                             command=lambda: self.stop_counter())
        button_stop.grid(row=2, column=1, padx=10, sticky="E")

    def start_counter(self, entry):
        print(f"BPM: {int(entry.get())}")
        self.start = False
        if not self.start:
            try:
                self.bpm = int(entry.get())
            except ValueError:
                self.bpm = 60
            else:
                if self.bpm > 600:  # Limits BPM
                    self.bpm = 600
        if self.bpm == 0:
            self.start = False
        else:
            self.start = True
            self.counter()

    def stop_counter(self):
        """Stop counter by setting self.start to False."""
        self.start = False

    def counter(self):
        """Control counter display and audio with calculated time delay.

        Args:
            spinbox (tkinter.Spinbox): tkinter Spinbox widget to get beat.
        """
        if self.start:

            self.time = int((60 / self.bpm - 0.1) * 1000)  # Math for delay
            self.beat = self.bpm / 60
            print(self.time)
            self.count += 1
            self.var.set(self.count)

            if self.count >= self.beat:
                self.count = 0
            Beep(60, 40)

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
