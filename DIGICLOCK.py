import tkinter as tkr
from datetime import datetime

root = tkr.Tk()
root.title("DIGITAL CLOCK")
root.geometry("800x400")
root.configure(bg='black')

label = tkr.Label(root, font=('Century Gothic', 75), background='black', foreground='green', padx=20, pady=20)
label.pack(expand=True)

def time():
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S %p')
    day_name = now.strftime('%A')
    date = now.strftime('%d/%m/%Y')
    string = f"{current_time}\n{day_name}\n{date}"
    label.config(text=string)
    label.after(1000, time)

def on_enter(event):
    label.config(foreground='gray')

def on_leave(event):
    label.config(foreground='green')

label.bind("<Enter>", on_enter)
label.bind("<Leave>", on_leave)

time()
root.mainloop()
