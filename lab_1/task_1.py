import numpy as np
from utils import time_track

m = 3750
n = 3750


def create_array(m, n):
    array = np.random.randint(0, 100, (m, n))
    print(f'Исходная матрица \n {array}')
    print(len(array))
    return array


def search_even_elements(array):
    column_even_elements = []
    for i in range(len(array)):
        even_rows = []
        if i % 2 == 0:
            for j in array[i]:
                even_rows.append(j)
            column_even_elements.append(even_rows)
    return column_even_elements


def count_sum(array):
    column_sums = np.sum(array, axis=0)
    list_array = [l.tolist() for l in column_sums]
    index_min_column = list_array.index(min(list_array))
    print(f'Минимальная сумма четных элементов в столбце № {index_min_column}')
    return index_min_column


def change_columns(array, index):
    array_0 = np.copy(array[:, 0])
    array_i = array[:, index]
    array[:, 0], array[:, index] = array_i, array_0
    print(f'Новая матрица \n {array}')
    return array


@time_track
def run(m, n):
    array = create_array(m, n)
    even_elements = search_even_elements(array)
    index_min_column = count_sum(array=even_elements)
    change_columns(array=array, index=index_min_column)


if __name__ == '__main__':
    run(m, n)
