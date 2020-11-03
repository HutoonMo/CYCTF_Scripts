#!/usr/bin/python
# -*- coding: utf-8 -*-
# read file content into a variable

with open('flag.txt') as file:
    flag = ' '.join([l.rstrip() for l in file])

  # print(flag)

# convert the content to morse code characters

flag = flag.replace('?M6', '.').replace('D', '-')



# implemintation of morse code dycrption

def morse(flag):
    d = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        ' ': '.....',
        '?': '.----.',
        '!': '-.-.--',
        '@': '.--.-.',
        '.': '.-.-.-',
        '_': '..--.-',
        '': '',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '8': '---..',
        '9': '----.',
        '0': '-----'


        }

    flag = flag.upper()
    translation = ''
    # Swap key/values in d:
    d_encrypt = dict([(v, k) for k, v in d.items()])
    # Morse code is separated by empty space chars
    flag = flag.split(' ')
    for x in flag:
    	translation += d_encrypt.get(x)
    return translation.strip()

print (morse(flag))