import random
from time import time_ns

n = 4500

unordered_array = [random.randint(1, 100) for _ in range(n)]

x = 101
unordered_array_1 = list()
for i in unordered_array:
    unordered_array_1.append(i)


def linear_search(lys, element):
    for i in range(len(lys)):
        if lys[i] == element:
            return f'Найден элемент с индексом {i}'

    return 'Элемент не найден'


def linear_search_fast(list, element):
    for i in range(len(list)):
        if i > (n - 1):
            return 'Элемент не найден'
        if list[i] == element:
            return f'Найден элемент с индексом {i}'

    return 'Элемент не найден'


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return f'Найден элемент с индексом {mid}'
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return 'Элемент не найден'


def block_search(list, element):
    for i in range(len(list)):
        last = (len(list[i]))
        if list[i][last - 1] < element:
            continue
        else:
            for j in range(len(list[i])):
                if list[i][j] == element:
                    return f'Элемент находится в {i + 1}-ом блоке, и имеет индекс {j + 1}'
    return 'Элемент не найден'


if __name__ == '__main__':
    print('--------НЕУПОРЯДОЧЕННЫЙ МАССИВ-----------')
    tic = time_ns()
    print('Линейный поиск')
    print(linear_search(unordered_array, 101))
    toc = time_ns()
    print(f'Время выполнения: {(toc - tic)}')
    print()

    print('Быстрый линейный поиск')
    tic = time_ns()
    print(linear_search_fast(unordered_array, 101))
    toc = time_ns()
    print(f'Время выполнения: {(toc - tic)}')
    print()

    print('--------УПОРЯДОЧЕННЫЙ МАССИВ-----------')
    array = unordered_array
    array.sort()
    print('Быстрый линейный поиск')
    tic = time_ns()
    print(linear_search_fast(array, 101))
    toc = time_ns()
    print(f'Время выполнения: {(toc - tic)}')
    print()

    print('Бинарный поиск')
    tic = time_ns()
    print(binary_search(array, 101))
    toc = time_ns()
    print(f'Время выполнения: {(toc - tic)}')
    print()

    N = int(n ** 0.5)


    def func_chunk(lst, n):
        for x in range(0, len(lst), n):
            e_c = lst[x: n + x]

            if len(e_c) < n:
                e_c = e_c + [None for y in range(n - len(e_c))]
            yield e_c


    q = list(func_chunk(unordered_array, N))
    print('Блочный поиск')
    tic = time_ns()
    print(linear_search(q, 101))
    toc = time_ns()
    print(f'Время выполнения: {(toc - tic)}')
