n = int(input("Введите кол-во строк: "))
cat = False
for i in range(n):
    line = input("Введите слова: ")
    if "кот" in line or "Кот" in line:
        print("МЯУ")
        cat = True
        break
if not cat:
    print("НЕТ")    