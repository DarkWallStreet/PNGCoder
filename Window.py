from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showerror, showinfo
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


version = '1.1.0'




# Creating a window (name & icon)
root = Tk()
root.title('PNGCoder')
root.iconbitmap(default='key_icon.ico')

# Window size
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
width = screensize[0] // 4
height = (screensize[1] // 3) * 2
size = width, height
root.geometry(f'{width}x{height}+{(screensize[0] - width) // 2}+{(screensize[1] - height) // 2}')


# "Do you want to quit?" window
def close_window():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


root.protocol('WM_DELETE_WINDOW', close_window)

label = Label(text='PNGCoder menu', font='bold')
label.pack(anchor='n', pady=int(0.02 * height))

notebook = ttk.Notebook()
notebook.pack()

# Coding functions

# Need to create new key for coding
is_gen_key_pressed = False


def generate_key_true():
    global is_gen_key_pressed
    global button_select_key_file
    if is_gen_key_pressed:
        is_gen_key_pressed = False
        button_select_key_file['state'] = ['abled']
    else:
        is_gen_key_pressed = True
        button_select_key_file['state'] = ['disabled']


# Need to select file to code
def coding_file_selector():
    global coding_file_path
    path = filedialog.askopenfilename()
    if path == '':
        path = 'None'
    coding_file_path.set(value=path)


# Need to select key file in coding
def key_file_selector():
    global key_file_path
    path = filedialog.askopenfilename()
    if path == '':
        path = 'None'
    key_file_path.set(value=path)


# Need to start coding process
def start_coding():
    global is_gen_key_pressed
    global message_editor
    global coding_file_path
    global new_key_name
    global key_file_path
    global new_code_name
    code_name = new_code_name.get()
    code_key = key_file_path.get()
    new_name = new_key_name.get()
    file = coding_file_path.get()
    message = message_editor.get("1.0", "end")
    if is_gen_key_pressed:
        if new_name == '':
            new_name = 'key'
        code_key = key_creator(file_name=new_name)
    if file == 'None':
        file = None
    if code_key == 'None':  # No Key Error
        showerror(title="Error", message="Select key file or create new one")
        return 0
    if code_name != '':
        coder(key_file=code_key, message=message, file_path=file, code_name=code_name)
    else:
        coder(key_file=code_key, message=message, file_path=file)
    showinfo(title='Success', message='Coding completed successfully')


# Decoding functions

# Need to select key file in decoding
def decode_key_file_selector():
    global decode_key_file_path
    path = filedialog.askopenfilename()
    if path == '':
        path = 'None'
    decode_key_file_path.set(value=path)


# Need to select coded file
def decoding_file_selector():
    global code_file_path
    path = filedialog.askopenfilename()
    if path == '':
        path = 'None'
    code_file_path.set(value=path)


# Need to start decoding process
def start_decoding():
    global decode_key_file_path
    global code_file_path
    decode_key = decode_key_file_path.get()
    code_file = code_file_path.get()
    if decode_key == 'None':
        showerror(title="Error", message="Select key")
        return 0
    if code_file == 'None':
        showerror(title="Error", message="Select PNGcode")
        return 0
    decoded_message = decoder(key_file=decode_key, code_path=code_file)
    if decoded_message != '':
        showinfo(title='Success', message=f'Decoding completed successfully\n\nMessage: {decoded_message}')
    else:
        showinfo(title='Success', message='Decoding completed successfully')


# Buttons and other USEFUL elements

# Coding block
coding_frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])

label_frame_name_coding = Label(coding_frame, text='Coding menu', font='bold')
label_frame_name_coding.pack(anchor='w')

label_message = Label(coding_frame, text='Enter your text message')
label_message.pack(anchor='w')
message_editor = ScrolledText(master=coding_frame, wrap='word', height=5)
message_editor.pack(anchor='w')

coding_file_path = StringVar(value='None')
button_select_file = ttk.Button(coding_frame, text='Select file', command=coding_file_selector)
button_select_file.pack(anchor='w', pady=7)
label_your_file = Label(coding_frame, text='Selected file:')
label_your_file.pack(anchor='w')
label_your_file_dynam = Label(coding_frame, textvariable=coding_file_path, background='Light grey')
label_your_file_dynam.pack(anchor='w')

key_file_path = StringVar(value='None')
button_select_key_file = ttk.Button(coding_frame, text='Select key', command=key_file_selector)
button_select_key_file.pack(anchor='w', pady=7)
label_key_file = Label(coding_frame, text='Selected key file:')
label_key_file.pack(anchor='w')
label_key_file_dynam = Label(coding_frame, textvariable=key_file_path, background='Light grey')
label_key_file_dynam.pack(anchor='w')

new_key_name = StringVar()
checkbox_generate_key = ttk.Checkbutton(coding_frame, text='Generate a new key', command=generate_key_true)
checkbox_generate_key.pack(anchor='w', pady=int(0.02 * height))
label_key_name = Label(coding_frame, text='Enter NEW key name')
label_key_name.pack(anchor='w')
key_name_editor = Entry(master=coding_frame, textvariable=new_key_name)
key_name_editor.pack(anchor='w')

new_code_name = StringVar()
label_key_name = Label(coding_frame, text='Enter code file name')
label_key_name.pack(anchor='w')
code_name_editor = Entry(master=coding_frame, textvariable=new_code_name)
code_name_editor.pack(anchor='w')

button_start_coding = ttk.Button(coding_frame, command=start_coding, text='Code')
button_start_coding.pack(anchor='w', padx=int(0.04 * width), pady=int(0.02 * height))

coding_frame.pack(anchor='w', padx=int(0.04 * width))

# Decoding block
decoding_frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])

label_frame_name_decoding = Label(decoding_frame, text='Decoding menu', font='bold')
label_frame_name_decoding.pack(anchor='w')

code_file_path = StringVar(value='None')
button_select_code_file = ttk.Button(decoding_frame, text='Select coded file', command=decoding_file_selector)
button_select_code_file.pack(anchor='w', pady=7)
label_code_file = Label(decoding_frame, text='Selected file:')
label_code_file.pack(anchor='w')
label_code_file_dynam = Label(decoding_frame, textvariable=code_file_path, background='Light grey')
label_code_file_dynam.pack(anchor='w')

decode_key_file_path = StringVar(value='None')
button_select_decode_key_file = ttk.Button(decoding_frame, text='Select key', command=decode_key_file_selector)
button_select_decode_key_file.pack(anchor='w', pady=7)
label_decode_key_file = Label(decoding_frame, text='Selected key file:')
label_decode_key_file.pack(anchor='w')
label_decode_key_file_dynam = Label(decoding_frame, textvariable=decode_key_file_path, background='Light grey')
label_decode_key_file_dynam.pack(anchor='w')

decoding_label0 = ttk.Label(master=decoding_frame, text='File will be decoded in directory of this program',foreground='dark grey')
decoding_label0.pack(anchor='w', pady=int(0.02 * height))
decoding_label1 = ttk.Label(master=decoding_frame, text='Decoding can take a lot of time', foreground='dark grey')
decoding_label1.pack(anchor='w')
button_start_decoding = ttk.Button(master=decoding_frame, command=start_decoding, text='Decode')
button_start_decoding.pack(anchor='w', padx=int(0.04 * width))

decoding_frame.pack(anchor='w', padx=int(0.04 * width), pady=int(0.03 * height))

notebook.add(coding_frame, text='Coding')
notebook.add(decoding_frame, text='Decoding')

version_label = ttk.Label(master=root, text=version, foreground='dark grey')
version_label.pack(anchor='se', pady=int(0.02 * height))

root.mainloop()
