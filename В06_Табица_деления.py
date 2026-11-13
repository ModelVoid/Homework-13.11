#Табица деления
N = int(input("Введите количество столбцов таблицы: "))
n = int(input("Введите количество строк таблицы: "))
for i in range (1, n + 1):
    for j in range (1, N + 1):
        x = j / i
        print(f"{x:.1f}", end = "\t")
    print()  