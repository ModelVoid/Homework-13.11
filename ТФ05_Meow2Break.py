n = 0
cat = False

while True:
    line = input("Введите слова(чтобы остановить напиши СТОП): ")
    if line == "СТОП":
        break
    n += 1
    if "Кот" in line or "кот" in line:
        print(n)
        cat = True
        break

if not cat:
    print(-1)
