import tkinter
from tkinter import *

Window = Tk()
Window.title("Calculator")
Window.geometry("500x500")
Window.configure(bg='grey')

display = StringVar()
display.set("_")

entry = Entry(Window, textvariable=display, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4, ipadx=70)

just_calculated = False

# ---------------------- BUTTON CLICK -----------------------
def button_click(value):
    global just_calculated
    current = display.get()

    if just_calculated:
        display.set(value)
        just_calculated = False
        return

    if current == "_" or current == "Error":
        display.set(value)
    else:
        display.set(current + value)

# ---------------------- SET OPERATOR -----------------------
def set_operator(display_op, internal_op):
    global just_calculated

    current = display.get()
    if current in ("_", "Error"):
        return

    if just_calculated:
        just_calculated = False

    if current[-1] in "+-×÷*/":
        display.set(current[:-1] + display_op)
    else:
        display.set(current + display_op)

# ----------------------- CALCULATE -------------------------
def calculate():
    global just_calculated

    expr = display.get()
    if expr in ("_", "Error"):
        return

    expr = expr.replace("×", "*").replace("÷", "/")
    expr = expr.replace("_", "")

    while len(expr) > 0 and expr[-1] in "+-*/":
        expr = expr[:-1]

    try:
        result = eval(expr)
        display.set(str(result))
        just_calculated = True
    except:
        display.set("Error")
        just_calculated = True

# ---------------------- BUTTONS (NO SPACES) ---------------------------

# Row 1
Button(Window, width=6, height=2, bg="black", fg="white", text="1", command=lambda: button_click("1")).grid(row=1, column=0)
Button(Window, width=6, height=2, bg="black", fg="white", text="2", command=lambda: button_click("2")).grid(row=1, column=1)
Button(Window, width=6, height=2, bg="black", fg="white", text="3", command=lambda: button_click("3")).grid(row=1, column=2)
Button(Window, width=6, height=2, bg="orange", fg="white", text="+", command=lambda: set_operator("+", "+")).grid(row=1, column=3)

# Row 2
Button(Window, width=6, height=2, bg="black", fg="white", text="4", command=lambda: button_click("4")).grid(row=2, column=0)
Button(Window, width=6, height=2, bg="black", fg="white", text="5", command=lambda: button_click("5")).grid(row=2, column=1)
Button(Window, width=6, height=2, bg="black", fg="white", text="6", command=lambda: button_click("6")).grid(row=2, column=2)
Button(Window, width=6, height=2, bg="orange", fg="white", text="÷", command=lambda: set_operator("÷", "/")).grid(row=2, column=3)

# Row 3
Button(Window, width=6, height=2, bg="black", fg="white", text="7", command=lambda: button_click("7")).grid(row=3, column=0)
Button(Window, width=6, height=2, bg="black", fg="white", text="8", command=lambda: button_click("8")).grid(row=3, column=1)
Button(Window, width=6, height=2, bg="black", fg="white", text="9", command=lambda: button_click("9")).grid(row=3, column=2)
Button(Window, width=6, height=2, bg="orange", fg="white", text="×", command=lambda: set_operator("×", "*")).grid(row=3, column=3)

# Row 4
Button(Window, width=6, height=2, bg="black", fg="white", text="0", command=lambda: button_click("0")).grid(row=4, column=1)
Button(Window, width=6, height=2, bg="black", fg="white", text=".", command=lambda: button_click(".")).grid(row=4, column=0)
Button(Window, width=6, height=2, bg="orange", fg="white", text="-", command=lambda: set_operator("-", "-")).grid(row=4, column=2)
Button(Window, width=6, height=2, bg="orange", fg="white", text="=", command=calculate).grid(row=4, column=3)

Window.mainloop()


def key_input(event):
    key = event.char

    if key.isdigit():            # numbers 0–9
        button_click(key)

    elif key in "+-*/":          # operators
        if key == "*":
            set_operator("×", "*")
        elif key == "/":
            set_operator("÷", "/")
        else:
            set_operator(key, key)

    elif key == "\r":            # Enter key
        calculate()

Window.bind("<Key>", key_input)
