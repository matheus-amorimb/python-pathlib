import os
import os.path

if os.path.exists('test.txt'):
    with open('test.txt', 'w') as text_file:
        text_file.write('Esse é um arquivo de teste')

with open('test.txt') as text_file:
    content = text_file.read()
    print(content)