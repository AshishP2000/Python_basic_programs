import logging


def power(input_number):
    """
    power gives power of 2
    :param input_number: int,giving the range
    :return: None
    """
    try:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info("Started Power of 2")
        for i in range(1, input_number + 1):
            print(2 * i)
        logging.info("Finished power of 2")
    except ArithmeticError:
        logging.error(ArithmeticError)
        print(ArithmeticError)


if __name__ == '__main__':
    number = int(input("Enter Power value N: "))
    power(input_number=number)
