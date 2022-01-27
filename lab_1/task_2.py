from utils import time_track
from task_1 import create_array

m = 3750
n = m


def search_even_values(array):
    for i in range(len(array)):
        if i % 2 != 0:
            for j in range(len(array[i])):
                array[i][j] = i - j
    print(f'Новая матрица \n {array}')


@time_track
def run(m, n):
    array = create_array(m, n)
    search_even_values(array)


if __name__ == '__main__':
    run(m, n)
