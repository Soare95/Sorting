numbers = [99, 44, 45, 32, 1, 7, 173, 6, 3, 15, 0, 2]


def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len-1):
        for j in range(arr_len - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


bubble_sort(numbers)
print(numbers)
