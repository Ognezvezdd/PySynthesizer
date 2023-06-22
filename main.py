import dearpygui.dearpygui as dpg
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


print(OCT_NUMBER)
f = generate_notes(2)
print(OCT_NUMBER)


def change_gen():
    pass
def set_dist():
    pass
def play_note(note):
    print(note)

dpg.create_context()

with dpg.window(label="FL", tag="Primary Window"):
    oct_label = dpg.add_text(f"{OCTAVES[OCT_NUMBER]}")
    change_gen_btn = dpg.add_button(label=f"{GENERATION_TYPE}", callback=change_gen)

    dpg.add_text("Distortion")
    dpg.add_button(label="Set", callback=set_dist)
    dist_slider = dpg.add_slider_float(label="", default_value=0.1, min_value=0.1, max_value=1)

    buttons = []
    for i in NOTES:
        print(i)
        buttons.append(dpg.add_button(label=i, callback=play_note))

dpg.create_viewport(title='Custom Title', width=600, height=300)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()