import dearpygui.dearpygui as dpg
from Melodys.Samples import Generator

# длительность звука
DURATION_TONE = 1 / 64.0
# частота дискретизации
SAMPLE_RATE = 44100
# 16-ти битный звук (2 ** 16 -- максимальное значение для int16)
S_16BIT = 2 ** 16

OCT_NUMBER = 3
OCTAVES = ["contr", "greate", "small", "first", "second", "third", "fourth"]

NOTES = ["C1", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Hb", "H", "C2"]

GENERATION_TYPE = "sinus"
GENERATION_TYPES = ["sinus", "saw", "guitar"]
EFFECTS = {"distortion": 1}

USED_GRAPHS = False

g = Generator(S_16BIT, SAMPLE_RATE, GENERATION_TYPES, GENERATION_TYPE, EFFECTS, OCT_NUMBER, USED_GRAPHS)

def change_gen():
    global GENERATION_TYPE
    GENERATION_TYPE = GENERATION_TYPES[(GENERATION_TYPES.index(GENERATION_TYPE)+1) % len(GENERATION_TYPES)]
    dpg.set_item_label(change_gen_btn, f"{GENERATION_TYPE}")

def set_dist():
    pass


def play_note(note):
    print(NOTES[note - 27])


def oct_plus():
    global OCT_NUMBER
    OCT_NUMBER = (OCT_NUMBER + 1) % len(OCTAVES)
    dpg.set_item_label(oct_label, f"{OCTAVES[OCT_NUMBER]}")
def oct_minus():
    global OCT_NUMBER
    OCT_NUMBER = (OCT_NUMBER - 1) % len(OCTAVES)
    dpg.set_item_label(oct_label, f"{OCTAVES[OCT_NUMBER]}")


dpg.create_context()

with dpg.window(label="FL", tag="Primary Window"):
    with dpg.group(horizontal=True):
        dpg.add_button(label="Distortion:", height=20, width=160)
        oct_label = dpg.add_button(label=f"{OCTAVES[OCT_NUMBER]}", height=20, width=320)
        dpg.add_button(label="", height=20, width=160)
    with dpg.group(horizontal=True):
        dist_slider = dpg.add_slider_float(label="", default_value=0.1, min_value=0.1, max_value=1, height=20, width=160)
        dpg.add_button(label="Set", callback=set_dist, height=20, width=72)
        change_gen_btn = dpg.add_button(label=f"{GENERATION_TYPE}", callback=change_gen, height=20, width=160)
        dpg.add_button(label="", callback=set_dist, height=20, width=72)
    with dpg.group(horizontal=True):
        buttons = []
        for i in NOTES:
            buttons.append(dpg.add_button(label=i, callback=play_note, height=160, width=43))
    with dpg.group(horizontal=True):
        dpg.add_button(label="Oct-", callback=oct_minus)
        dpg.add_button(label="Oct+", callback=oct_plus)


dpg.create_viewport(title='Custom Title', width=688, height=550)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
