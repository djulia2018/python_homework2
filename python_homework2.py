def binary_search(sorted_array, item):
    low = 0
    high = len(sorted_array)
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        guess = sorted_array[mid]
        if item == guess:
            return guess
        if item < guess:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(binary_search(range(1,101), 50))

def select_sort(array):
    new_lst = []
    while len(array) > 0:
        i = 0
        m = len(array)
        smallest = array[0]
        while i < m:
            if array[i] < smallest:
                smallest = array[i]
            i += 1
        new_lst.append(smallest)
        array.remove(smallest)
        i += 1
    return new_lst

print(select_sort([8,3,14,5,7,10,1,2]))