# Вычислить число c заданной точностью d

from cmath import pi

is_error = True
while is_error:
    d = float(input('Введите точность (Допустимые значения: 10**-1 >= d >= 10**-10) \nd = '))
    if 10**-1 >= d >= 10**-10:
        is_error = False
    else: print('Недопустимое значение. Повторите ввод.')

res = d*int(pi / d)

print('Результат вычисления с заданной точностью:', res)