from tkinter import *

root = Tk()
root.geometry('500x500+1200+150')
root.title('My first tkinter app')
root.iconbitmap('py.ico')
root.resizable(False, False)
# root.config(background='white')
root['bg'] = 'yellow'
root.mainloop()
