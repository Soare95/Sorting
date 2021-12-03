numbers = [99, 44, 45, 32, 1, 7, 173, 6, 3, 15, 0, 2]


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


print(selection_sort(numbers))
