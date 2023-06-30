""""  КОНСТАНТЫ В ПРОЕКТЕ """

SAMPLE_RATE = 44100
""""  Частота дискретизации (не рекомендую менять) """

S_16BIT = 2 ** 16
""""  16-ти битный звук (не рекомендую менять) """

DURATION = 0.7
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
""" Типы генерации """
EFFECTS = {'distortion': 1}
""" Эффекты (distortion = 1 - это отсутствие distortion) """

BIND_KEYS = [["q", "2", "w", "3", "e", "r", "7", "u", "8", "i", "9", "o", "p"],
             ["z", "s", "x", "d", "c", "v", "j", "m", "k", "comma", "l", "period", "slash"]]
""" Клавиши для игры """
AMOUNT_OCT = 3
""" Количество октав на экране """
WHITE_NOTES = AMOUNT_OCT * 7 + 1
""" Количество клавиш для работы внутри программы (не рекомендую менять) """
NOTES = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Hb", "H"]
""" Ноты для игры """

oct_num = 1
try:
    for piano_num in range(1, AMOUNT_OCT):
        for j in range(0, 12):
            NOTES.append(NOTES[j] + str(oct_num))
        oct_num += 1
except Exception as es:
    pass
NOTES.append(NOTES[0] + str(oct_num))

""" ЦВЕТА И ОФОРМЛЕНИЕ """
FONT = "Arial 16"
FIRST_COLOR = "#666666"
SECOND_COLOR = "#BB0000"
SECOND_COLOR_PRESSED = "#990000"
