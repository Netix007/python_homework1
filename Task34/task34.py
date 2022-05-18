# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

from random import randint

def koef(str):
    last_digit = False
    index_s = str.find('x')
    index_f = str.find(' ')
    if index_s !=-1:
        if index_s == 0:
            a = 1
        else:
            a = int(str[0:index_s-1])
        if str[index_s+1:index_s+3] == '**':
            k = int(str[index_s+3:index_f])
            str = str[index_f + 3:]
        else:
            k = 1
            str = str[index_f + 3:]
    else:
        k = 0
        last_digit = True
        if len(str) > 3:
            a = int(str[:3])
        else:
            a = 0
    return str, k, a, last_digit

def receive_index(str1):
    str1_list = koef(str1)

    list1 = [0 for item in range(str1_list[1]+1)]
    list1[str1_list[1]] = str1_list[2]
    str1 = str1_list[0]
    while not str1_list[3]:
        str1_list = koef(str1)
        str1 = str1_list[0]
        list1[str1_list[1]] = str1_list[2]
    return list1

def mult(list, k):
    f_txt = open("text.txt", 'w')
    if list[k] == 1:
        f_txt.write(f'x**{k}')
    else:    
        f_txt.write(f'{list[k]}*x**{k}')

    f_txt = open("text.txt", 'a')
    for i in range(k-1,1,-1):
        if list[i] != 0 and list[i] != 1:
            f_txt.write(f' + {list[i]}*x**{i}')
        if list[i] == 1:
            f_txt.write(f' + x**{i}')

    if list[1] == 0 and list[0] != 0:
        f_txt.write(f' + {list[0]} = 0')
    elif list[0] == 0 and list[1] != 0:
        if list[1] == 1:
            f_txt.write(f' + x = 0')    
        else:
            f_txt.write(f' + {list[1]}*x = 0')
    elif list[0] != 0 and list[1] != 0:
        if list[1] == 1:
            f_txt.write(f' + x + {list[0]} = 0')
        else:
            f_txt.write(f' + {list[1]}*x + {list[0]} = 0')
    else:
        f_txt.write(f' = 0')
    f_txt.close()


txt1 = open("text1.txt", 'r')
str1 = txt1.readline()
txt1.close()
txt2 = open("text2.txt", 'r')
str2 = txt2.readline()
txt2.close()
print(str1)
print(str2)

list1 = receive_index(str1)
list2 = receive_index(str2)

print(list1, "\n" ,list2)

if len(list1) < len(list2):
    list1, list2 = list2, list1
list3 = list1
for i in range(len(list2)):
    list3[i] += list2[i]

print(list3)

mult(list3, len(list3)-1)
