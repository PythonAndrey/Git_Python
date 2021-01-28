# 6.1 (8) Числовые типы данных: int, float

# Первая цифра после точки
    
# Дано положительное действительное число.
# Выведите его первую цифру после десятичной точки.
    
# Формат входных данных
# На вход программе подается положительное действительное число.
    
# Формат выходных данных
# Программа должна вывести цифру в соответствии с условием задачи.

num = int(input())
one, two, three = num // 100, num // 10 % 10, num % 10
#print(one, two, three)
average = (one + two + three) - (max(one, two, three) + min(one, two, three))
# print(average)
#print(max(one, two, three) - min(one, two, three))
if average == max(one, two, three) - min(one, two, three):
    print('Число интересное')
else:
    print('Число неинтересное')

    
