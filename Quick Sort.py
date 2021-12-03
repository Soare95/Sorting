# numbers = [99, 44, 45, 32, 1, 22, 7, 173, 6, 3, 15, 0, 2]
numbers = [3, 7, 8, 5, 2, 1, 9, 5, 4]


def quick_sort(arr, left, right):
    if left < right:
        pivot = right
        partition_index = partition(arr, pivot, left, right)
        quick_sort(arr, left, partition_index-1)
        quick_sort(arr, partition_index+1, right)
    return arr


def partition(arr, pivot, left, right):
    pivot_value = arr[pivot]
    partition_index = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            swap(arr, i, partition_index)
            partition_index += 1
    swap(arr, right, partition_index)
    return partition_index


def swap(arr, first_index, second_index):
    temporary = arr[first_index]
    arr[first_index] = arr[second_index]
    arr[second_index] = temporary


print(quick_sort(numbers, 0, len(numbers)-1))
