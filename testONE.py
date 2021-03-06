# Задачи на циклы и оператор условия

"""
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
"""
a = 0
while a < 5:
    a += 1
    print('№',a,'- '"0")


"""
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифры 5.
"""
sum = 0
for a in range(10):
    answer = int(input('Введите десять раз любое число и нажмите ввод:  '))
    if answer == 5:
        sum += 1
print("количество введеных пользователем цифр  равно: ", sum)


"""
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
"""
sum = 0
for a in range(1,101):
    sum += a
print(sum)


"""
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
"""
sum = 1
for a in range(1,10):
    sum *= a
print(sum)


"""
Задача 5
Вывести цифры числа на каждой строчке.
"""
integer_namber = "36288"[::-1]
while (int(integer_namber)>0):
        print(int(integer_namber)%10)
        integer_namber = int(integer_namber)//10


"""
Задача 6
Найти сумму цифр числа.
"""
a = 36288 % 10
b = (36288// 10 ) % 10
c = (36288// 100) % 10
d = 36288//1000 % 10
f = 36288//10000

print ( a + b + c + d + f)

"""
Вариант 2
"""
a = 36288
sum = 0
while a>0:
    sum += a%10
    a = a//10
print(sum)


"""
Задача 7
Найти произведение цифр числа.
"""
a = 36288 % 10
b = (36288// 10 ) % 10
c = (36288// 100) % 10
d = 36288//1000 % 10
f = 36288//10000

print ( a * b * c * d * f)

"""
вариант 2
"""
a = 36288
mult = 1
while a>0:
    mult *= a%10
    a = a//10
print(mult)


"""
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
"""
a = 1234567890
while a > 0:
    if a %10 == 5:
        print("Yes")
        break
    a = a//10
else: print("No")


"""
Задача 9
Найти максимальную цифру в числе.
"""
a = 1234567890
max = 0
while a>0:
    if a%10 >= max:
        max = a%10
    a = a//10
print(max)


"""
Задача 10
Найти количество цифр 5 в числе.
"""
a = 1234567890
sum = 0
while a>0:
    if a%10 == 5:
        sum += 1
    a = a//10
print(sum)
