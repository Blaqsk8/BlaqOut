#!python
# Binary Search
# Author Robert Wilson

def binary_search(arr, lo, hi, search):

    while lo <= hi:
        print(lo, hi)
        mid = lo + (hi - lo) // 2
        print(mid)
        if arr[mid] == search:
            return mid

        elif arr[mid] < search:
            lo = mid + 1

        else:
            hi = mid - 1

    return -1


if __name__ == '__main__':

    array = [2, 3, 4, 10, 40]
    search_number = int(input("Please enter an integer you would like to find in list: "))

    element = binary_search(array, 0, len(array) - 1, search_number)

    if element != -1:
        print("Element %d is present at index %d" % (search_number, element))
    else:
        print("Number not present")
