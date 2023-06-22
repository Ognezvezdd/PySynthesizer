import dearpygui.dearpygui as dpg

# длительность звука
DURATION_TONE = 1 / 64.0
# частота дискретизации
SAMPLE_RATE = 44100
# 16-ти битный звук (2 ** 16 -- максимальное значение для int16)
S_16BIT = 2 ** 16

OCT_NUMBER = 3
OCTAVES = ["contr", "greate", "small", "first", "second", "third", "fourth"]

GENERATION_TYPE = "sinus"
GENERATION_TYPES = ["sinus", "saw", "guitar"]
EFFECTS = {"distortion": 1}



dpg.create_context()

with dpg.window(label="FL", tag="Primary Window"):
    dpg.add_text(f"{OCTAVES[OCT_NUMBER]}")
    dpg.add_button(label=f"{GENERATION_TYPES[GENERATION_TYPE]}", callback=)
    dpg.add_text("Distortion")
    dpg.add_button(label="Set", callback=)
    dpg.add_slider_float(label="", default_value=0.1, min_value=0.1, max_value=1)

dpg.create_viewport(title='Custom Title', width=600, height=300)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()