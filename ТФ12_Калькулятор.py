while True:
    a = int(input("Введите первое число: "))
    op = input("Введите действие знаком: ")
    if op == "x":
        print(a)
        break
    if op == "!":
        if a >= 0:
            fact = 1
            for i in range(2, a + 1):
                fact *= i
            print(fact)
        continue
    b = int(input("Введите второе число: "))
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        if b != 0:
            print(a // b)
    elif op == "%":
        if b != 0:
            print(a % b)