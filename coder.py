
from PIL import Image, ImageDraw
import json
from random import randint
import os

def coder(key_file: str = 'key.json', message: str = "Hello World! \nThis code is the best\nI love this script228", code_path: str = f'{os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')}/', code_name: str = 'code', file_path: str = None):
    message = message.replace('|', '÷')
    if file_path != None:
        file_path = file_path.replace('\\', '/')
        with open(f"{file_path}", "rb") as file:
            file_binary = file.read()
        file_encoded = file_binary.hex()
        message = message + '|' + str(file_path.split('/')[-1]) + '|' + file_encoded
    with open(f'{key_file}', 'r+') as file:
        key = json.load(file)
    codes = []
    for letter in message:
        if letter == ' ':
            codes.append(key[letter][randint(0, 4)])
        elif letter not in key.keys():
            letter = 'unknown'
            codes.append(key[letter][randint(0, 1)])
        else:
            codes.append(key[letter][randint(0, 1)])
    n = 2
    if len(message) > 10:
        n = int((len(message)**0.5)+1)
    img = Image.new('RGB', ((len(message)//n)+1, n), 'black')
    idraw = ImageDraw.Draw(img)
    i = 0
    for y in range(n):
        for x in range((len(message)//n)+1):
            try:
                idraw.rectangle((x, y, x, y), fill=tuple(codes[i]))
                i+=1
            except: pass
    img.save(f'{code_path}{code_name}.png')



def decoder(key_file: str = 'key.json', code_path: str = f'{os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')}/code.png'):
    with open(f'{key_file}', 'r+') as file:
        key = json.load(file)
    pixs = list(key.values())
    image = Image.open(f'{code_path}')
    picwidth = image.size[0]
    picheight = image.size[1]
    im = image.load()
    res = ''
    fl = 0
    file_name = ''
    file_data = ''
    for y in range(picheight):
        for x in range(picwidth):
            pix = im[x,y]
            for i in pixs:
                if list(pix) in i:
                    letter = list(key.keys())[pixs.index(i)]
                    if letter == '|':
                        fl += 1
                    elif letter == '÷': letter = '|'
                    elif letter == 'unknown': letter = '¿'
                    if fl == 0:
                        res += letter
                    if fl == 1:
                        file_name += letter
                    if fl == 2:
                        file_data += letter
    if file_name != '':
        with open(f'{file_name[1:]}', 'wb+') as file:
            file_data = file_data[1:]
            file_data = bytes.fromhex(file_data)
            file.write(file_data)
    return res

