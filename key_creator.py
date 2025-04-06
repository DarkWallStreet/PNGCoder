from random import randint
import json



space = ' '
sym = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '|', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '}', '~', '÷']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ru = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
en = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alp = sym + num + ru + en




def key_creator(file_name: str = 'key'):
    global alp
    variants = []
    i = 0
    f = randint(10, 25)
    while i != ((len(alp) * f) + 9):
        n = "#{:02x}{:02x}{:02x}".format(randint(0, 255), randint(0, 255), randint(0, 255)).upper()
        if n not in variants and n != '#000000':
            variants.append(n)
            i += 1
    dict = {space:variants[:5]}
    variants = variants[5:]
    for item in alp:
        z = randint(5, f)
        dict[item] = variants[:z]
        variants = variants[z:]
    dict['unknown'] = variants[:2]
    variants = variants[2:]
    dict['\n'] = variants[:2]
    with open(f'{file_name}.json', 'w+') as file:
        json.dump(dict, file)
    return f'{file_name}.json'