
from numpy import *
from concurrent.futures import ThreadPoolExecutor
# import itertools


def InsertionSort(array):
    for j in range(len(array))[1:]:
        i = j-1
        while array[i+1] < array[i] and i >= 0:
            array[i], array[i+1] = array[i+1], array[i]
            i -= 1
    return array


def quickSort(array, executor, org_len):
    if len(array) <= 1:
        return array
    if len(array) <= 0.4*org_len:
        return InsertionSort(array)
    sortedArray = zeros(len(array))
    p_smaller = 0
    p_bigger = len(array) - 1
    i_arr = 1
    pivot = array[0]
    while (p_smaller != p_bigger):
        if array[i_arr] < pivot:
            sortedArray[p_smaller] = array[i_arr]
            p_smaller += 1
        else:
            sortedArray[p_bigger] = array[i_arr]
            p_bigger -= 1
        i_arr += 1
    sortedArray[p_bigger] = pivot

    if p_bigger == len(array)-1:
        p_bigger -= 1
    elif p_bigger == 0:
        p_bigger += 1
    smaller = executor.submit(quickSort, sortedArray[:p_bigger], executor, org_len)
    bigger = executor.submit(quickSort, sortedArray[p_bigger:], executor, org_len)

    return map(int, smaller.result()) + map(int, bigger.result())


def main():
    array = [5, 4, 8, 12, 67, 75, 33, 44, 321, 7, 55, 84, 855, 1]
    org_len = len(array)
    # print(InsertionSort(array))
    executor = ThreadPoolExecutor(8)
    # x = executor.submit(InsertionSort, array)
    # y = x.done()
    # z = x.result()
    # print(x)
    # print(y)
    # print(z)
    sorted = quickSort(array, executor, org_len)
    print(array)
    print(sorted)

if __name__ == "__main__":
    main()
