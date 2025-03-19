from PIL import Image
import json

def coder(key_file: str = 'key.json', text: str = "Hello World"):
    with open(f'{key_file}', 'r+') as file:
        key = json.loads(file)
