# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def Range_min_max(min_border, max_border):
    dict_1 ={}
    for i in range(min_border, max_border + 1):
        dict_1[i] = 0
    return dict_1

def Index_list(list_1, dict_1):
    list_2 =[]
    for i in range(len(list_1)):
        if list_1[i] in dict_1:
            list_2.append(i)
    return list_2

def DZ4z30():
    list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
    min_border = int(input('Ввелите нижнюю границу диапазона: '))
    max_border = int(input('Ввелите верхнюю границу диапазона: '))
    print(Index_list(list_1, Range_min_max(min_border, max_border)))


# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def Progression(a1, n, d):
    list_1 = []
    for i in range(1, n + 1):
        list_1.append(a1 + (i - 1) * d)
    return list_1

def DZ4z32():
    a1 = int(input('Введите первый элемент прогрессии а1 = '))
    n = int(input('Введите количество элементов прогрессии n = '))
    d = int(input('Введите разность d = '))
    print(Progression(a1, n, d))


def SelectTask():
    a = int(input("Введите номер задачи (30, 32): "))
    if a == 30:
        DZ4z30()
    elif a == 32:
        DZ4z32()
    else:
        print("Такого номера задачи нет.")
    SelectTask()

SelectTask()