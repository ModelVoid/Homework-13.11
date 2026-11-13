# Ёлочный счёт
N = int(input("Введите n: "))
num = 1
x = 1
while x <= N:
    j = 0
    while j < x and num <= N:
        print(num, end=" ")
        num += 1
        j += 1
    print()
    x += 1
        

