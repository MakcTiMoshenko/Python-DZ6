"""Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

Диапазон от 6 до 12

Вывод: [1, 9, 13, 14, 19]"""

list1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
def Podbor(list1):
    list2 = []
    for i in range(len(list1)-1):
        if 6 < list1[i]<12:
            list2.append(list1[i])
    return list2
print(Podbor(list1))