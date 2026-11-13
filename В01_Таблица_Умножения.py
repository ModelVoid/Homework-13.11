# Таблица Умножения
N = int(input("Введите размер таблицы: "))
for i in range (1, N + 1):
    for j in range (1, N + 1):
        print(i * j, end = "\t")
    print()    
