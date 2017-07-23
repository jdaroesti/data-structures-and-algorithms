"""
File: selection_sort.py

Selection sort improves bubble sort by doing less operations.
While bubble sort must do several swaps in order to reach a result,
selection sort stores the index of the largest element and does
only one swap on each pass.

Nonetheless, selection sort is still inefficient.

0. [3, 6, 5, 4, 2, 9, 7, 1]
1. [3, 6, 5, 4, 2, 1, 7, 9]
2. [3, 6, 5, 4, 2, 1, 7, 9]
3. [3, 1, 5, 4, 2, 6, 7, 9]
4. [3, 1, 2, 4, 5, 6, 7, 9]
5. [3, 1, 2, 4, 5, 6, 7, 9]
6. [2, 1, 3, 4, 5, 6, 7, 9]
7. [1, 2, 3, 4, 5, 6, 7, 9]


Time complexity: O(n^2)
Space complexity: O(1)

http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html
"""
import random
import time


def selection_sort(arr):
    for fill_slot in range(len(arr) - 1, 0, -1):
        index_of_max = 0

        for current_index in range(1, fill_slot + 1):
            if arr[current_index] > arr[index_of_max]:
                index_of_max = current_index

        arr[index_of_max], arr[fill_slot] = arr[fill_slot], arr[index_of_max]

    return arr

if __name__ == '__main__':
    array_size = int(input('What array size do you want? '))
    arr = random.sample(range(array_size), array_size)

    print(arr)
    start = time.time()
    result = selection_sort(arr)
    end = time.time()

    print(result)
    print('The selection sort took {} seconds'.format(end - start))
