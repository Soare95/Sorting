numbers = [99, 44, 45, 32, 1, 22, 7, 173, 6, 3, 15, 0, 2]


def insertion_sort(arr):
    arr_length = len(arr)
    i = 1
    end = arr[0]
    while i < arr_length:
        if arr[i] < end:
            x = arr.pop(i)
            for j in range(0, i):
                if x < arr[j]:
                    arr.insert(j, x)
                    break
        end = arr[i]
        i += 1
    return arr


print(insertion_sort(numbers))
