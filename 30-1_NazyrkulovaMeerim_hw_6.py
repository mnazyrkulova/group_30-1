# Функция bubble
numbers = [160, 85, 33, 64, 5, 22, 78, 93, 14, 56, 1020]
def bubble_sort(numbers):
    changed_place = True
    while (changed_place):
        changed_place = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                return numbers
print(bubble_sort(numbers))


# Функция binary_search
numbers = [160, 85, 33, 64, 5, 22, 78, 93, 14, 56, 1020]
n = 56
def binary_search(numbers):
    first = 0
    last = len(numbers) - 1
    while first <= last:
        middle = first + (last - first) // 2
        if numbers[middle] == n:
            return middle
        elif numbers[middle] < n:
            first = middle + 1
        else:
            last = middle - 1
            return numbers
print(binary_search(numbers))