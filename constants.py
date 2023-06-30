""""  КОНСТАНТЫ В ПРОЕКТЕ """

SAMPLE_RATE = 44100
""""  Частота дискретизации (не рекомендую менять) """

S_16BIT = 2 ** 16
""""  16-ти битный звук (не рекомендую менять) """

DURATION = 0.8
"""" Длительность звука (по умолчанию = 1) """

AMOUNT_PIANOS = 2
"""" Количество раскладок пианино (клавиатур)
     Для воспроизведения заранее записанных звуков рекомендуется ставить 2"""

""" ОКТАВЫ """

OCT_NUMBERS = [3] * AMOUNT_PIANOS  # 3 - first (начальное значение)
OCTAVES = ["contr", "greate", "small", "first", "second", "third", "fourth"]

""" ДОПОЛНИТЕЛЬНЫЕ ЭФФЕКТЫ И ИЗМЕНЕНИЕ ТИПА ЗВУЧАНИЯ """
GENERATION_TYPES = ["sinus"] * AMOUNT_PIANOS
""" Тип генерации для каждой из клавиатур """
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
