from PIL import Image
import json
from random import randint

def coder(key_file: str = 'key.json', message: str = "Hello World", file_name: str = 'code.png'):
    with open(f'{key_file}', 'r+') as file:
        key = json.load(file)
    png = []
    for letter in message:
        if letter == ' ':
            png.append(key[letter][0][randint(0, 2)])
        elif letter not in key.keys():
            letter = 'unknown'
            png.append(key[letter][randint(0, 1)])
        else:
            png.append(key[letter][randint(0, 1)])
    img = Image.new('RGB', [max(len(message.split('\n'), key = len), len(message.split('\n')))], 'black')


png = coder()