#6.1 (7) Числовые типы данных: int, float

# Dog age
# На вход программе подается число nnn – количество собачьих лет.
# Напишите программу, которая вычисляет возраст собаки в человеческих годах.

#age_dog = float(input())
#if 0 < age_dog <= 2:
    #print(age_dog * 10.5)
#else:
    #print(21 + (age_dog - 2) * 4)
    

# 6.1 (8) Числовые типы данных: int, float

# Первая цифра после точки
    
# Дано положительное действительное число.
# Выведите его первую цифру после десятичной точки.
    
# Формат входных данных
# На вход программе подается положительное действительное число.
    
# Формат выходных данных
# Программа должна вывести цифру в соответствии с условием задачи.

# num = float(input())
# i = ((num - int(num))*10)
# print(int(i))

#6.1 (9) Числовые типы данных: int, float

# Дробная часть
# Дано положительное действительное число. Выведите его дробную часть.
# Формат входных данных
# На вход программе подается положительное действительное число.
# Формат выходных данных
# Программа должна вывести дробную часть числа в соответствии с условием задачи.

num = float(input())
print(num - int(num))