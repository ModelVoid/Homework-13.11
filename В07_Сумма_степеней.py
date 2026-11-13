#Сумма степеней
n = int(input("Введите число: "))
x = 0
num = 0
for i in range(1, n+1):
    summa = 0
    for j in range(1, i+1):
        if i % 2 == j % 2:
            summa += j
    num += i ** summa
print(num)
    