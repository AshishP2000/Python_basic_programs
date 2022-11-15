import logging


def merge_sort(array1, left_index, right_index):
    """
    dividing array into subarrays
    :param array1: unsorted array
    :param left_index: left side element
    :param right_index: right side element
    :return: array
    """
    if left_index >= right_index:
        return

    middle = (left_index + right_index) // 2
    merge_sort(array1, left_index, middle)
    merge_sort(array1, middle + 1, right_index)
    merge(array1, left_index, right_index, middle)


def merge(array1, left_index, right_index, middle):
    """

    :param array1:
    :param left_index: left side element
    :param right_index: right side element
    :param middle: middle element
    :return:None
    """
    try:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info("Started merge sort")
        # Creating subparts of a arrays
        left_sublist = array1[left_index:middle + 1]
        right_sublist = array1[middle + 1:right_index + 1]

        # Initial values for variables that we use to keep
        # track of where we are in each array1
        left_sublist_index = 0
        right_sublist_index = 0
        sorted_index = left_index

        # traverse both copies until we get run out one element
        while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist):

            # If our left_sublist has the smaller element, put it in the sorted
            # part and then move forward in left_sublist (by increasing the pointer)
            if left_sublist[left_sublist_index] <= right_sublist[right_sublist_index]:
                array1[sorted_index] = left_sublist[left_sublist_index]
                left_sublist_index = left_sublist_index + 1
                # Otherwise add it into the right sublist
            else:
                array1[sorted_index] = right_sublist[right_sublist_index]
                right_sublist_index = right_sublist_index + 1

                # move forward in the sorted part
            sorted_index = sorted_index + 1

            # we will go through the remaining elements and add them
        while left_sublist_index < len(left_sublist):
            array1[sorted_index] = left_sublist[left_sublist_index]
            left_sublist_index = left_sublist_index + 1
            sorted_index = sorted_index + 1

        while right_sublist_index < len(right_sublist):
            array1[sorted_index] = right_sublist[right_sublist_index]
            right_sublist_index = right_sublist_index + 1
            sorted_index = sorted_index + 1
        logging.info("Finished merge sort")
    except ArithmeticError:
        print(ArithmeticError)


if __name__ == '__main__':
    array1 = [44, 65, 2, 3, 58, 14, 57, 23, 10, 1, 7, 74, 48]
    merge_sort(array1, 0, len(array1) - 1)
    print(array1)
