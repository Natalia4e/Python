#1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.(sample попробовать)
# in Number of words: 10
# out авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

import random

word = "абв"

num = (int(input("Введите количество слов : ")))
list_word = []
for i in range(num):
    random_word = random.sample(word, 3)
    list_word.append("".join(random_word))

print(" ".join(list_word))

list_word2 = list(filter(lambda x: word not in x, list_word))
print(" ".join(list_word2))


