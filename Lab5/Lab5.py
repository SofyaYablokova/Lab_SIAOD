import turtle                   # Подключаем модуль turtle
from datetime import datetime as t  # Модуль позволяющий управлять датой и временем

# Функция для отрисовки фракталов

def drawing(size, angle, line):
    for sym in line:
        if sym == "F":
            turtle.forward(size) # Двигать черепаху вперед на указанный size
        elif sym == "+":
            turtle.right(angle)  # Повернуть черепаху направо на angle единиц, по умолчанию в градусах
        elif sym == "-":
            turtle.left(angle)   # Повернуть черепаху налево на angle единиц, по умолчанию в градусах


# Кривая Серпинского

turtle.TurtleScreen._RUNNING = True

n = int(input('Глубина фрактала: '))  # Здесь пользователь вводит глубину фрактала
size = 5  # Размер
angle = 90  # Угол равный пи на 2, то есть 90
axiom = "F+XF+F+XF"  # Аксиома для кривой
rules = {"X":"XF-F+F-XF+F+XF-F+F-X"}  # Правило кривой


def create_sierpinski(n, axiom):
    if n == 0:
        return axiom  # Если введенное число равно 0, то возвращается значение аксиомы
    else:
        res_str = ""
        for i in axiom:
            if i == "+":
                res_str = res_str + "+"
            elif i == "-":
                res_str = res_str + "-"
            elif i == "F":
                res_str = res_str + "F"
            else:
                res_str = res_str + rules[i]
        return create_sierpinski(n - 1, res_str)


for i in range(n + 1):
    turtle.reset()  # Сбросить черепаху на экране в исходное состояние
    turtle.hideturtle()  # Сделать черепаху невидимой. На деле скрытие черепахи ускоряет рисование
    turtle.color('black')  # Устанавливает цвет пера на красный
    turtle.width(2)  # Установка толщины линии на width, то есть на 2
    turtle.speed(0)  # Задает скорость черепахи. При 0 значение скорости является fastest

    time1 = t.now()
    res_line = create_sierpinski(i, axiom)
    drawing(size, angle, res_line)
    time2 = t.now()

    print("Кривая Серпинского с глубиной = ", i, "|", "Время построения: ", ":",
          "{0} ms".format((time2 - time1).microseconds))

turtle.exitonclick()  # Выход с помощью клика мышкой