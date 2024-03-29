import random

jeje_letter_map = {
  "a": ['aA', '@', 'ä', 'ã', 'â', 'A', 'a', '4', 'Aa', '/-\\'],
  "b": ['B', 'V', 'b', 'v', 'bH', 'Bv'],
  "c": ['c', 'C', 'cK', 'cH', 'Ck'],
  "d": ['d', 'D', 'Dd', 'dH', 'Dh'],
  "e": ['3', 'E', 'Ee', 'eE', 'è', 'ë', 'ē'],
  "f": ['F', 'f', 'fH', 'fF', 'FF'],
  "g": ['g', 'G', 'Gh', 'gH', '6', '9'],
  "h": ['h', 'H', 'hH', 'j', 'J', '|-|'],
  "i": ['i', 'I', '!', '1', '|'],
  "j": ['j', 'J', 'Jh', 'jH', 'Jj'],
  "k": ['k', 'K', 'Kk', 'kH', 'Kh'],
  "l": ['l', 'L', 'lH', 'Lh'],
  "m": ['m', 'M', 'mM', 'mH', 'Mh'],
  "n": ['n', 'N', 'nN', 'nH', 'Nh'],
  "o": ['0', 'o', 'Oo', 'O', 'oH', '()', 'ö', 'ø'],
  "p": ['p', 'P', 'Pp', 'pH', 'Ph'],
  "q": ['q', 'Q', 'Qq', 'qH', 'Qh'],
  "r": ['r', 'R', 'rR', 'rH', 'Rh'],
  "s": ['S', 'Z', 'zZ', '$', 's', 'sS', '5'],
  "t": ['T', 't', '+', 'Tt', 'tT', 'tH'],
  "u": ['u', 'U', 'uU', 'uH', 'û', 'ü', 'Uh', '|_|'],
  "v": ['v', 'V', 'vV', 'vH', 'Vh', '\\/'],
  "w": ['w', 'W', 'wW', 'wH', 'Wh'],
  "x": ['x', 'X', 'xX', 'xH', 'Xh'],
  "y": ['y', 'Y', 'yY', 'yH', 'Yh'],
  "z": ['z', 'Z', 'zH', 'Zh', 'zzZ'],
}

def jejenizer(text):
    new_text = ''
    for i in text:
        if i.lower() in jeje_letter_map.keys():
            new_text += random.choice(jeje_letter_map[i.lower()])
        else:
            new_text += i
    return new_text