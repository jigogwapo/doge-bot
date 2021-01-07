from jeje_map import jeje_letter_map
import random

def jejenizer(text):
    new_text = ''
    for i in text:
        if i.lower() in jeje_letter_map.keys():
            new_text += random.choice(jeje_letter_map[i.lower()])
        else:
            new_text += i
    return new_text