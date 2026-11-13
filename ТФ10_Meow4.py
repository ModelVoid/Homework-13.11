n = int(input("Введите кол-во строк: "))
found = False

for _ in range(n):
    line = input("Введите слова(чтобы остановить напиши СТОП): ")
    if "Кот" in line or "кот" in line:
        found = True
    if "Пёс" in line or "пёс" in line:
        found = False

if found:
    print("МЯУ")
else:
    print("НЕТ")