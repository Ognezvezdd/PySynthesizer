import dearpygui.dearpygui as dpg

# длительность звука
duration_tone = 1 / 64.0
# частота дискретизации
SAMPLE_RATE = 44100
# 16-ти битный звук (2 ** 16 -- максимальное значение для int16)
S_16BIT = 2 ** 16

OCT_NUMBER = 3
OCTAVES = ["contr", "greate", "small", "first", "second", "third", "fourth"]

GENERATION_TYPE = "sinus"
GENERATION_TYPES = ["sinus", "saw", "guitar"]
EFFECTS = {'distortion': 1}

dpg.create_context()

with dpg.window(label="FL", tag="Primary Window"):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.1, min_value=0.1, max_value=1)

dpg.create_viewport(title='Custom Title', width=600, height=300)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()