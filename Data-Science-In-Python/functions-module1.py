def addNumbers (x, y, z = None, flag = False):
    if (flag):
        print("Flag is True!")
    if z == None:
        return x + y
    else:
        return x + y + z
 
def num3 (q, w, e=None):
    if e is None:
        return q + w
    else:
        return q + w + e 

print(num3(3, 55))
print(num3(3, 55, 21))
print(addNumbers(23, 9, 18))


see = input("Enter three numbers: ")
parts = see.split()
if len(parts) == 2:
    print(addNumbers(int(parts[0]), int(parts[1])))
elif len(parts) == 3:
    print(addNumbers(int(parts[0]), int(parts[1]), int(parts[2])))
else:
    print("Too many numbers provided")


def do_math(a, b, kind='add'):
    if (kind=='add'):
        return a+b
    else:
        return a-b

print(do_math(1, 2, kind='add'))
