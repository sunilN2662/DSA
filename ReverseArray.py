def reverseArry(array):
    print(array)
    reverse_array = array[::-1]
    print(reverse_array)


array = [1, 2, 3, 4, 5, 6, 7]
reverseArry(array)


def reverseAry(Array, start, end):
    print(Array)
    while start < end:
        Array[start], Array[end] = Array[end], Array[start]
        start += 1
        end -= 1
    print(Array)


array = [1, 2, 3, 4, 5, 6, 7, 8]
reverseAry(array, 0, len(array) - 1)

