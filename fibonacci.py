import tkinter as tk

window = tk.Tk()
window.title("fibonacci window")
window.geometry("300x200")



#线性递归
def fibonacci(x): #普通线性递归
    if x < 1:
        print('error!') #小于一出错
    elif x < 3:
        return 1 #小于3的都是1
    else:
        return fibonacci (x-1) + fibonacci (x-2) #第n个是第n-1+第n-2的

def ett1():
    txt.insert('insert', fibonacci(int(ent.get())))


#尾递归
def fibonacci_enhance(count, number_1 = 1, number_2 = 1,  c = 3):
    if count < 1:
        print('error!')
    elif count < 3:
        return 1
    else:
        if count == c:
            return number_1 + number_2
        else:
            return fibonacci_enhance(count, number_1 = number_2, number_2 = number_1+number_2, c = c+1) #同事改变count和数字两个变量

def ett2():
    txt.insert('insert', fibonacci_enhance(int(ent.get())))


ent = tk.Entry(window, show = None)
ent.pack()
btn_1 = tk.Button(window, text='线性递归', width=15, height=2, command = ett1)
btn_1.pack()
btn_2 = tk.Button(window, text='尾递归', width=15, height=2, command = ett2)
btn_2.pack()
txt = tk.Text(window, height = 2)
txt.pack()

window.mainloop()
