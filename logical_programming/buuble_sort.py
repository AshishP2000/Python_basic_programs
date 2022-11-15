import logging


def bubble_sort(arr1):
    """
    use bubble sort and use swapping
    :param arr1: unsorted array
    :return: None
    """
    try:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info("Started bubble sort")
        for i in range(0, len(arr1) - 1):
            for j in range(len(arr1) - 1):
                if arr1[j] > arr1[j + 1]:
                    temp = arr1[j]
                    arr1[j] = arr1[j + 1]
                    arr1[j + 1] = temp
        print("Sorted array is:")
        for i in range(len(arr1)):
            print("% d" % arr1[i], end=" ")
        logging.info("Finished bubble sort")
    except ArithmeticError:
        logging.error(ArithmeticError)
        print(ArithmeticError)


if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
