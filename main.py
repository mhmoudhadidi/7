myVar = 0


def on_button_pressed_a():
    global myVar
myVar += 1
basic.show_number(myVar) 
input.on_button_pressed(Button.A, on_button_pressed_a)
