# 1. Составить программу, которая требует ввести два числа.
# Если первое число больше второго, то программа печатает слово больше.
# Если первое число меньше второго, то программа печатает слово меньше.
# А если числа равны, программа напечатает сообщение Эти числа равны.


def ex1():
    a = input("Введите первое число \n > ")
    b = input("Введите второе число \n > ")

    if a > b:
        print('первое число больше второго')
    elif a == b:
        print('числа равны')
    else:
        print('второе число больше первого')


# 2. Составить алгоритм увеличения всех трех, введённых с клавиатуры, переменных на 5,
# если среди них есть хотя бы две равные. В противном случае выдать ответ «равных нет».

def ex2():
    a = int(input("Введите первое число \n > "))
    b = int(input("Введите второе число \n > "))
    c = int(input("Введите третье число \n > "))

    if a == b or a == c or b == c:
        print(a+5, b+5, c+5)
    else:
        print('равных нет')


# Вывести таблицу умножения на экран.
def ex3():
    number = 0
    for number in range(11):
        for second_number in range(11):
            print(number, '*', second_number, '=', number*second_number)
        print()


# Вывести на экран фигуры со звездочек (Ромб, Елочка, Треугольник, Квадрат, ступеньки)
def ex4():
    value = input("input value")
    a = " "
    b = "*"


# Напишите программу, запрашивающую имя, фамилия, отчество и номер группы студента и выводящую введённые данные в
# следующем виде:
#  ************************************
#  *Лабораторная работа № 1   *
#  *Выполнил(а): ст. гр. ЗИ-123 *
#  *Иванов Андрей Петрович    *
#  ************************************
# Необходимо, чтобы программа сама определяла нужную длину рамки. Сама же длина рамки зависит от длины наибольшей
# строки внутри рамки. Используя циклы for легко можно выровнять стороны рамки.
def ex5():
    name = input('введите Ваши ФИО')
    group = input('введите номер группы')
    first_line = 'Лабораторная работа № 1'
    second_line = '{}{}'.format("Выполнил(а): ст. гр.", group)
    d = [len(name), len(first_line), len(second_line)]

    maxlong = 0
    for i in d:
        if i > maxlong:
            maxlong = i

    print('*' * (maxlong+2))
    print('*{}{}*'.format(first_line, ' ' * (maxlong - len(first_line))))
    print('*{}{}*'.format(second_line, ' ' * (maxlong - len(second_line))))
    print('*{}{}*'.format(name, ' ' * (maxlong - len(name))))
    print('*' * (maxlong + 2))


# 5. Дано двузначное число. Определить:
#     • входит ли в него цифра 3
#     • входит ли в него цифра а
def ex6():
    value = input('input value \n > ')
    a = '3'
    b = 'a'
    for i in value:
        if i == a:
            print('a = ok')
        elif i == b:
            print('b = ok')


# 6. Определить, является ли треугольник со сторонами a, b, c равнобедренным

def ex7():
    a = int(input('input first side \n > '))
    b = int(input('input second side \n > '))
    c = int(input('input third side \n > '))

    if a + b > c and b + c > a and a + c > b:
        if a == b == c:
            print('This is equilateral triangle')
        elif a == b or a == c or b == c:
            print('This is isosceles triangle')
        else:
            print('It isn`t isosceles triangle')
    else:
        print('It can`t be triangle')


# 7. Даны три различных числа. Определить, какое из них (первое, второе или третье)
#     • самое большое
#     • самое маленькое
#     • является средним
def ex8():
    a = int(input('input first value \n > '))
    b = int(input('input second value \n > '))
    c = int(input('input third value \n > '))
    d = [a, b, c]
    maxvalue = 0
    for i in d:
        if i > maxvalue:
            maxvalue = i
    print('maxvalue =', maxvalue)

    minvalue = maxvalue
    for i in d:
        if i < minvalue:
            minvalue = i
    print('minvalue =', minvalue)

    average = 0
    for i in d:
        if minvalue < i < maxvalue:
            average = i
    print('average =', average)

