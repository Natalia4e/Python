from random import randrange
Some_list = list(range(33,45))

print (Some_list)

for i, val in enumerate (Some_list):
    j = randrange (len(Some_list))
    Some_list[i], Some_list[j] = Some_list[j], Some_list[i]


print (Some_list)