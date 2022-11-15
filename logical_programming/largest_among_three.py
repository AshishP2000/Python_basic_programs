import logging
import traceback


def largest_among_three(input_number1, input_number2, input_number3):
    """
    function largest_among_three: use comparison operator and find largest number
    :param input_number1: int,number 1
    :param input_number2: int,number 2
    :param input_number3: int,number 3
    :return: None
    """
    try:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info("Started largest_among_three")
        if input_number1 > input_number2 and input_number1 > input_number3:
            print(input_number1, "is larger than", input_number2, "", input_number3)
        elif input_number2 > input_number1 and input_number2 > input_number3:
            print(input_number2, "is larger than", input_number1, "", input_number3)
        elif input_number3 > input_number1 and input_number3 > input_number2:
            print(input_number3, "is larger than", input_number1, "", input_number2)
        logging.info("Finished largest_among_three")
    except ArithmeticError:
        logging.error(ArithmeticError)
        print(ArithmeticError)
    except NameError:
        print(NameError)


if __name__ == '__main__':
    number1 = int(input("Enter 1st number: "))
    number2 = int(input("Enter 2nd number: "))
    number3 = int(input("Enter 3rd number: "))
    largest_among_three(input_number1=number1, input_number2=number2, input_number3=number3)
