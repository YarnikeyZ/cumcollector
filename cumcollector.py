from tkinter import *
from tkinter import ttk
from configparser import ConfigParser
from os.path import abspath as wd

config = ConfigParser()
config.read(f'{wd("")}/config.ini')

style = dict(config["style"])
style.update({
    'text-size-big': int(style["text-size-big"]),
    'text-size-mid': int(style["text-size-mid"]),
    'text-size-small': int(style["text-size-small"]),
    'button-size-main': int(style["button-size-main"]),
})

tocalc = None
equal = None
str_tocalc = "9 + 10 = "
str_equal = "21"

def calcEqual():
    global tocalc, equal, str_tocalc, str_equal
    if str_tocalc == "":
        result = ""
    else:
        try:
            result = eval(str_tocalc.replace(' ', '').replace('=', ''))
            if result % 1 == 0:
                result = int(result)
            result = str(result).rjust(12, " ")
            if len(result) > 12 or len(str_tocalc) > 94:
                regPress("ON/C")
                result = ""
        except SyntaxError:
            result = "?"
    return result

def regPress(text):
        global tocalc, equal, str_tocalc, str_equal
        try:
            int(text)
            str_tocalc += text
        except ValueError:
            pass
        if text == "ON/C" or text == "CE":
            str_tocalc = ""
        if text == "+" or text == "-" or text == "*" or text == "/" or text == "%":
            str_tocalc += f" {text} "
        str_equal = calcEqual()
        tocalc.configure(text=str_tocalc+" = ")
        equal.configure(text=str_equal)


def addButton(text, row, column, rowspan, columnspan, colortype):
    button = Button(text=text, command=lambda: regPress(text))
    color = style['button-main'] if colortype == 0 else style['button-secondary'] if colortype == 1 else style['button-accent']
    button.configure(
        width=style['button-size-main']*4*columnspan,
        height=style['button-size-main']*rowspan,
        font=(style['font'], style['text-size-mid']),
        bg=color,
        fg=style['text-main'],
    )
    button.grid(padx=5, pady=5, row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky=NE)


def main():
    global tocalc, equal, str_tocalc, str_equal
    window = Tk()
    window.title("Cumcollector")
    window.geometry("320x375")
    window.resizable(width=False, height=False)
    window.configure(bg=style['bg'])

    tocalc = ttk.Label(background=style['bg'], foreground=style['text-secondary'], text=str_tocalc, font=(style['font'], style['text-size-small']))
    tocalc.grid(row=0, column=0, columnspan=5, sticky=NE)

    equal = ttk.Label(background=style['bg'], foreground=style['text-main'], text=str_equal, font=(style['font'], style['text-size-big']))
    equal.grid(row=1, column=0, columnspan=5, sticky=NE)

    addButton("MRC", 2, 0, 1, 1, 1), addButton("M-", 2, 1, 1, 1, 1), addButton("M+", 2, 2, 1, 1, 1), addButton("CE" , 2, 3, 1, 1, 1), addButton("ON/C", 2, 4, 1, 1, 2)
    addButton("7"  , 3, 0, 1, 1, 0), addButton("8" , 3, 1, 1, 1, 0), addButton("9" , 3, 2, 1, 1, 0), addButton("%"  , 3, 3, 1, 1, 1), addButton("sqrt", 3, 4, 1, 1, 1)
    addButton("4"  , 4, 0, 1, 1, 0), addButton("5" , 4, 1, 1, 1, 0), addButton("6" , 4, 2, 1, 1, 0), addButton("+/-", 4, 3, 1, 1, 1), addButton("/"   , 4, 4, 1, 1, 1)
    addButton("1"  , 5, 0, 1, 1, 0), addButton("2" , 5, 1, 1, 1, 0), addButton("3" , 5, 2, 1, 1, 0), addButton("+"  , 5, 3, 3, 1, 1), addButton("*"   , 5, 4, 1, 1, 1)
    addButton("0"  , 6, 0, 1, 1, 0), addButton("." , 6, 1, 1, 1, 0), addButton("=" , 6, 2, 1, 1, 0),                                  addButton("-"   , 6, 4, 1, 1, 1)

    window.mainloop()

if __name__ == '__main__':
    main()
