numbers = [99, 44, 45, 32, 1, 22, 7, 173, 6, 3, 15, 0, 2]
# numbers = [99, 44, 0, 2]


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    length = len(arr)
    mid = length // 2
    left = arr[:mid]
    right = arr[mid:]
    print("Left {}".format(left))
    print("Right {}".format(right))
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    print(left, right)
    return result + left[left_index:] + right[right_index:]


answer = merge_sort(numbers)
print(answer)
