from numpy import *
import itertools

def quickSort(array):

    # print (len(array))
    if len(array) <= 1:
        return array

    sortedArray = zeros(len(array))
    # print(sortedArray)


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
    # print(sortedArray)

    if p_bigger == len(array)-1 :
        p_bigger -= 1
    elif p_bigger == 0:
        p_bigger += 1

    smaller = quickSort(sortedArray[:p_bigger])
    bigger = quickSort(sortedArray[p_bigger:])

    # print(smaller)
    # print(bigger)
    return map(int, smaller) + map(int, bigger)

# print(len([1, 2, 3]))

def main():
    array=[5, 4 ,8 ,12, 67, 75, 33]
    sorted = quickSort(array)
    print(array)
    print(sorted)
    # print(array[:0])
    # print(array[0:])
if __name__== "__main__":
    main()