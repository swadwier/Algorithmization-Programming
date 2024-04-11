# array_of_numbers = [1, 43, 4, 8, 30, 77, 92, 0]
import copy


def sortirovka(blocks):
    arr = copy.deepcopy(blocks)
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr



