count = int(input("Количество вводимых строк: "))

cat = False
for i in range(count):
    s = input("Введите слово: ")
    if "Кот" in s or "кот" in s:
         cat = True
if cat:
     print("МЯУ")
else:
     print("НЕТ")              