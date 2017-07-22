import random

def bubble_sort(numbers):
    for pass_num in range(len(numbers) - 1, 0, -1):
        for i in range(pass_num):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

    return numbers

if __name__ == '__main__':
    numbers = [random.randint(0, 200) for i in range(50)]
    print(numbers)
    result = bubble_sort(numbers)
    print(result)
