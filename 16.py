# Семинар 3. Списки и словари
# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

# n, a, x = 5, [1, 2, 3, 4, 5], 3
n = int(input("Длина массива: "))
a = [int(input(f"Введите {i+1}-е число: ")) for i in range(n)]
x = int(input("Число для поиска: "))
print(f"В массиве это число встречается: {a.count(x)}")
