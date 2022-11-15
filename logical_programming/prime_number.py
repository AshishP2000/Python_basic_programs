import logging


def prime_number(input_number):
    """
    function prime_number: To check if given number is prime or not
    :param input_number: int, number from user to check prime or not
    :return: None
    """
    try:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info("Started Prime Number")
        flag = 0
        for i in range(3, input_number):
            if (input_number % i == 0):
                flag = flag + 1
        if (flag == 0):
            print(input_number, "is prime Number")
        elif (flag >= 1):
            print(input_number, "is not a prime Number")
        else:
            print(input_number, "is Invalid")
        logging.info("Finished Prime Number")
    except ArithmeticError:
        logging.error(ArithmeticError)
        print(ArithmeticError)


if __name__ == '__main__':
    number = int(input("Enter number to check Prime Number: "))
    prime_number(input_number=number)
