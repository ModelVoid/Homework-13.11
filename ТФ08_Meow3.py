count = 0
first = -1
n = 0

while True:
    line = input("Введите слова(чтобы остановить напиши СТОП): ")
    if line == "СТОП":
        break
    n += 1
    if "Кот" in line or "кот" in line:
        count += 1
        if first == -1:
            first = n
print(count, first)
