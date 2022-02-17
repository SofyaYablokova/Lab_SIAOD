# Лабораторная работа №1
# Выполнила студентка группы БСТ2001 Яблокова С.А.
# Задание №1
# Вывести строку "Hello World"
print("Hello, World!")
# Задание №2
# Написать генератор случайных матриц(многомерных),
# который принимает опциональные параметры m, n, min_limit, max_limit,
# где m и n указывают размер матрицы, а min_lim и max_lim - минимальное и максимальное значение для генерируемого числа .
# По умолчанию при отсутствии параметров принимать следующие значения:
# m = 50 n = 50 min_limit = -250 max_limit = 1000 + (номер своего варианта)
import random
m = int(input())
n = int(input())
min_limit = int(input("min_limit="))
max_limit = int(input("max_limit="))
Matrix = [ [ random.randint(min_limit, max_limit) for j in range(n)] for i in range(m) ]
print('Matrix:')
for i in range(m):
    print(Matrix[i])
# Задание №3
# Реализовать методы сортировки строк числовой матрицы в соответствии с заданием.
# Оценить время работы каждого алгоритма сортировки и сравнить его со временем стандартной функции сортировки.
# Испытания проводить на сгенерированных матрицах.
# Сортировка Выбором
def selections(arr):
    for i, e in enumerate(arr):
        mn = min(range(i, len(arr)), key=arr.__getitem__)
        arr[i], arr[mn] = arr[mn], e
    return arr
#Сортировка Вставкой
def insertions(arr):
    for i in range(1, len(arr)):
        j = i - i
        while j >= 0 and arr[i] < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = arr[i]
#Сортировка Обменом
def bubbles(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
# Сортировка Шелла
def shells(arr):
    last_index = len(arr) - 1
    step = len(arr) // 2
    while step > 0:
        for i in range(step, last_index + 1, 1):
            j = i
            delta = j - step
            while delta >= 0 and arr[delta] > arr[j]:
                arr[delta], arr[j] = arr[j], arr[delta]
                j = delta
                delta = j - step
        step //= 2
#<scnhfz Cjhnbhjdrf
def quicks(arr, fst=0, lst=None):
    if lst == None:
        lst = len(arr) - 1
    if fst >= lst:
        return
    i, j = fst, lst
    pivot = arr[(lst + fst) // 2]
    while i <= j:
        while arr[i] < pivot: i += 1
        while arr[j] > pivot: j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i, j = i + 1, j - 1
    quicks(arr, fst, j)
    quicks(arr, i, lst)
#Турнирная Сортировка
def tournaments(arr):
    tree = [None] * 2 * (len(arr) + len(arr) % 2)
    index = len(tree) - len(arr) - len(arr) % 2
    for i, v in enumerate(arr):
        tree[index + i] = (i, v)
    for j in range(len(arr)):
        n = len(arr)
        index = len(tree) - len(arr) - len(arr) % 2
        while index > -1:
            n = (n + 1) // 2
            for i in range(n):
                i = max(index + i * 2, 1)  # на последней итерация index + i * 2 = 0
                if tree[i] != None and tree[i + 1] != None:
                    if tree[i][1] < tree[i + 1][1]:
                        tree[i // 2] = tree[i]
                    else:
                        tree[i // 2] = tree[i + 1]
                else:
                    tree[i // 2] = tree[i] if tree[i] != None else tree[i + 1]
            index -= n

        index, x = tree[0]
        arr[j] = x
        tree[len(tree) - len(arr) - len(arr) % 2 + index] = None
#Пиоамидальная Сортировка
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def heaps(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
#Время работы алгоритмов
import time
SORT_FUNCTIONS = {
    'Сортировка выбором': selections,
    'Сортировка вставкой': insertions,
    'Сортировка обменом': bubbles,
    'Cортировка Шелла': shells,
    'Быстрая сортировка': quicks,
    'Турнирная сортировка': tournaments,
    'Пирамидальная сортировка': heaps,
    'Встроенная сортирока': sorted
}
def print_comparison(comparison):
    largest_name_len = len(max(comparison.keys(), key=len))
    largest_name_len += 6

    heading = 'Алгоритм'.ljust(largest_name_len) + 'Время'
    print(heading)
    print('-' * len(heading))
    for algo, time_taken in comparison.items():
        print(f'{algo:<{largest_name_len}}{time_taken}')

time_taken = {}
samples = Matrix
for algo_name, sorter in SORT_FUNCTIONS.items():
    samples_copy = samples.copy()
    start = time.perf_counter()
    for sample in samples_copy:
        sorter(sample)
    end = time.perf_counter()

    time_taken[algo_name] = (end - start) / len(samples)

time_taken_sorted = dict(sorted(time_taken.items(), key=lambda kv: kv[1]))
print_comparison(time_taken_sorted)
# Вывод
# В ходе лабораторной работы мы научились использовать Pycharm,
# оформлять заголовки, выполнять простую задачу на вывод Hello, World! на языке программирования Python 3.10,
# а также создавать генераторы случайных матриц, реализовали 7 методов сортировки и
# сравнили время работы каждого метода со временем стандартной функции сортировки.
# Также создали публичный репозиторий на github и выгрузили данную лабораторную работу в созданный репозиторий.



