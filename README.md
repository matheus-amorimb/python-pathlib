# Pathlib


Manipulando arquivos e diretórios com PathLib

``` python
from pathlib import path
```
## Referências

[Pathlib - Official Documentation](https://docs.python.org/3/library/pathlib.html)

## Introdução

Pathlib é uma biblioteca que trabalha com caminhos do sistema de arquivos orientados a objetos.

Este módulo oferece classes que representam caminhos de sistema de arquivos com semântica apropriada para diferentes sistemas operacionais.

## Principais funcionalidades

### Verificando o Path

```python
Path() #retorna o caminho relativo

Path().absolute() #retorna o caminho absoluto

Path() == Path().absolute() #retorna False
```

**Importante**: O caminho retornando em `Path()` se trata do caminho na qual o programa foi chamado, não o caminho na qual o arquivo se encontra.


```python
from pathlib import Path

path_atual = Path() #retorna o caminho relativo
files = path_atual / 'files'

absoluto = files.absolute()

print(absoluto)

➜ python-pathlib (main) ✗ python3 files/main.py
#/home/matheus/data-science/Python/python-pathlib/files

➜ files (main) ✗ python3 main.py      
#/home/matheus/data-science/Python/python-pathlib/files/files

➜ python-pathlib (main) ✗ exa -T   
#python-pathlib
#│
#├── files
#│  └── main.py
#├── README.md
#├── test.txt
#└── with_open_as.py
```

### Manipulando arquivos

```python
p =  Path('teste.txt')

p.touch() #cria um arquivo

p.unlink() #remove um arquivo

```