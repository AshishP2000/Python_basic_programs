import logging


def perfect_number(param1):
    """
    function perfect_number: finding the given number is perfect number or not
    :param param1: int,Giving range to the loop
    :return: None
    """
    try:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info("Started perfect_number program")
        sum1 = 0
        for i in range(1, x):
            if x % i == 0:
                sum1 = sum1 + i
        if sum1 == x:
            print(x, "is a Perfect Number")
        else:
            print(x, "is not a Perfect Number")
        logging.info("Finished perfect_number program")
    except ArithmeticError:
        logging.info(ArithmeticError)
        print(ArithmeticError)


if __name__ == '__main__':
    x = int(input("Enter number to check Perfect Number: "))
    perfect_number(param1=x)
