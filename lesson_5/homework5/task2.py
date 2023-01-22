#2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.Алгоритм RLE 2 функции
# 1 руками вводим ( сжали инфу и записали в файл)2)дали имя берем из файла и раскодируем lambda выходные данные в терминале

with open('text_words.txt', 'w') as data:
    data.write('aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaavvvvvvvvvvvbbwwPPuuuTTYyWWQQ')

with open('text_words.txt', 'r') as data:
    string = data.readline()

def encode(s):
    encoding = "" 
    i = 0
    # считаем количество одинаковых символов 
    while i < len(s):
        count = 1
        while i+1  < len (s) and s[i] == s[i+1]:
            count = count + 1
            i = i+1
        # encoding =  символ + его количество
        encoding += str(count) + s[i]
        i = i+1
    return encoding

s = string 

print (encode(s))



