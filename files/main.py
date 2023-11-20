from pathlib import Path

path_atual = Path() #retorna o caminho relativo
files = path_atual / 'files'

absoluto = files.absolute()

print(absoluto)

p =  Path('teste.txt')

p.touch()



