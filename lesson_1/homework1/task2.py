# 2.Напишите программу, для проверки ложности утверждения (w^z) v ( x->( y ^ z))
print(" x y z w")
for x in range (2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not ((w and z)) or not y or (not x == (not w)):
                    print (x, y, z, w)
