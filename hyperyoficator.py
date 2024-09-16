import sys

def yoficate(text):
    yoficated_text = ''
    for c in text:
        if c in 'ёЁ':
            yoficated_text += '¨'
        elif c == '\n':
            yoficated_text += c
        else:
            yoficated_text += ' '
    return yoficated_text

text = sys.stdin.read()

result = yoficate(text)

print(result)