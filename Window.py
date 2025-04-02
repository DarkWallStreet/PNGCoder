from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import ctypes
from key_creator import key_creator
# Checking libraries start --------------------
import subprocess
import sys
package = 'pillow'
subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
package = 'tqdm'
subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
# Checking libraries end ---------------
from coder import coder, decoder





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


# "Do you want to quit?" window
def close_window():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol('WM_DELETE_WINDOW', close_window)


label = Label(text='PNGCoder menu')
label.pack(anchor='n', pady=10)

is_gen_key_pressed = False
def generate_key_true():
    global is_gen_key_pressed
    if is_gen_key_pressed:
        is_gen_key_pressed = False
        button_start_decoding['state'] = ['abled']
    else:
        is_gen_key_pressed = True
        button_start_decoding['state'] = ['disabled']


checkbox_generate_key = ttk.Checkbutton(text='Generate a new key', command=generate_key_true)
checkbox_generate_key.pack(anchor='w', padx=20)
button_start_coding = ttk.Button(text='Code')
button_start_coding.pack(anchor='w', padx=20)
button_start_decoding = ttk.Button(text='Decode')
button_start_decoding.pack(anchor='w', padx=20)





# try:
#     a = open('key.json')
#     a.close()
# except:
#     print('Creating key')
#     key_creator()
#
# print('Start coding')
# code_path = coder(message='Hello world!')
# print('Start decoding')
# res = decoder(code_path=code_path)
























































root.mainloop()

