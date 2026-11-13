x = int(input("x: "))
y = int(input("y: "))

cur_x = 0
cur_y = 0
count = 0

while True:
    direction = input("Введите направление движения: ")
    if direction == "стоп":
        break
    steps = int(input("Введите кол-во шагов: "))
    count += 1
    if direction == "север":
        cur_y += steps
    elif direction == "юг":
        cur_y -= steps
    elif direction == "восток":
        cur_x += steps
    elif direction == "запад":
        cur_x -= steps
    if cur_x == x and cur_y == y:
        print(count)
        break