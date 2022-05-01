# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

list1 = [randint(0,10) for item in range(10)]
list2 = []
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] == list1[j]:
            list2.append(list1[i])
#for i in range(len(list)):

print('Исходная последовательность', list1)
print('Список неповторяющихся элементов', list(set(list1)-set(list2)))