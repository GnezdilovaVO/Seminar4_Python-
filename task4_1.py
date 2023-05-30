# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
# Если таких чисел нет - выдать внятное диагностическое сообщение
# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры

# Примеры/Тесты:
# Input1: 2 4 6 8 10 12 10 8 6 4 2
# Input2: 3 6 9 12 15 18
# Output: 6 12     Обратите внимание: Без скобочек, в одну строку

# Input1: 2 4 6 8 10 10 8 6 4 2
# Input2: 3 9 12 15 18
# Output: Повторяющихся чисел нет

input1 = (2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2)
input2 = (3, 6, 9, 12, 15, 18)
# input1 = (2, 4, 6, 8, 10, 10, 8, 6, 4, 2)
# input2 = (3, 9, 12, 15, 18)
input1 = set(input1)
input2 = set(input2)
new_input = input1.intersection(input2)
new_input = list(new_input)
for i in range(len(new_input)-1):
    if new_input[i] > new_input[i+1]:
        temp = new_input[i+1]
        new_input[i+1] = new_input[i]
        new_input[i] = temp
if new_input == list(): 
    print("Таких данных нет")
else: 
    for item in new_input:
        print(item, end = " ")