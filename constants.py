""""  КОНСТАНТЫ В ПРОЕКТЕ """
DURATION_TONE = 1 / 64.0
# частота дискретизации
SAMPLE_RATE = 44100
# 16-ти битный звук (2 ** 16 -- максимальное значение для int16)
S_16BIT = 2 ** 16

DURATION = 1

AMOUNT_PIANOS = 2

OCT_NUMBERS = [3] * AMOUNT_PIANOS

OCTAVES = ["contr", "greate", "small", "first", "second", "third", "fourth"]

GENERATION_TYPES = ["sinus"] * AMOUNT_PIANOS
GENERATIONS_TYPES = ["sinus", "saw", 'guitar']
EFFECTS = {'distortion': 1}

BIND_KEYS = [["q", "2", "w", "3", "e", "r", "7", "u", "8", "i", "9", "o", "p"],
             ["z", "s", "x", "d", "c", "v", "j", "m", "k", "comma", "l", "period", "slash"]]
AMOUNT_OCT = 2
WHITE_NOTES = AMOUNT_OCT * 7 + 1
NOTES = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Hb", "H"]
oct_num = 1

FONT = "Arial 16"
FIRST_COLOR = "#666666"
SECOND_COLOR = "#BB0000"
SECOND_COLOR_PRESSED = "#990000"
