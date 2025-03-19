from tkinter import *
from tkinter import messagebox
import ctypes
from key_creator import key_creator
import subprocess
import sys

package = 'pillow'
subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])





# Creating a window (name & icon)
root = Tk()
root.title('PNGCoder')
root.iconbitmap(default='key_icon.ico')

# Window size
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
width = screensize[0]//4
height = (screensize[1]//3) * 2
size = width, height
root.geometry(f'{width}x{height}+{(screensize[0]-width)//2}+{(screensize[1]-height)//2}')



def close_window():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol('WM_DELETE_WINDOW', close_window)




label = Label(text='Hello World')
label.pack()













































root.mainloop()

