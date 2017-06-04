import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("500x200")

var = tk.StringVar()


l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 18), width=20
 , height=2)
l.pack()

on_hit = False


def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set("you don't hit me")


btn = tk.Button(window, text='click button', width=8, height=2, command=hit_me)

btn.pack()


window.mainloop()
