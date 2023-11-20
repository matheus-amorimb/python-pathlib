from pathlib import Path

path_atual = Path() #retorna o caminho relativo
files = path_atual / 'files' #concatena caminhos

absoluto = files.absolute() #retorna o caminho absoluto

print(absoluto)

p =  Path('teste.txt')

p.touch() #cria um arquivo

p.unlink() #remove um arquivo


path = Path("files/pasta_0/")
print(list(path.parents))

print(path.parts)

print(path.absolute().parent)

print(list(path.absolute().parents))

