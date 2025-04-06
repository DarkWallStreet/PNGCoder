from PIL import Image, ImageDraw
import json
from random import randint
import datetime
from tqdm import tqdm
import os

def coder(key_file: str = 'key.json', message: str = "Hello World!", code_path: str = 'Codes/', code_name: str = f'Code_{datetime.datetime.now().date()}_{datetime.datetime.now().time().hour}-{datetime.datetime.now().time().minute}-{datetime.datetime.now().time().second}', file_path: str = None):
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
    for letter in tqdm(message, desc='Coding', colour='#00f058'):
        if letter == ' ':
            codes.append(key[letter][randint(0, len(key[letter])-1)])
        elif letter not in key.keys():
            letter = 'unknown'
            codes.append(key[letter][randint(0, len(key[letter])-1)])
        else:
            codes.append(key[letter][randint(0, len(key[letter])-1)])
    n = 2
    if len(message) > 10:
        n = int((len(message)**0.5)+1)
    img = Image.new('RGB', ((len(message)//n)+1, n), 'black')
    idraw = ImageDraw.Draw(img)
    i = 0
    for y in tqdm(range(n), desc='Writing in picture', colour='#00f058'):
        for x in range((len(message)//n)+1):
            try:
                idraw.rectangle((x, y, x, y), fill=codes[i])
                i+=1
            except: pass
    try:
        img.save(f'{code_path}{code_name}.png')
    except:
        os.mkdir(f'{code_path}')
        img.save(f'{code_path}{code_name}.png')
    return f'{code_path}{code_name}.png'



def decoder(key_file: str = 'key.json', code_path: str = f'Codes/code.png'):
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
    for y in tqdm(range(picheight), desc='Decoding', colour='#00f058'):
        for x in range(picwidth):
            pix = im[x,y]
            pix = "#{:02x}{:02x}{:02x}".format(pix[0], pix[1],pix[2]).upper()
            for i in pixs:
                if pix in i:
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
        try:
            os.mkdir('Decoded_files')
        except: pass
        with open(f'Decoded_files/{file_name[1:]}', 'wb+') as file:
            file_data = file_data[1:]
            file_data = bytes.fromhex(file_data)
            file.write(file_data)
    return res