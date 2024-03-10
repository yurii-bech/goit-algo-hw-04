import timeit
import random

# Функція для тестування сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

# Функція для тестування сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Генерація випадкових даних для тестування
data_sizes = [100, 1000, 10000]
datasets = {size: [random.randint(0, 1000) for _ in range(size)] for size in data_sizes}

# Заміри часу виконання для кожного алгоритму на різних наборах даних
for size, data in datasets.items():
    print(f"Data size: {size}")
    print("Merge Sort:", timeit.timeit(lambda: merge_sort(data.copy()), number=10))
    print("Insertion Sort:", timeit.timeit(lambda: insertion_sort(data.copy()), number=10))
    print("Timsort:", timeit.timeit(lambda: sorted(data.copy()), number=10))
    print()