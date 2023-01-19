"""
este é código simples, primeiro lista todos os arquivos na pasta files, após mostra a quantidade de arquivos na pasta
files, para que o laço while não vire um loop infinito, no laço while, enquanto tiver arquivo, o laço for pegará 
esse arquivo, renomeará e inserirá na pasta renamed
"""

import os

files_dir = os.listdir('./files')
size_folder = len(files_dir)
size = 0
i = 0
j = 0

while size <= size_folder:
    for file in files_dir:
        os.rename(f'./files/{files_dir[i]}', f'./renamed/file_renamed{j}.txt')
        i += 1
        j += 1
        size += 1
