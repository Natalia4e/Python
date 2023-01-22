
from random import choices

amount = int(input())
new_list = choices(range(1,amount+1), k=amount)
print(new_list)

def identical_numb(any_list):
    temp = []
    for x in any_list:
        if x not in temp:
            temp.append(x)
    any_list= temp
    print(temp)

print(identical_numb(new_list))