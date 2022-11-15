import logging


def reverse_number(input_number):
    """
    function reverse_number: to reverse the number
    :param input_number: int,taking only input from user
    :return: None
    """
    try:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info("Started Reverse Number: ")
        reverse = 0
        while input_number != 0:
            num = input_number % 10
            reverse = (reverse * 10) + num
            input_number = int(input_number / 10)
        print(reverse)
        logging.info("Finished Reverse Number")
    except ZeroDivisionError:
        logging.error(ZeroDivisionError)
        print(ZeroDivisionError)
    except ArithmeticError:
        logging.error(ArithmeticError)
        print(ArithmeticError)


if __name__ == '__main__':
    number = int(input("Enter number to Reverse: "))
    reverse_number(input_number=number)



