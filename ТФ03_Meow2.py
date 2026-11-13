number = 0
index = -1

while True:
    line = input("Введите слова(чтобы остановить напиши СТОП): ")
    if line == "СТОП":
        break
    number += 1
    if ("Кот" in line or "кот" in line) and index == -1:
        index = number
print(index)         