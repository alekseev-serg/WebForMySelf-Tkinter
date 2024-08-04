from tkinter import *
import time

root = Tk()
root.geometry('500x500+1200+150')
root.title(f'Counter')


def check_time():
    btn_time['text'] = time.strftime('%H:%M:%S')
    # print(time.strftime('%H:%M:%S'))


clicks = 0


def counter():
    global clicks
    clicks += 1
    root.title(f'Counter {clicks}')


btn_time = Button(root, text='Check Time', command=check_time)
btn_time.pack(anchor=CENTER)

btn_count = Button(root, text='Counter', command=counter)
btn_count.pack(anchor=CENTER)

root.mainloop()
