# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

from random import randint

# Метод вычисления степени многочлена (k) и высшего коэффициента (a). Допустимые значения k >= 1 a >= 0

def coef(str, str_need):                
    index_s = str.find(str_need)
    if index_s != -1:
        if str_need == '*x**':
            index_f = str.find(' ')
            k = int(str[index_s+4:index_f])
        else:
            index_f = str.find(' ')
            k = 1
        a = int(str[0:index_s])
        str = str[index_f + 3:]
    else:
        k = index_s
    return str, k, a

def receive_index(str1):
    str1_list = coef(str1, '*x**')
    list1 = [0 for item in range(str1_list[1]+1)]
    list1[str1_list[1]] = str1_list[2]
    str1 = str1_list[0]
    str1_list = coef(str1, '*x')     # вычисление 1 коэффициента
    list1[1] = str1_list[2]
    str1 = str1_list[0]              # вычисление 0 коэффициента
    list1[0] = int(str1[:3])
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

print(list1, list2)

list3 = []
for i in range(len(list1)):
    list3.append(list1[i] + list2[i])

print(list3)

mult(list3, len(list3)-1)
