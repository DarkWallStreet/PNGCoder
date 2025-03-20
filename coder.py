
from PIL import Image, ImageDraw
import json
from random import randint
import os


def coder(key_file: str = 'key.json', message: str = "Hello World! \nThis code is the best\nI love this script228", file_path: str = f'{os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')}/', file_name: str = 'code'):
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
    img.save(f'{file_path}{file_name}.png')



def decoder(key_file: str = 'key.json', file_path: str = f'{os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')}/code.png'):
    with open(f'{key_file}', 'r+') as file:
        key = json.load(file)
    pixs = list(key.values())
    image = Image.open(f'{file_path}')
    picwidth = image.size[0]
    picheight = image.size[1]
    im = image.load()
    res = ''
    for y in range(picheight):
        for x in range(picwidth):
            pix = im[x,y]
            for i in pixs:
                if list(pix) in i:
                    letter = list(key.keys())[pixs.index(i)]
                    if letter == 'unknown': letter = '¿'
                    res += letter
    return res

