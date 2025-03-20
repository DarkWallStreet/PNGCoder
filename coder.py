from ctypes import c_double

from PIL import Image, ImageDraw
import json
from random import randint
import os

def coder(key_file: str = 'key.json', message: str = "Hello World! \nThis code is the best\nI love this script228", file_name: str = 'code'):
    with open(f'{key_file}', 'r+') as file:
        key = json.load(file)
    codes = []
    for letter in message:
        if letter == ' ':
            codes.append(key[letter][0][randint(0, 2)])
        elif letter not in key.keys():
            letter = 'unknown'
            codes.append(key[letter][randint(0, 1)])
        else:
            codes.append(key[letter][randint(0, 1)])
    n=2
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
    img.save(f'{os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')}/{file_name}.png')

