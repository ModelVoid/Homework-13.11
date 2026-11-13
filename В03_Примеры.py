
#Примеры
num1 = int(input("Введите начальное число: "))
num2 = int(input("Введите конечное число: "))
num3 = int(input("Введите изменение: "))
for i in range (num1, num2 + 1, num3):
    for j in range (num1, num2 + 1, num3):
        print(f"{i} + {j} = {i+j}", end = "\t")
    print("")

        