from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('500x500+1200+150')
root.title('My first tkinter app')
root.iconbitmap('py.ico')


def click():
    print('clicked')


# btn = Button(root, text='Push', command=click, width=10, font=('Arial', 10))
btn = Button(root, text='Push', justify='left', command=click)
btn.configure(width=10, height=1)
btn['font'] = ('Arial', 14)
btn.pack()

btn2 = ttk.Button(root, text='Push')
btn2.pack()

root.mainloop()
