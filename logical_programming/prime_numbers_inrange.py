import logging


def prime_numbers_inrange(input_number):
    """
    function prime_numbers_inrange: takes range and print prime numbers within that range
    :param input_number: gives the range to print prime numbers
    :return: None
    """
    try:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info("Started Prime numbers in range")
        for i in range(1, input_number + 1):
            flag = 0
            for j in range(1, i + 1):
                if (i % j == 0):
                    flag = flag + 1
            if (flag <= 2):
                print(i, "is prime Number")
        logging.info("Finished Prime numbers in range")
    except ArithmeticError:
        logging.error(ArithmeticError)
        print(ArithmeticError)


if __name__ == '__main__':
    number = int(input("Give the range of prime number: "))
    prime_numbers_inrange(input_number=number)
