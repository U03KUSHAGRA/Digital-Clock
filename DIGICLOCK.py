import tkinter as tkr
from time import strftime

root = tkr.Tk()
root.title ("DIGITAL CLOCK")
label = tkr.Label(root, font=('Courier', 75, 'bold'), background ='white', foreground='black')
label.pack(anchor='center')
def time():
    string = strftime('%H:%M:%S %p\n %D')
    label.config(text=string)
    label.after(1000,time)
time()
root.mainloop()