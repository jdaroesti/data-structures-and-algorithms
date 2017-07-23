"""
File: insertion_sort.py

Insertion sort keeps a subarray inside the array to be sorted and
shifts this sub array in order to make room for the number to be sorted.

This stills needs to compare each number in the subarray.

0. [3, 6, 5, 4, 2, 9, 7, 1]
1. [3, 6, 5, 4, 2, 9, 7, 1]
2. [3, 5, 6, 4, 2, 9, 7, 1]
3. [3, 4, 5, 6, 2, 9, 7, 1]
4. [2, 3, 4, 5, 6, 9, 7, 1]
5. [2, 3, 4, 5, 6, 9, 7, 1]
6. [2, 3, 4, 5, 6, 7, 9, 1]
7. [1, 2, 3, 4, 5, 6, 7, 9]


Time complexity: O(n^2)
Space complexity: O(1)

http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html
"""
import random
import time


def insertion_sort(arr):
    for index in range(1, len(arr)):
        current_value = arr[index]
        position = index

        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = current_value

    return arr


if __name__ == '__main__':
    array_size = int(input('What array size do you want? '))
    arr = random.sample(range(array_size), array_size)

    print(arr)
    start = time.time()
    result = insertion_sort(arr)
    end = time.time()

    print(result)
    print('The insertion sort took {} seconds'.format(end - start))
