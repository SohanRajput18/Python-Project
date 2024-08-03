from tkinter import *
import tkinter.messagebox as tmsg
import math as m

root = Tk()

root.minsize(520, 340)
root.maxsize(520, 340)

root.title("Scientific Calculator")

sc = StringVar()
entry = Entry(root, width=31, textvariable=sc, relief=SUNKEN, font="cosmicsansms 20")
entry.grid(row=0, column=0, columnspan=10, padx=11, pady=12)

def helper():
    help_text = '''1. For the following functions please enter the number first and then press the required function:
sin, cos, tan, log, ln, √, !, rad, degree, 1/x, π, e 

2. For multiplication with float numbers, say 5*0.4 multiply like 5*4/10'''
    tmsg.showinfo("Help", help_text)

def abt():
    about_text = "Thank you for using our app!" 
    tmsg.showinfo("About", about_text)

def const():
    msg = '''If you press constants like: π and e, 2 times, the result will be square of that constant. 
That means number of times you press the constant, the result will be constant to the power that number.'''
    tmsg.showinfo("Help", msg)

mainmenu = Menu(root)

submenu = Menu(mainmenu, tearoff=0)
submenu.add_command(label="General", command=helper)
submenu.add_command(label="Constants", command=const)
mainmenu.add_cascade(label="Help", menu=submenu)

mainmenu.add_command(label="About", command=abt)
mainmenu.add_command(label="Exit", command=root.quit)

root.config(menu=mainmenu)

def sciCal(event):
    key = event.widget
    text = key['text']
    val = sc.get()
    sc.set("")
    try:
        if text == "sin":
            sc.set(m.sin(float(val)))
        elif text == "cos":
            sc.set(m.cos(float(val)))
        elif text == "tan":
            sc.set(m.tan(float(val)))
        elif text == "log":
            if float(val) <= 0.00:
                sc.set("Not Possible")
            else:
                sc.set(m.log10(float(val)))
        elif text == "ln":
            if float(val) <= 0.00:
                sc.set("Not Possible")
            else:
                sc.set(m.log(float(val)))
        elif text == "√":
            sc.set(m.sqrt(float(val)))
        elif text == "!":
            sc.set(m.factorial(int(val)))
        elif text == "rad":
            sc.set(m.radians(float(val)))
        elif text == "deg":
            sc.set(m.degrees(float(val)))
        elif text == "1/x":
            if val == "0":
                sc.set("ꝏ")
            else:
                sc.set(1/float(val))
        elif text == "π":
            if val == "":
                sc.set(m.pi)
            else:
                sc.set(float(val) * m.pi)
        elif text == "e":
            if val == "":
                sc.set(m.e)
            else:
                sc.set(float(val) * m.e)
    except ValueError:
        sc.set("Error")

def click(event):
    key = event.widget
    text = key['text']
    oldValue = sc.get()
    newValue = oldValue + text
    sc.set(newValue)

def clr(event):
    sc.set("")

def backspace(event):
    entered = sc.get()
    sc.set(entered[:-1])

def calculate(event):
    answer = sc.get()
    try:
        if "^" in answer:
            answer = answer.replace("^", "**")
        answer = eval(answer)
        sc.set(answer)
    except Exception as e:
        sc.set("Error")

class Calculator:
    def __init__(self, txt, r, c, funcName, color="white"):
        self.var = Button(root, text=txt, padx=3, pady=5, fg="black", bg=color, width=10, font="cosmicsansms 12")
        self.var.bind("<Button-1>", funcName)
        self.var.grid(row=r, column=c)

# Set professional color scheme
button_color = "#f0f0f0"  # Light grey
function_color = "#d9d9d9"  # Slightly darker grey
highlight_color = "#0066cc"  # Blue for important functions

btn0 = Calculator("sin", 1, 0, sciCal, function_color)
btn1 = Calculator("cos", 1, 1, sciCal, function_color)
btn2 = Calculator("tan", 1, 2, sciCal, function_color)
btn3 = Calculator("log", 1, 3, sciCal, button_color)
btn4 = Calculator("ln", 1, 4, sciCal, button_color)
btn5 = Calculator("(", 2, 0, click, button_color)
btn6 = Calculator(")", 2, 1, click, button_color)
btn7 = Calculator("^", 2, 2, click, button_color)
btn8 = Calculator("√", 2, 3, sciCal, button_color)
btn9 = Calculator("!", 2, 4, sciCal, button_color)
btn10 = Calculator("π", 3, 0, sciCal, highlight_color)
btn11 = Calculator("1/x", 3, 1, sciCal, button_color)
btn12 = Calculator("deg", 3, 2, sciCal, button_color)
btn13 = Calculator("rad", 3, 3, sciCal, button_color)
btn14 = Calculator("e", 3, 4, sciCal, highlight_color)
btn15 = Calculator("/", 4, 0, click, function_color)
btn16 = Calculator("*", 4, 1, click, function_color)
btn17 = Calculator("-", 4, 2, click, function_color)
btn18 = Calculator("+", 4, 3, click, function_color)
btn19 = Calculator("%", 4, 4, click, function_color)
btn20 = Calculator("9", 5, 0, click, button_color)
btn21 = Calculator("8", 5, 1, click, button_color)
btn22 = Calculator("7", 5, 2, click, button_color)
btn23 = Calculator("6", 5, 3, click, button_color)
btn24 = Calculator("5", 5, 4, click, button_color)
btn25 = Calculator("4", 6, 0, click, button_color)
btn26 = Calculator("3", 6, 1, click, button_color)
btn27 = Calculator("2", 6, 2, click, button_color)
btn28 = Calculator("1", 6, 3, click, button_color)
btn29 = Calculator("0", 6, 4, click, button_color)
btn30 = Calculator("C", 7, 0, clr, "red")
btn31 = Calculator("⌦", 7, 1, backspace, "red")
btn32 = Calculator("00", 7, 2, click, button_color)
btn33 = Calculator(".", 7, 3, click, button_color)
btn34 = Calculator("=", 7, 4, calculate, highlight_color)

root.mainloop()
