# Задание 1.
# Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторы числа и строки и
# сохраните в переменные, затем выведите на экран
print('Задание 1')
a = 10
b = 15
c = 'привет'
print(a, b, c)
d = input('Ведите число')
e= input('Ведите строку')
print('Это то, что ввел пользователь - ', d, e)
print('')

# Задание 2.
# Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк
print('Задание 2')
time_sec = int(input('Введите время в секундах'))
time_min_cel = time_sec // 60
time_h_cel = time_min_cel // 60
print('Время в чч:мм:сс:', time_h_cel, ':', time_min_cel - time_h_cel * 60, ':', time_sec - time_min_cel * 60 )
print('')

# Заждание 3.
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369
print('Задание 3')
n_str = str(input('Введите число n'))
n_n = n_str + n_str
n_n_n = n_str + n_str + n_str
n_n_n_int = int(n_str) + int(n_n) + int(n_n_n)
print('Сумма чисел n+nn+nnn = ', n_n_n_int)
print('')

# Заждание 4.
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
print('Задание 4')
cel_plus = int(input('введите целое положительное число'))
# print(list(str(cel_plus)))
print('С помощью операции max самая большая цифра - ', max(list(str(cel_plus))))
print('Теперь с помощью математических операций')
max_cel_plus = cel_plus % 10
# print(max_cel_plus)
while cel_plus >= 1:
    cel_plus = cel_plus // 10
    # print (cel_plus)
    if cel_plus % 10 > max_cel_plus:
        # print (cel_plus)
        # print(max_cel_plus)
        max_cel_plus = cel_plus % 10
        # print(max_cel_plus)
    elif cel_plus > 9:
        pass
print('Максимальная цифра в числе', max_cel_plus)
print('')

# Задание 5
# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.
# Задание 6.
# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

print('Задание 5 и 6')
earn = int(input('Введите выручку фирмы'))
costs = int(input('Введите издержки фирмы'))
if earn > costs:
    print('Фирма работает с прибылью', earn - costs)
    print('Рентабельность выручки', (earn - costs) / earn)
    chisl_sotr = int(input('Введите численность сотрудников'))
    print('Прибыль фирмы в расчите на одного сотрудника', (earn - costs) / chisl_sotr)
else:
  print('Фирма работает с убытком', abs(earn - costs))
print('')

# Задание 7
# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен
# увеличивал результат на 10% относительно предыдущего. Требуется определить номер дня, на который результат спортсмена
# составит не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное
# число — номер дня
print('Задание 7')
a_km = int(input('Введите значение "а" км - результат в первый день'))
b_km = int(input('Введите значение "b" км - итоговый результат'))
# задаем номер первого дня
d_1 = 1
while a_km <= b_km:
    d_1 = d_1 + 1
    a_km = a_km + a_km / 10
print('Вы достигли результата на  ', d_1, '  день')

# проба Git