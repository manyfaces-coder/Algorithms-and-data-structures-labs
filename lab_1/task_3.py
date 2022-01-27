from utils import time_track
from random import randint

array = [randint(-100, 100) for i in range(2500)]
print(f'Исходная последовательность \n {array}')


@time_track
def run(array):
    positive_elements = []
    for i in array[::-1]:
        if i > 0 and len(positive_elements) < 5:
            positive_elements.append(i)

    max = 0
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
            max_index = i
    print(f'Номер максимального элемента \n {max_index}')

    new_array = [i * max_index for i in positive_elements]
    print(f'Новый массив \n {new_array}')


if __name__ == '__main__':
    run(array)
