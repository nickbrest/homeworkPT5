# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.

from os import path
from itertools import groupby, starmap


def compr_rle(text, text_rle):
    if path.exists(text):
         with open(text, 'r', encoding='utf-8') as file_1, open(text_rle, 'a', encoding='utf-8') as file_2:
            for i in file_1:
                file_2.write(''.join([f'{len(list(qv))}{letter}' for letter, qv in groupby(i)]))
    else:
        print('Файл не существует!')

def decompr_rle(text_rle):
    if path.exists(text_rle):
        with open(text_rle, 'r', encoding='utf-8') as file:
            string = ''
            for i in file:
                dig_letters = []
                for j in i.strip():
                    if j.isdigit():
                        string += j
                    else:
                        dig_letters.append([int(string), j])
                        string = ''
                print(''.join(starmap(lambda x, y: x * y, dig_letters)))
    else:
        print('Файл не существует!')


command = str.upper(input('Введите "С" для запуска сжатия или "D" для декодирования: '))

if command == 'C':
    compr_rle(input('Введите имя файла с исходным текстом: '), input('Введите имя файла для записи данных: '))
elif command == 'D':
    decompr_rle(input('Введите имя файла для декодирования: '))
else:
    print('Команда не найдена')
