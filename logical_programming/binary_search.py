import logging


def binarySearchAppr(arr, start, end, x):
    """
    param arr: it is a string array
    :param start: start of an array
    :param end: end of an array
    :param x: word to search from list
    :return: index if word is present and -1 if word is not present
    """
    try:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info("Started binary_search")
        # check condition
        if end >= start:
            mid = start + (end - start) // 2
            # If element is present at the middle
            if arr[mid] == x:
                return mid
            # If element is smaller than mid
            elif arr[mid] > x:
                return binarySearchAppr(arr, start, mid - 1, x)
            # Else the element greator than mid
            else:
                return binarySearchAppr(arr, mid + 1, end, x)
        else:
            # Element is not found in the array
            return -1
        logging.info("Finished prime_anagram_palindrome")
    except ArithmeticError:
        logging.error(ArithmeticError)
        print(ArithmeticError)


if __name__ == '__main__':
    arr = sorted(['zee', 'java', 'python', 'ashish'])
    x = input("Enter word you want to search: ")
    result = binarySearchAppr(arr, 0, len(arr) - 1, x)
    if result != -1:
        print("Element is present at index " + str(result))
    else:
        print("Element is not present in array")
