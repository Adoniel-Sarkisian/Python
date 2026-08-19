# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))



# Add your event handler script here 

expression = ""  # store the current expression globally

def click_handler(event):
    global expression
    button = event.widget
    value = button.cget("text")

    if value == "C":
        expression = ""
        label.config(text="0")
    elif value == "=":
        try:
            safe_expression = expression.replace("x", "*")
            result = str(eval(safe_expression))
            label.config(text=result)
            expression = result  # allow chaining
        except Exception:
            label.config(text="Error")
            expression = ""
    else:
        expression += value
        label.config(text=expression)


main = tk.Tk()
main.title("Calculator")
main.config(bg="#E4E2E2")
main.geometry("271x342")
main.update_idletasks()

geometryX = 0
geometryY = 0

main.geometry("+%d+%d"%(geometryX, geometryY))
main.resizable(False, False)



style = ttk.Style(main)
style.theme_use("clam")

style.configure("button.TButton", background="#E4E2E2", foreground="#000", font=("", 16))
style.map("button.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button = ttk.Button(master=main, text="7", style="button.TButton")
button.bind("<Button-1>", click_handler)
button.place(x=27, y=111, width=45, height=39)

style.configure("button1.TButton", background="#E4E2E2", foreground="#000", font=("", 16))
style.map("button1.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button1 = ttk.Button(master=main, text="8", style="button1.TButton")
button1.bind("<Button-1>", click_handler)
button1.place(x=83, y=111, width=45, height=39)

style.configure("button2.TButton", background="#E4E2E2", foreground="#000", font=("", 16))
style.map("button2.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button2 = ttk.Button(master=main, text="9", style="button2.TButton")
button2.bind("<Button-1>", click_handler)
button2.place(x=140, y=111, width=45, height=39)

style.configure("button3.TButton", background="#E4E2E2", foreground="#000", font=("", 16))
style.map("button3.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button3 = ttk.Button(master=main, text="+", style="button3.TButton")
button3.bind("<Button-1>", click_handler)
button3.place(x=196, y=111, width=45, height=39)

style.configure("button4.TButton", background="#E4E2E2", foreground="#000", font=("", 16))
style.map("button4.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button4 = ttk.Button(master=main, text="4", style="button4.TButton")
button4.bind("<Button-1>", click_handler)
button4.place(x=27, y=167, width=45, height=39)

style.configure("button5.TButton", background="#E4E2E2", foreground="#000", font=("", 16))
style.map("button5.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button5 = ttk.Button(master=main, text="5", style="button5.TButton")
button5.bind("<Button-1>", click_handler)
button5.place(x=83, y=167, width=45, height=39)

style.configure("button6.TButton", background="#E4E2E2", foreground="#000", font=("", 16))
style.map("button6.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button6 = ttk.Button(master=main, text="6", style="button6.TButton")
button6.bind("<Button-1>", click_handler)
button6.place(x=140, y=167, width=45, height=39)

style.configure("button7.TButton", background="#E4E2E2", foreground="#000", font=("", 16))
style.map("button7.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button7 = ttk.Button(master=main, text="-", style="button7.TButton")
button7.bind("<Button-1>", click_handler)
button7.place(x=196, y=167, width=45, height=39)

style.configure("button8.TButton", background="#E4E2E2", foreground="#000", font=("", 16))
style.map("button8.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button8 = ttk.Button(master=main, text="1", style="button8.TButton")
button8.bind("<Button-1>", click_handler)
button8.place(x=27, y=223, width=45, height=39)

style.configure("button9.TButton", background="#E4E2E2", foreground="#000", font=("", 16))
style.map("button9.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button9 = ttk.Button(master=main, text="2", style="button9.TButton")
button9.bind("<Button-1>", click_handler)
button9.place(x=83, y=223, width=45, height=39)

style.configure("button10.TButton", background="#E4E2E2", foreground="#000", font=("", 16))
style.map("button10.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button10 = ttk.Button(master=main, text="3", style="button10.TButton")
button10.bind("<Button-1>", click_handler)
button10.place(x=140, y=223, width=45, height=39)

style.configure("button11.TButton", background="#E4E2E2", foreground="#000", font=("", 16))
style.map("button11.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button11 = ttk.Button(master=main, text="/", style="button11.TButton")
button11.bind("<Button-1>", click_handler)
button11.place(x=196, y=223, width=45, height=39)

style.configure("button12.TButton", background="#E4E2E2", foreground="#000", font=("", 16))
style.map("button12.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button12 = ttk.Button(master=main, text=".", style="button12.TButton")
button12.bind("<Button-1>", click_handler)
button12.place(x=27, y=279, width=45, height=39)

style.configure("button13.TButton", background="#E4E2E2", foreground="#000", font=("", 16))
style.map("button13.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button13 = ttk.Button(master=main, text="0", style="button13.TButton")
button13.bind("<Button-1>", click_handler)
button13.place(x=83, y=279, width=45, height=39)

style.configure("button14.TButton", background="#E4E2E2", foreground="#000", font=("", 16))
style.map("button14.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button14 = ttk.Button(master=main, text="=", style="button14.TButton")
button14.bind("<Button-1>", click_handler)
button14.place(x=140, y=279, width=45, height=39)

style.configure("button15.TButton", background="#E4E2E2", foreground="#000", font=("", 16))
style.map("button15.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button15 = ttk.Button(master=main, text="x", style="button15.TButton")
button15.bind("<Button-1>", click_handler)
button15.place(x=196, y=279, width=45, height=39)

style.configure("label.TLabel", background="#E4E2E2", foreground="#000", font=("TkDefaultFont", 30), anchor="e")
label = ttk.Label(master=main, text="0", style="label.TLabel")
label.configure(anchor="e")
label.place(x=27, y=27, width=223, height=54)



main.mainloop()