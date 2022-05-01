# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

is_Error = True
while is_Error:
    n = input('Введите натуральное число n = ')
    try:
        int(n)
        is_Error = False
    except ValueError:
        is_Error = True
    if not is_Error and int(n) > 0:
       n = int(n)
    else:
        is_Error = True

list = []
prime_number = 1
for i in range(2,n):
    while n%i == 0:
        list.append(i)
        n = n / i
        prime_number += 1
if not prime_number > 1:
    print('Вы ввели простое число')
else:
    print('Список простых множителей числа:', list)