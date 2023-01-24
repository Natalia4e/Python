# Напишите программу вычисления арифмитического выражения заданного строкой. Используйте операции +,-,/,*
# приоритет операци стандартный . Добавьте скобки приоритет операций меняется

def sort_s(string):
    spl = string.split()
    fn_spl= []
    i = 0
    while i < len(spl):
        if spl[i] == "(":
            bracket = spl.index(")")
            fn_spl.append(spl[i+1:bracket])
            i = bracket
        else:
            fn_spl.append(spl[i])
            i = i+1
    return fn_spl


d = input("Введите данные")
print(sort_s(d))