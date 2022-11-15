import logging


def swap_2_numbers(input_number1, input_number2):
    """
    function swap_2_numbers: it swaps two numbers from 1st variable to 2nd variable using third variable
    :param input_number1: int,1st number
    :param input_number2: int,2nd number
    :return: None
    """
    try:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.info("Started swap_2_numbers")
        temp = 0
        print("Before Swapping")
        print("Position 1 = ", input_number1, end=" ")
        print("| Position 2 = ", input_number2)
        temp = input_number1
        input_number1 = input_number2
        input_number2 = temp
        print("After Swapping")
        print("Position 1 = ", input_number1, end=" ")
        print("| Position 2 = ", input_number2)
        logging.info("Finished swap_2_numbers")
    except ArithmeticError:
        logging.error(ArithmeticError)
        print(ArithmeticError)


if __name__ == '__main__':
    number1 = int(input("Enter 1st Number: "))
    number2 = int(input("Enter 2nd Number: "))
    swap_2_numbers(input_number1=number1, input_number2=number2)
