# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint

is_Error = True
while is_Error:
    k = input('Задайте натуральную степень k = ')
    try:
        int(k)
        is_Error = False
    except ValueError:
        is_Error = True
    if not is_Error and int(k) >= 1:
       k = int(k)
    else:
        is_Error = True

list = [randint(0,100) for item in range(k+1)]
while list[k] == 0:
    list = [randint(0,100) for item in range(k+1)]
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
print(list)
