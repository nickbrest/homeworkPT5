# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.

from random import choices


def rand_text(numb, letters):
    result = []
    for i in range(numb):
        temp = choices(letters, k=3)
        result.append("".join(temp))
    return " ".join(result)

N = int(input("Введите количество слов: "))
text = input("Введите набор символов: ")
texts = rand_text(N, text)
print(texts)
letters = input("Введите удаляемый текст: ")


print(' '.join(list(filter(lambda x: letters not in x, texts.split(' ')))))

