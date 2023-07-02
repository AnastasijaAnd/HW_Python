# Задача 22: Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями). Выдать без повторений в порядке возрастания 
# все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random

def DZ4z22():
    n = int(input('Введите колличество элементов первого набора чисел: '))
    m = int(input('Введите колличество элементов второго набора чисел: '))
    set1 = [int(input(f'Введите {i + 1} число первого списка: ')) for i in range (n)]  
    set2 = [int(input(f'Введите {i + 1} число второго списка: ')) for i in range (m)]  
    new_collection = []
    for i in set1:
        if i in set2 and not i in new_collection:
            new_collection.append(i)                                                          
    print(f"В обоих наборах встречаются числа: {sorted(new_collection)}")


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них 
# выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.


def DZ4z24():
    a = int(input('Введите количество кустов на грядке: '))
    garden = [random.randint(1, 9) for i in range(a)]
    print(*garden)
    max_bushes  = garden[0] + garden[1] + garden[2]
    indicator = ["*"] * 3 + [" "] * (len(garden) - 3)
    for i in range (len(garden)):
        following_bushes = garden[1] + garden[2] + garden[3]
        if following_bushes > max_bushes:
            max_bushes = following_bushes
            indicator = ["*"] * 3 + [" "] * (len(garden) - 3)
        else:
            temp = indicator.pop(0)
            indicator.append(temp)    
        temp = garden.pop(0)
        garden.append(temp)
    print(*indicator)
    print(f"Максимальное число собранных ягод за один заход = {max_bushes}")

def SelectTask():
    a = int(input("Введите номер задачи (22, 24): "))
    if a == 22:
        DZ4z22()
    elif a == 24:
        DZ4z24()
    else:
        print("Такого номера задачи нет.")
    SelectTask()

SelectTask()


