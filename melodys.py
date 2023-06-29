import tkinter


def accord(notes):
    pass

def keyup(event):
    worker.btn_is_up = True
    global pressed_keys
    pressed_keys.discard(event.keysym)
    print(event.keysym)
    for now_piano_num in range(0, AMOUNT_PIANOS):
        try:
            index = BIND_KEYS[now_piano_num].index(event.keysym)
            if len(NOTES[index]) >= 2 and NOTES[index][1] == "b":
                btns[now_piano_num][index].config(bg="black", relief="raised")
            else:
                btns[now_piano_num][index].config(bg="white", relief="raised")
        except ValueError:
            pass

def mario():
    event = tkinter.Event
    event.keysym = {'q', 'd'}
    accord([[0, 16], [1, 14]])
    accord([[0, 16], [1, 14]])
    accord([[0, 12], [1, 14]])
    accord([[0, 16], [1, 14]])

    accord([[0, 19], [1, 19]])
    accord([[1, 7]])

    accord([[0, 12], [1, 12]])
    accord([[0, 7], [1, 12]])
    accord([[0, 4], [1, 12]])

    accord([[0, 9], [1, 5]])
    accord([[0, 11], [1, 5]])
    accord([[0, 10], [1, 5]])
    accord([[0, 9], [1, 5]])