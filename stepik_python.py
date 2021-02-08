# 6.1 (8) Числовые типы данных: int, float

# Первая цифра после точки
    
# Дано положительное действительное число.
# Выведите его первую цифру после десятичной точки.
    
# Формат входных данных
# На вход программе подается положительное действительное число.
    
# Формат выходных данных
# Программа должна вывести цифру в соответствии с условием задачи.

# num = int(input())
# one, two, three = num // 100, num // 10 % 10, num % 10
# #print(one, two, three)
# average = (one + two + three) - (max(one, two, three) + min(one, two, three))
# # print(average)
# #print(max(one, two, three) - min(one, two, three))
# if average == max(one, two, three) - min(one, two, three):
#     print('Число интересное')
# else:
#     print('Число неинтересное')

#------------------------------------------------------------

# 6.1 (9) Числовые типы данных: int, float
    
# Даны пять чисел. Напишите программу, которая вычисляет сумму их модулей.
# Формат входных данных
# На вход программе подается пять действительных чисел каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести одно число – сумму модулей введёных чисел.

# a1, a2, a3, a4, a5 = float(input()), float(input()), float(input()), float(input()), float(input())
# print(abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5))

#---------------------------------------------------------------------

# 6.1 (10) Числовые типы данных: int, float
# Формат входных данных
# На вход программе подается четыре целых числа, каждое на отдельной строке – p_{1}, \, p_{2}, \, q_{1}, \, q_{2}p 

# Формат выходных данных
# Программа должна вывести одно число – манхэттенское расстояние.
# p1, p2, q1, q2 = int(input()), int(input()), int(input()),int(input())
# print(abs(p1 - q1) + abs(p2 - q2))

#---------------------------------------------------------------------

#6.2 (2) Модуль math
# Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.
# Формат входных данных
# На вход программе подается четыре вещественных числа, каждое на отдельной строке – 
# Формат выходных данных
# Программа должна вывести одно число – евклидово расстояние.

# from math import sqrt
# x1, y1, x2, y2 = float(input()), float(input()), float(input()),float(input())
# print(sqrt(((x1 - x2)**2) + ((y1 - y2)**2)))

#6.2 (3) Модуль math

# from math import pi
# r = float(input())
# print(pi * (r**2))
# print(2 * pi * r)

#---------------------------------------------------------

#6.2 (4) Модуль math
# Формат входных данных
# На вход программе подается два вещественных числа a и b​, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.

# from math import sqrt
# a, b = float(input()), float(input())
# print((a + b) / 2)
# print(sqrt(a * b))
# print((2 * a * b) / (a + b))
# print(sqrt(((a**2) + (b**2)) / 2))

#-------------------------------------------------------------

#6.2 (5) Модуль math

# Тригонометрическое выражение
# Напишите программу, вычисляющую значение тригонометрического выражения
# по заданному числу градусов xx.
# Формат входных данных
# На вход программе подается одно вещественное число xx измеряемое в градусах​. 
# Формат выходных данных
# Программа должна вывести одно число – значение тригонометрического выражения.
# Примечание 1. Тригонометрические функции принимают аргумент в радианах. Чтобы перевести градусы в радианы, воспользуйтесь формулой

#from math import sin, cos, tan, radians
#x = float(input())
#print(sin(radians(x)) + cos(radians(x)) + tan(radians(x))**2)

# ---------------------------------------------------------------------------------

# 6.2 (6) Модуль math
#Пол и потолок
#Напишите программу, вычисляющее значение x + x по заданному вещественному числу x
#Формат входных данных
#На вход программе подается одно вещественное число x
#Формат выходных данных
# Программа должна вывести одно число – значение указанного выражения.

#from math import floor, ceil
#x = float(input())
#print(ceil(x) + floor(x))

# ---------------------------------------------------------------------------------

# 6.2 (7) Модуль math

#Квадратное уравнение
# Даны три вещественных числа a, b, c Напишите программу, которая находит вещественные корни
#Формат входных данных
#На вход программе подается три вещественных числа каждое на отдельной строке.
#Формат выходных данных
#Программа должна вывести вещественные корни уравнения если они существуют или текст «Нет корней» в противном случае.
# Примечание. Если уравнение имеет два корня, то следует вывести их в порядке возрастания.

#import math

#a, b, c = float(input()), float(input()), float(input())
#d = b ** 2 - 4 * a * c

#if d > 0:
    #x1 = (-b + math.sqrt(d)) / (2 * a)
    #x2 = (-b - math.sqrt(d)) / (2 * a)
    #print(x1)
    #print(x2)
#elif d == 0:
    #x = - b / (2 * a)
    #print(x)
#else:
    #print('Нет корней')

#import math
#n, a = int(input()), float(input())
#print(n * (a ** 2) / (4 * math.tan(math.pi / n)))

# --------------------------------------------------------

# 6.3 (5) Строковый тип данных

#txt = '''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."'''
# print(txt)

# ---------------------------------------------------------

# 6.3 (6) Строковый тип данных

#name1, name2 = input(), input()
#print('Hello ' + name1, name2 + '! You just delved into Python')

# -----------------------------------------------------------

# 6.3 (7) Строковый тип данных

#football = input()
#print('Футбольная команда ' + football +
      # ' имеет длину ' + str(len(football)) + ' символов')
      
# ----------------------------------------------------------

# 6.3 (8) Строковый тип данных

#sity1, sity2, sity3 = input(), input(), input()
#print(min(sity1, sity2, sity3, key=len))
#print(max(sity1, sity2, sity3, key=len))

# -----------------------------------------------------------

# (2) 7.1 Цикл for

#for i in range(10):
    #print('Python is awesome!')

# ------------------------------------------------------------

# (3) 7.1 Цикл for

#line, repeat = input(), int(input())
#for i in range(repeat):
    #print(line)

# --------------------------------------------------------------

# (4) 7.1 Цикл for

for i in range(6):
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')
        



